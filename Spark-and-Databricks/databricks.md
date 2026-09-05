
## DataBricks concepts

### Task

A task is an individual step in a Databricks Job.
Tasks can have dependencies.

Job → Task → Spark Job → Stage → Task/Partition

DataBricks will show you task-level DAG:
```
extract
   ↓
clean
   ↓
transform
  ↙ ↘
aggregate  validate
  ↘ ↙
 publish

```

### Stage

When Databricks runs a Spark job, Spark breaks the computation into stages based on operations such as shuffle boundaries. 
These are execution-level units inside Spark, not workflow steps.

### Adaptive Query Execution

Databricks Adaptive Query Execution (AQE) is a Spark optimization feature that lets Spark change its execution plan while the query is running, based on the data it actually sees.

- Dynamically coalescing shuffle partitions (combine small partitions)
- Handling data skew: detect unusually large shuffle partitions and split skewed partitions
- Dynamically changing join strategy 

### Salting

Salting is a technique for fixing data skew in a join.

Example:
- customer_1 has 1000 000 orders and all other customers only few
- add artificial/random salt key: 
    ```
    customer_id | salt
    -------------|-----
    1            | 0
    1            | 1
    1            | 2
    1            | 3
    ...
    1            | 9
    ```
    Now customer 1's huge amount of data can be distributed across 10 different join keys:

### Liquid Clustering

Partitioning organizes data into fixed buckets you choose upfront. 
Liquid Clustering lets Databricks continuously organize data based on the columns you specify, without requiring fixed partitions.

You tell Databricks which columns are important for clustering:
```
CREATE TABLE orders (
    order_id BIGINT,
    customer_id BIGINT,
    order_date DATE,
    amount DECIMAL(18,2)
)
USING DELTA
CLUSTER BY (customer_id, order_date);
```

Databricks then organizes the underlying data so that records with similar clustering values are colocated.

Partitioning can be better than Liquid Clustering when the partition column gives you a small number of large, naturally separated groups and your queries consistently filter on that column.

Liquid Clustering is attractive when query/update patterns are multidimensional or evolve over time.

### target-file discovery

Reduce the number of files Databricks has to consider/read to answer a query. 
You do it by using partition and liquid clustering

```
10 TB table
   ↓
inspect Delta/file statistics
   ↓
eliminate files that cannot contain customer_id = 12345
   ↓
eliminate files outside the date range
   ↓
read only relevant files
```

To check look at query profile:
```
Files read
Files pruned / skipped
Bytes read
Rows read
Rows returned
```

## Databricks Interview Questions

### How to create a partitioned Delta table

When you run:
```
CREATE TABLE orders (
    order_id BIGINT,
    customer_id BIGINT,
    order_date DATE,
    amount DECIMAL(18,2),
    status STRING
)
USING DELTA
PARTITIONED BY (order_date);
```

It will organized data like this:
```
orders/
  order_date=2026-08-29/
  order_date=2026-08-30/
  order_date=2026-08-31/
  order_date=2026-09-01/
```

Then you can run query that uses partition pruning:
```
SELECT *
FROM orders
WHERE order_date = '2026-09-01';
```


### Delta Lake + Concurrency

You have a Databricks Delta table with 10 billion rows:

orders
------
order_id
customer_id
order_date
status
amount
updated_at

Every day, you receive a CDC feed containing 50 million changed records. Some records are inserts, some updates, and some deletes.

Your current implementation is:
```
MERGE INTO orders t
USING daily_cdc s
ON t.order_id = s.order_id

WHEN MATCHED AND s.operation = 'DELETE'
  THEN DELETE

WHEN MATCHED
  THEN UPDATE SET *

WHEN NOT MATCHED
  THEN INSERT *
```

The job has become extremely slow and expensive. You discover that the target table is frequently being scanned, and sometimes multiple CDC jobs run concurrently for different dates.

What would you do?

#### Answer

1. Deduplicate the CDC source first
    ```
    WITH ranked_cdc AS (
        SELECT *,
            ROW_NUMBER() OVER (
                PARTITION BY order_id
                ORDER BY sequence_number DESC
            ) AS rn
        FROM daily_cdc
    )
    SELECT *
    FROM ranked_cdc
    WHERE rn = 1;
    ```
2. Reduce the target data that MERGE has to consider
    ```
    MERGE INTO orders t
    USING deduplicated_cdc s
    ON t.order_id = s.order_id
    AND t.order_date >= s.min_order_date
    AND t.order_date <= s.max_order_date
    ```
3. Reconsider traditional partitioning
4. Liquid Clustering vs partitioning
5. Optimize file layout: healthy file sizes (huge numbers of tiny files is bad)
6. Concurrent MERGEs are a major issue: 
   - If multiple jobs are modifying the same Delta table concurrently, I need to understand whether they can touch overlapping files.
   - Delta Lake provides transactional concurrency control, so concurrent operations don't simply corrupt the table.

### Databricks job processing 2 TB of JSON data every night

You have a Databricks job processing 2 TB of JSON data every night.

```
df = spark.read.json("/mnt/raw/events/")

df = df.filter("event_date >= '2026-08-01'")

df = df.join(
    customers,
    df.customer_id == customers.customer_id,
    "left"
)

df = df.groupBy("customer_id").agg(
    count("*").alias("event_count"),
    sum("amount").alias("total_amount")
)

df.write.mode("overwrite").saveAsTable("daily_customer_metrics")
```

The job currently takes 2 hours, and the Spark UI shows:
-    A large shuffle
-    Significant data skew
-    Executors frequently spill to disk
-    The customers table is only 50 MB
-    The raw JSON contains billions of records
-    The output table is queried frequently by customer_id and event_date

Interview question: How would you diagnose and optimize this Databricks job? Explain the changes you would make and why.

#### Answer

1. inspect:
- Number of stages and tasks
- Shuffle read/write size
- Task duration distribution
- Records read/written
- Spill to memory/disk
- Whether a small number of tasks are taking much longer than others
- Physical execution plan using df.explain("formatted")
2. Filter as early as possible
3. Convert the raw JSON to Delta rather than repeatedly querying JSON.
4. Broadcast the 50 MB customer table
```
from pyspark.sql.functions import broadcast
df = df.join(
    broadcast(customers),
    "customer_id",
    "left"
)
```
5. Investigate the skew
```
df.groupBy("customer_id") \
  .count() \
  .orderBy("count", ascending=False) \
  .show(20)
```
6. Don't blindly increase executor memory
7. Use Delta for the output

```
from pyspark.sql.functions import broadcast, col, count, sum

events = (
    spark.read
    .format("delta")
    .table("events_bronze")
    .select("customer_id", "event_date", "amount")
    .filter(col("event_date") >= "2026-08-01")
)

result = (
    events
    .join(
        broadcast(customers),
        "customer_id",
        "left"
    )
    .groupBy("customer_id", "event_date")
    .agg(
        count("*").alias("event_count"),
        sum("amount").alias("total_amount")
    )
)

result.write \
    .format("delta") \
    .mode("append") \
    .saveAsTable("daily_customer_metrics")

```