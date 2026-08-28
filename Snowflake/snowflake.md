# snowflake

# Table of Contents
- [Architecture](#architecture)
- [Data Loading](#dataloading)
- [Performance Optimization](#performanceoptimization)
- [Snowpipe](#snowpipe)
- [Timetravel](#timetravel)
- [Table Types](#tabletypes)
- [View Types](#viewtypes)
- [Zero-copy cloning](#zerocopycloning)
- [Data Sharing](#datasharing)
- [Data Sampling](#datasampling)
- [Streams](#streams)
- [Change Tracking](#changetracking)
- [Tasks](#tasks)
- [UDF](#udf)
- [Stored Procedures](#storedprocedures)
- [Spark](#spark)
- [Security](#security)
- [Best practices](#bestpractices)
- [Interview Questions](#interviewquestions)

## Architecture <a id="architecture"></a>

* storage
* compute (virtual warehouse): cache and micro-partitions
* cloud services: authentication, authorization, infrastructure manager, metadata manager, optimizer, Transaction Management

### Tools

* snowSight: Web UI
* snowSQL: command line interface
* SnowCLI: Comprehensive Command-Line Interface. extends the functionality of SnowSQL by: managing account configurations, setting up integrations, and automating complex tasks.
* SnowPipe: Continuous Data Ingestion
* snowPark:  Integration of Programming Languages

### scalability

* vertical - depends on query dependency
* horizontal - driven my number of concurrent queries

## Data Loading <a id="dataloading"></a>

* bulk
* continuous

### bulk data loading

Uses warehouse

#### stages

stage = database object containing location where we load data from

There are:

* external stage (aws s3 or azure blob storage).  
* internal stage: (local storage). 

#### load data to tables

Steps to load data:
* 'CREATE STORAGE INTEGRATION' object to be able to access your S3 bucket from Snowflake
* Create AWS Role to access the Snowflake Integration Object
* 'CREATE FILE FORMAT' in Snowflake
* 'CREATE STAGE' loads data from storage
```
CREATE STAGE my_s3_stage
  URL = 's3://mybucket/path/to/data/'
  CREDENTIALS = (AWS_KEY_ID = '<AWS_ACCESS_KEY>' 
                 AWS_SECRET_KEY = '<AWS_SECRET_KEY>')
  FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '"');
```
* Create target table:
```
CREATE OR REPLACE TABLE my_table (
  id INT,
  name STRING,
  email STRING,
  created_at TIMESTAMP
);
```
* 'COPY' load data from STAGE to a table. Ingests data to snowflake in batches at time intervals. Snowflake 'COPY' command scheduled using Snowflake tasks or trigger copy commands using python/glue/airflow
```
COPY INTO my_table
  FROM @my_s3_stage
  FILES = ('data_file.csv')
  ON_ERROR = 'SKIP_FILE'        -- Skip the file if there is an error
  VALIDATION_MODE = 'RETURN_ERRORS'; -- Return errors in the output
```
* Monitor loading process:
```
SELECT * 
FROM INFORMATION_SCHEMA.COPY_HISTORY 
WHERE TABLE_NAME = 'MY_TABLE' 
ORDER BY LOAD_TIME DESC;
```

COPY command can have:
* on error option
* validation option

#### transform data

Can be done with COPY command using SELECT statement:

```
INSERT INTO transformed_data (user_id, full_name, age_category)
  SELECT 
    id,
    CONCAT(first_name, ' ', last_name) AS full_name,  -- Concatenating first and last name
    CASE 
      WHEN age < 18 THEN 'Minor'
      WHEN age BETWEEN 18 AND 65 THEN 'Adult'
      ELSE 'Senior'
    END AS age_category  -- Categorizing based on age
  FROM users;
```

### loading unstructured data

You can load json, xml, parquet etc data formats including nested data, arrays etc..

To do that you need to add 'file format' to the COPY command.

Each document will be a new row and later you need to use 'dot notation', 'table' or 'flatten' functions.

### continuous data loading

* write / load the data into staging location (as before) on S3 and
* Snowpipe object (continous data ingestion) is triggered as soon as data is written to S3 and it will write the data to snowflake table

OR

* There is a Kafka-Snowflake connector
  - Kafka produces events → connector reads them → buffers/stages them → Snowflake loads them in micro-batches into tables

#### Using Snowpipe for Continuous Data Loading

* Create an External Stage
```
CREATE STAGE my_s3_stage
  URL = 's3://mybucket/data/'
  CREDENTIALS = (AWS_KEY_ID = '<AWS_ACCESS_KEY>' 
                 AWS_SECRET_KEY = '<AWS_SECRET_KEY>')
  FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '"');
```
* Create the Target Table
```
CREATE OR REPLACE TABLE my_table (
  id INT,
  name STRING,
  email STRING,
  created_at TIMESTAMP
);
```
* Create the Snowpipe
```
CREATE PIPE my_pipe
  AUTO_INGEST = TRUE
  AS
  COPY INTO my_table
  FROM @my_s3_stage
  FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '"')
  ON_ERROR = 'SKIP_FILE';  -- Skips files with errors
```
* Set Up Event Notification on S3: To trigger Snowpipe automatically whenever a new file is uploaded to the S3 bucket
* Monitor the Data Loading Process
```
SELECT * 
FROM INFORMATION_SCHEMA.PIPE_USAGE_HISTORY
WHERE PIPE_NAME = 'MY_PIPE'
ORDER BY START_TIME DESC;
```

## Performance Optimization <a id="performanceoptimization"></a>

Traditional: add indexes, primary keys, partition data, analyze query plan

__In snowflake: everything is managed in micro-partitions__.

Optimization in snowflake:
* assign appropriate data types
* size virtual warehouse
* cluster keys: to locate micro-partitions. Managed by snowflake. Use it for very large (data size) tables.
* cache (store query results) 

### Data Modeling and Schema Design

- __Star Schema or Snowflake Schema__: Use a star or snowflake schema to structure your data efficiently. Fact tables store aggregated or transactional data, while dimension tables store descriptive attributes.
- __Avoid Large Fact Tables with Many Null Values__: Tables with many NULL values or sparse data increase storage costs and slow down queries. Normalize the data as much as possible to avoid large, sparse tables.
- Denormalization for Read Performance

### Query Optimization

Snowflake optimizes most queries automatically, but you can still make improvements by focusing on certain aspects of your queries.

- __Use JOIN Conditions Efficiently__: Avoid unnecessary joins and filter out data as early as possible in your query
- __Use WITH Clauses (CTE)__: Common Table Expressions (CTEs) can improve query readability and simplify complex queries, but avoid excessive use of them in very large datasets, as __it could create performance overhead__. Instead, consider using temporary tables or subqueries for complex operations.
- __Minimize the Use of DISTINCT and GROUP BY__
  - SELECT DISTINCT customer_id FROM events;
    - Scan all relevant micro-partitions, 
    - Extract customer_id
    - Redistribute rows across nodes so identical values end up together
    - Sort or hash values, Remove duplicates
- Use __EXPLAIN__ to Analyze Query Plans

### Clustering and Partitioning

Clustering and partitioning are key for optimizing performance, especially when dealing with large datasets. 
Snowflake uses micro-partitioning by default, but you can optimize it further using clustering keys.

You don’t manually “partition” data the way you do in MongoDB or Cosmos DB. 
Instead, Snowflake uses automatic micro-partitioning, and your job is to guide how data is organized so queries prune as much data as possible.

How Snowflake Partitioning Actually Works: Micro-partitions
- Size: ~50–500 MB (compressed)
- Stored in columnar format
- Contains metadata:
  - min/max values per column
  - distinct values
  - null counts

How You “Partition” Data in Snowflake (Indirectly): Control Data Ingestion Order
- Snowflake creates micro-partitions based on insert order.
  ```
  ORDER BY company_id, event_date
  ```

Snowflake does NOT update micro-partitions in place. Instead, it uses an __immutable storage model__.

Clustering Keys:
- Define the columns that Snowflake should use to cluster the data at a physical level. This helps reduce the need for Snowflake to scan entire partitions during a query.
- If your queries often filter or group by a specific column, clustering by that column can speed up the query execution.

Clustering example:
```
CREATE TABLE employees (
  company_id STRING,
  employee_id STRING,
  field_1 STRING,
  field_2 STRING,
  field_3 STRING,
  created_at TIMESTAMP
)
CLUSTER BY (company_id, field_1, field_2, field_3);
```

- Organizes micro-partitions around these columns
  - Partition P1 will contain company_id = A
  - Partition P2 will contain company_id = B
- Improves pruning (skip reading large portions of storage)

Choosing Good Clustering Keys:
- Based on your queries:
  - Put most selective columns first
  - Use columns in: WHERE, JOIN, ORDER BY


### Scaling the Virtual Warehouse

- __Scale Virtual Warehouses__: Snowflake allows you to scale virtual warehouses vertically (by increasing the size) or horizontally (by adding clusters).
  - Heavy queries
  - Large joins
  - Complex aggregations
- __Multi-Cluster Warehouses__: Use multi-cluster virtual warehouses to handle large concurrent workloads. Snowflake automatically scales the number of clusters based on the number of queries running
  - More concurrent queries
  - No queueing


### Caching

Snowflake’s caching mechanism automatically stores the results of queries and the data in result cache and metadata cache.

In Snowflake, the “query cache” is mostly automatic:
- If you run an identical query again, Snowflake can return the exact previous result instantly without re-scanning data. Stored for 24 hours
- Even if query text is identical, cache is skipped if:
  - Underlying data changed
  - You use non-deterministic functions

### Data Compression

Snowflake uses columnar storage to compress data and improve I/O performance. Snowflake automatically applies compression algorithms like ZSTD, Snappy, and LZ4 for optimal storage and query performance.

### Monitoring and Query Profiling

Monitoring your queries, virtual warehouses, and storage is key to understanding where your performance bottlenecks lie.

Snowflake Monitoring focuses on:
- warehouses: 
  - look at: CPU pressure, concurrency, queueing, credit consumption, auto-suspend behavior
  - Common issues: queries waiting in queue, warehouse too small, warehouse constantly restarting
  - Key metrics: queued queries, running queries, load percentage
  - Increase warehouse size when: spills (to storage), queueing, slow joins
  - Increase number of warehouses when: queued overload time, high parallel query counts
- query history: execution time, queued time, bytes scanned, rows produced
- storage: table storage, time travel storage, fail-safe storage, stage usage
- concurrency
- costs
- failures
- load patterns

- __Query Profiling__: Use Snowflake’s Query History and Query Profile tools to identify slow queries, unnecessary table scans, or missing indexes.
```
SELECT * 
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
WHERE QUERY_TEXT LIKE '%SELECT%'
ORDER BY START_TIME DESC;
```
  - Most Important Query Profile Operators: table scan, filter, joins, repartitions (group by), aggregates, sort
- __Warehouse Monitoring__: Monitor warehouse usage and performance to ensure you're not over-provisioning or under-provisioning your compute resources.
- __Resource Monitoring__: Use Snowflake's Resource Monitors to track compute usage and prevent overages.

### Snowflake development

- One shared DEV database and isolated schemas per engineer, use zero-copy cloning, shared and personal schemas
- One STAGE (uintegration testing, data validation, performance) and PROD database
- Medallion architecture on snowflake: One production database with separate schemas for each layer: easier governance, cleaner CI/CD, lineage, cross-layer queries simpler
- CI/CD for snowflake: 
  - automated testing, validation, deployment
  - tools: git, dbt, github actions
  - feature branch + test in dev
  - git PR -> github action -> dbt compile + dbt test + dbt run -> git PR approved
  - deploy to STAGE env + more/manual validate
  - deploy to PROD
  - Zero copy clone of schema 
    - zero-copy clone copies the metadata pointers to objects and data
    - once you create a zero-copy clone, the clone becomes an independent writable environment.
    - you can add tables and data without affecting original
- can different showflake warehouses and have them to use the same storage i.e. database?
  - Yes: Compute (warehouses) and storage (databases/tables) are completely separated.

## Snowpipe <a id="snowpipe"></a>

Snowpipe is Snowflake continous data ingestion service. 
It loads data within minutes after files are added to a stage and submitted for ingestion. 
It loads data from staged files in micro-batches (instead of COPY statements that are used to load larger batches).

Steps:
* CREATE STAGE object
  ```
  CREATE OR REPLACE STAGE analytics.raw.events_stage
  URL = 's3://my-event-bucket/events/'
  STORAGE_INTEGRATION = my_s3_integration
  FILE_FORMAT = analytics.raw.json_format;
  ```
* CREATE PIPE object AS COPY INTO ...
  ```
  CREATE PIPE my_pipe
  AS
  COPY INTO my_table
  FROM @my_stage
  FILE_FORMAT = (TYPE = 'JSON');
  ```
* Create AWS S3 Event Notification on create events = Snowflake INTEGRATION
  - secure, credential-free connection between Snowflake and cloud storage
  - Create it like this:
    ```
    CREATE STORAGE INTEGRATION s3_int
    TYPE = EXTERNAL_STAGE
    STORAGE_PROVIDER = S3
    ENABLED = TRUE
    STORAGE_ALLOWED_LOCATIONS = ('s3://my-data-bucket/events/');
    ```
  - Snowflake will generate a trust relationship
  - Create AWS IAM role and attach policy
  - check it: DESC INTEGRATION my_s3_integration;
  - creates AWS SQS queue containing events
- Check Pipe Status: 
  ```
  SELECT SYSTEM$PIPE_STATUS('analytics.raw.events_pipe');
  ```
Key Production Considerations:
- Idempotency. Snowpipe handles retries but you should: include event_id, deduplicate in CURATED layer if needed
  - You usually do NOT clean RAW directly. You deduplicate while loading into CURATED
  - Method 1: Use ROW_NUMBER(): 
    ```
    CREATE OR REPLACE TABLE analytics.curated.events AS
    SELECT *
    FROM (
        SELECT *,
              ROW_NUMBER() OVER (
                  PARTITION BY event_id
                  ORDER BY event_time DESC
              ) AS rn
        FROM analytics.raw.events
    )
    WHERE rn = 1;
    ```
    - groups by business key (event_id)
    - keeps latest record
    - removes duplicates
  - Method 2: QUALIFY
  - Method 3: GROUP BY (only if simple aggregation)
    ```
    SELECT DISTINCT * FROM analytics.raw.events;
    ```
- File sizing: Best practice: 10–100 MB files
- Error handling: ON_ERROR = 'CONTINUE' ?

Snowpipe keeps the state of processing and it will not load the same file again.

Multiple files can be processed at the same time, but one file cannot be processed in parallel. File size should be 100-250MB. 

To extract data from Snowflake to AWS S3 use 'COPY' command

Automatically load new file if is loaded into some bucket / container. It is serverless.

You need to create 'STAGE', test 'COPY' command and create 'Notification' (to trigger it).



## Time Travel <a id="timetravel"></a>

Time Travel in Snowflake allows you to query, clone, or restore data as it existed at a specific point in time (__within a defined retention period__). 
This feature is very useful for __recovering lost data, auditing, and comparing historical versions of data__. 
Snowflake keeps a historical record of changes made to tables, which allows you to access data from the past without requiring backups.

Time Travel is built into Snowflake, and it works across different objects, including __tables, schemas, and databases__.

Snowflake tracks all changes to data in the system (__inserts, updates, deletes__) at the storage level. 
When a record is updated or deleted, __Snowflake doesn’t immediately remove it but instead marks it as changed__, and the original data is still available within the Time Travel window.

Go back 60 s

```
SELECT * FROM <table> AT (OFFSET => -60 )
```

Go back before date

```
SELECT * FROM <table> BEFORE (timestamp => '2023-11-12 ...'::timestamp)
```

To recreate table at an older monent, create a new table and reinsert all data

To undrop a dropped table:

```
UNDROP TABLE <table>
```

The default retention period for Time Travel in Snowflake is __1 to 90 days__, depending on your Snowflake edition and configuration.

You can set the __retention period for individual tables or databases__.

You can use Time Travel in Snowflake to access and revert to a previous table schema by querying historical versions of the table

Reverting to a Previous Schema:
```
UNDROP TABLE my_table BEFORE (STATEMENT => '2023-01-05 10:00:00');
```


## Table types <a id="tabletypes"></a>

* __Permanent__: 'CREATE TABLE'. default, normal type with time travel and fail-safe
* __Transient__: 'CREATE TANSIENT TABLE'. No fail-safe, no time-travel. It is used where "data persistence" is required but doesn't need "data retention" for a longer period.
* __Temporary__: 'CREATE TEMPORARY TABLE'. No fail-safe. Exists only in __current session__ i.e. other users or sessions do not see it. Mostly used for transitory data like ETL/ELT
* __Dynamic__: 'CREATE DYNAMIC TABLE': Continously materlizes the results of the query you provide.


## View types <a id="viewtypes"></a>

* __Standard View__
* __Secure View__: accessed only by authorized users
* __Materialized View__: These views store the result from the main source using filter conditions. Materialized view is auto-refreshed

### Snowflake Dynamic Tables vs Materialized Views

Dynamic Table:
- Think: “auto-updating table”
- Acts like a normal table, but Snowflake keeps it in sync automatically when source tables change
- Ideal for staging, data pipelines, or slowly changing aggregates

Materialized View
- Think: “query cache”
- Limited to single query logic
- Great for accelerating repeated queries (like a precomputed aggregate)
- Snowflake incrementally updates it on writes to base table, but not as flexible as dynamic tables

| Feature                              | **Dynamic Table**                                                                                          | **Materialized View (MV)**                                                |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Definition**                       | A table whose data is **automatically maintained** based on a SQL query (like an auto-updating ETL output) | A **stored precomputed result of a query**, updated incrementally         |
| **Storage**                          | Physical table with actual data                                                                            | Physical storage of query result (internal)                               |
| **Refresh**                          | Automatic, continuous refresh when base tables change                                                      | Incremental refresh happens on write to base tables, managed by Snowflake |
| **Queryable**                        | Fully queryable like a normal table                                                                        | Fully queryable like a normal table                                       |
| **Supports Complex Transformations** | Yes, can handle multi-step logic in SQL                                                                    | Limited to **single SELECT statements**, cannot reference other MVs       |
| **Performance**                      | Can be partitioned/clustering optimized for large data; good for heavy ETL pipelines                       | Optimized for small-to-medium aggregation/query speed                     |
| **Time Travel / Fail-safe**          | Yes (inherits table properties)                                                                            | Yes (inherits table properties)                                           |
| **Use Case**                         | Auto-updating ETL pipelines, aggregations, data marts                                                      | Accelerating frequently run queries, caching aggregates                   |


## Zero-copy cloning <a id="zerocopycloning "></a>

Zero-copy cloning is a Snowflake feature that lets you create a copy of a database, schema, or table almost instantly without physically duplicating the data.

The clone initially __shares the same underlying storage (micro-partitions)__ as the source object, which makes it fast, storage-efficient, and cost-effective.

```
CREATE TABLE sales_clone
CLONE sales;
```


## Data Sharing <a id="datasharing"></a>

Data Sharing in Snowflake is a feature that allows one Snowflake account to share live, read-only access to its data with other Snowflake accounts without copying or moving the data.

* data sharing without copy data
* shared data consumed by own compute

```
CREATE SHARE <share>
```

Reader account: non snowflake user. We pay for this account.

### Example:

Provider: Create a Share
```
-- Create a share object
CREATE SHARE sales_share;

-- Add objects to share
GRANT USAGE ON DATABASE sales_db TO SHARE sales_share;
GRANT USAGE ON SCHEMA sales_db.public TO SHARE sales_share;
GRANT SELECT ON TABLE sales_db.public.orders TO SHARE sales_share;

-- Optional: add secure view for filtered access
GRANT SELECT ON VIEW sales_db.public.orders_secure TO SHARE sales_share;
```

Consumer: Access the Share:
```
-- Create a database from the share
CREATE DATABASE sales_db_from_partner
  FROM SHARE provider_account.sales_share;

-- Query the shared data
SELECT * FROM sales_db_from_partner.public.orders;
```


## Data Sampling <a id="datasampling"></a>

### Data samples

Take random sample of you data.

* Row method: every row has x% of being selected
* Block: every block has %x of being selected


Create data samples (random samples):
```
SELECT * 
FROM table_name
[SAMPLE (percentage | number_of_rows)];
```

### Synthetic Data

```
-- Generate 1000 rows of synthetic data
CREATE OR REPLACE TABLE test_data AS
SELECT
    SEQ4() AS id,
    RANDOM() AS value,
    CURRENT_DATE AS created_at
FROM TABLE(GENERATOR(ROWCOUNT => 1000));
```


## Streams <a id="streams"></a>

Streams are objects that record changes made to a table (or view). 
Follows CDC pattern: insert, update, delete statements are propagated.

Streams are most commonly __used together with Tasks__ to build continuous / incremental data pipelines inside Snowflake.

A stream does not store the changed data rows itself. 
It __only stores an offset__ (a pointer) in the table's version history.
When you query the stream → Snowflake computes the delta (what changed) since the last offset by looking at historical micro-partitions.

```
CREATE OR REPLACE STREAM <name> ON TABLE <table name>

# See what the stream currently contains
SELECT * FROM <stream name>

# Consume changes into the target table
-- One-time / scheduled MERGE (in real pipelines this goes inside a TASK)
MERGE INTO <target_table>> AS tgt
USING (
  SELECT
    customer_id,
    name,
    email,
    updated_at,
    -- Handle soft deletes if needed
    IFF(is_active = FALSE, 'DELETE', 'UPSERT') AS change_type
  FROM  <stream name>
  QUALIFY ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY updated_at DESC) = 1
) AS src
ON tgt.customer_id = src.customer_id
  AND tgt.is_current = TRUE

WHEN MATCHED AND src.change_type = 'DELETE' THEN
  UPDATE SET
    valid_to   = src.updated_at,
    is_current = FALSE

WHEN MATCHED AND src.change_type = 'UPSERT' THEN
  UPDATE SET
    valid_to   = src.updated_at,
    is_current = FALSE

WHEN MATCHED AND src.change_type = 'UPSERT' THEN
  INSERT (
    customer_id, name, email, valid_from, valid_to, is_current
  )
  VALUES (
    src.customer_id,
    src.name,
    src.email,
    src.updated_at,
    '9999-12-31',
    TRUE
  )

WHEN NOT MATCHED AND src.change_type = 'UPSERT' THEN
  INSERT (
    customer_id, name, email, valid_from, valid_to, is_current
  )
  VALUES (
    src.customer_id,
    src.name,
    src.email,
    src.updated_at,
    '9999-12-31',
    TRUE
  );
```

Types of streams:
* standard: tracks all DML
* append only: only inserts
* insert only: same as append-only but for external tables

CREATE STREAM ... ON TABLE ....

The 'stream' table contains the original table plus metadata (like if it was an update etc.)

Streams can contain transactions:
```
begin

multiple sql statements

commit
```


## Change Tracking <a id="changetracking"></a>

Read-only alternative to streams. Enables querying change tracking metadata between two points in time

```
ALTER TABLE ... SET CHANGE_TRACKING = TRUE

SELECT * FROM ... AT ( TIMESTAMP > $ts1 )
```

Use it when you do not know when you will need to see or process changes.



## Tasks    <a id="tasks"></a>

Snowflake Tasks are a built-in scheduling and orchestration feature used to automate SQL execution in Snowflake. 
They’re commonly used for ETL/ELT pipelines, data refreshes, and chaining transformations.

A Task is an object that:
- Runs SQL statements automatically
- Can run on a schedule (cron or interval) or
- Run after another task finishes (task dependencies / DAGs)
- Uses a warehouse or serverless compute

Tasks can be dependent, but there can be only one parent.

```
CREATE TASK ... SCHEDULE ... AS ... query
OR
CREATE TASK ... AFTER ... AS ... query
```

Example:
```
CREATE OR REPLACE TASK load_sales_task
  WAREHOUSE = compute_wh
  SCHEDULE = 'USING CRON 0 2 * * * UTC'
AS
INSERT INTO sales_final
SELECT *
FROM sales_stage;
```

Example: Task with Dependencies (DAG):
```
# root task
CREATE OR REPLACE TASK load_raw_task
  WAREHOUSE = compute_wh
  SCHEDULE = '10 MINUTE'
AS
COPY INTO raw_table
FROM @raw_stage;


# child task
CREATE OR REPLACE TASK transform_task
  WAREHOUSE = compute_wh
  AFTER load_raw_task
AS
INSERT INTO clean_table
SELECT *
FROM raw_table
WHERE valid = TRUE;

# final task
CREATE OR REPLACE TASK aggregate_task
  WAREHOUSE = compute_wh
  AFTER transform_task
AS
INSERT INTO agg_table
SELECT date, SUM(amount)
FROM clean_table
GROUP BY date;

# enable all tasks
ALTER TASK load_raw_task RESUME;

# check status
SHOW TASKS;

```

## UDF = user defined functions <a id="udf"></a>

A UDF is a named function that:
- Accepts input parameters
- Returns a single value
- Can be written in: SQL, JavaScript, Python (via Snowpark)

You can use UDFs in: SELECT, WHERE, JOIN, GROUP BY, ORDER BY

2 types of UDF:
* scalar: returns one output row
* tabular: returns 0,1, or many rows

SQL UDF Example:
```
CREATE FUNCTION funct1 (a number, b, number)
RETURNS number
language sql
AS
$$
    SELECT a+b
$$;

SELECT funct1(1,2)
```

Python UDF Example (Snowpark):
```
CREATE OR REPLACE FUNCTION normalize_text(txt STRING)
RETURNS STRING
LANGUAGE PYTHON
RUNTIME_VERSION = '3.8'
HANDLER = 'normalize'
AS
$$
def normalize(txt):
    return txt.lower().strip()
$$;
```

### UDF vs Stored Procedure

| Feature            | UDF                 | Stored Procedure              |
| ------------------ | ------------------- | ----------------------------- |
| Returns            | Single value        | Multiple values / result sets |
| DML allowed        | ❌ (SQL UDF)        | ✅                            |
| Called from SELECT | ✅                  | ❌                            |
| Control flow       | Limited             | Full                          |
| Best for           | Calculations, rules | ETL, workflows                |


## Snowflake Stored procedures <a id="storedprocedures"></a>

Snowflake Stored Procedures are used to execute procedural logic in Snowflake—things that go beyond a single SQL statement, such as loops, conditions, error handling, and multi-step workflows.

They run inside Snowflake’s cloud services layer, managed entirely by Snowflake.

Stored procedures (JavaScript or Python) execute in Snowflake’s Cloud Services layer. This compute is:
- Fully managed by Snowflake
- Serverless
- Not tied to your virtual warehouse

You do not pay warehouse credits for the procedural logic itself.

They are commonly used for ETL orchestration, data loading, auditing, and automation.

- Contains multiple SQL statements
- Supports control flow (IF, FOR, WHILE)
- Can execute DML and DDL
- Can return:
  - A single value, or
  - A table/result set
- Is written in: JavaScript, Python (Snowpark)
- Unlike UDFs, stored procedures cannot be used in SELECT statements.

Example:
```
CREATE OR REPLACE TABLE load_log (
    process_name STRING,
    status STRING,
    run_time TIMESTAMP
);

CREATE OR REPLACE PROCEDURE load_sales_data()
RETURNS STRING
LANGUAGE JAVASCRIPT
AS
$$
try {
    snowflake.execute({
        sqlText: `INSERT INTO sales_final
                  SELECT * FROM sales_stage`
    });
    snowflake.execute({
        sqlText: `INSERT INTO load_log
                  VALUES ('LOAD_SALES', 'SUCCESS', CURRENT_TIMESTAMP)`
    });
    return 'Load completed successfully';
} catch (err) {
    snowflake.execute({
        sqlText: `INSERT INTO load_log
                  VALUES ('LOAD_SALES', 'FAILED', CURRENT_TIMESTAMP)`
    });
    return 'Load failed: ' + err.message;
}
$$;

# call
CALL load_sales_data();
```

## Snowflake with Python and Spark <a id="spark"></a>

Snowflake integrates with Python and Spark in several well-defined ways.

### Option A: Snowflake Connector for Python

Used when Python runs outside Snowflake (laptop, server, Airflow, Databricks, etc.).

```
import snowflake.connector

conn = snowflake.connector.connect(
    user='USER',
    password='PASSWORD',
    account='ACCOUNT',
    warehouse='COMPUTE_WH',
    database='SALES_DB',
    schema='PUBLIC'
)

cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM SALES")
print(cur.fetchone())
```

### Option B: Snowpark Python (Python Runs Inside Snowflake)

Snowpark lets you write Python code that executes inside Snowflake.
- No Spark required
- Serverless execution
- Pushes computation to Snowflake

```
from snowflake.snowpark import Session

df = session.table("SALES")
result = df.group_by("REGION").sum("AMOUNT")
result.show()
```

## Security <a id="security"></a>

Snowflake (the platform) secures:
- Physical data centers
- Hardware, networking, OS
- Encryption mechanisms
- Infrastructure patching
- Availability and durability

Customer (you) secures:
- Users and roles (RBAC)
- Authentication & authorization
  - Username & Password
  - MFA
  - Single Sign-On (SSO), SAML 2.0 integration
  - Key Pair Authentication
- Data access policies
  - Encryption at Rest
  - Encryption in Transit
  - Row-Level Security (RLS)
  - Column-Level Security (CLS)
  - Secure Data Sharing
- Network controls (IP allowlists, PrivateLink)
  - Network Policies: IP allowlists / blocklists
  - Private Connectivity: AWS PrivateLink, Azure Private Endpoint
  - Internal Network Isolation: Customer workloads are isolated
- Data classification and governance
  - Object Tagging: Tag columns and tables with metadata (PII classification)
  - Access History: Tracks who accessed what data and when
  - Monitoring, Auditing & Logging: Account Usage Views, 
  - Data Recovery & Protection: Time Travel, Fail-safe

## Best practices <a id="bestpractices"></a>

Warehouse:
* set auto suspend (for ETL: immediately, SELECT queries: 10 min (use cache), DevOps/Data Science: 5 min)
* set auto resume
* set timeouts:
* set appropriate warehouse so you can process your queries

Table design:
* Staging table: transient (no need to time travel)
* Productive table: permanent
* Development tables: transient

Data types: use appropriete data types (timestamp, numbers etc.)

Set clusters only if necessary: large table, or query profile has lots of table scans

Monitor:
* usage of warehouse
* usage of storage

Retention period:
* staging tables or processing tables: do not need time travel
* production/curated tables: use time travel.
* large tables: expensive - maybe you do not need time travel

### Pricing

- fee for data storage
- fee for compute: function of warehouse size, number of clusters and time spent to execute queries

### Use snowsight UI web interface
- login to account
- create database
- create schema
- create table
- optional: create file format
- create stage
- import file to stage

### Use snowSQL client

https://sivachandanc.medium.com/ingesting-local-files-to-snowflake-table-using-snowsql-396301578fde

- Connect to snowflake
```
snowsql -a <account_name> -u <username>
```

- Create a Table
```
use WAREHOUSE ??? ;
use DATABASE ?? ;
use SCHEMA pulic ;
CREATE TABLE ... ;
```

- load data to to default User stage
```
put 'file:////home/sivachandan/Downloads/MOCK_DATA.csv' @~/staged;

list @~;
```

- load data from stage to table
```
copy into <table>> from @~/staged/MOCK_DATA.csv.gz ;
```

### load bulk data from azure

- load data into azure storage account

- CREATE STORAGE INTEGRATION

- Create Stage
```
CREATE STAGE azstage
URL = azure://<account>.blob.core.windows.net/<container>/<path>
CREDENTIALS=(AZURE_SAS_TOKEN=…)
```
- Copy data to table
```
COPY INTO <table>
FROM @azstage/newbatch
```


## Interview questions <a id="interviewquestions"></a>

### explain how showflake AWS PrivateLink works

Snowflake AWS PrivateLink allows you to connect to Snowflake privately over the AWS network, without exposing traffic to the public internet.

It uses AWS PrivateLink + VPC Endpoints so all communication stays within AWS’s backbone network.

Key Components
- Customer VPC (your AWS account)
- Interface VPC Endpoint (powered by AWS PrivateLink)
- Snowflake Service VPC
- Snowflake Virtual Warehouses

Step 1: Snowflake Creates a PrivateLink Service
- Snowflake exposes its service using a VPC Endpoint Service
- This service is backed by Network Load Balancers (NLBs)

Step 2: Customer Creates a VPC Interface Endpoint. In your AWS account:
- You create an Interface VPC Endpoint
- You select Snowflake’s endpoint service
- AWS creates Elastic Network Interfaces (ENIs) in your VPC subnets
- These ENIs have private IP addresses

More about VPC Endpoint:
- VPC endpoint is a virtual device that enables you to privately connect your Virtual Private Cloud (VPC) to supported AWS services without requiring an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection
- Creates an Elastic Network Interface (ENI) with a private IP address in your subnet.
- Supports access from on-premises networks via VPN/Direct Connect, peered VPCs, and Transit Gateway
- To connect to a VPC endpoint in another company's AWS account, you use AWS PrivateLink to establish a private, secure connection that does not traverse the public internet

### what is the difference between snowflake time travel and fail safe

Time Travel lets you access, query, and restore historical data that has changed or been deleted
- Query data as it existed at a point in time
- Recover accidentally deleted or updated data

Fail-safe is a disaster recovery mechanism of last resort. It allows Snowflake to __recover data after Time Travel has expired__.
- Recover data only through Snowflake Support
- Restore data lost due to:
  - Accidental drops after Time Travel window
  - System failures
  - Catastrophic events

### How to copy data from snowflake table to file on aws s3?

To copy data from a Snowflake table to a file in AWS S3, you can use the COPY INTO command

```
CREATE STAGE my_s3_stage
  URL = 's3://mybucket/snowflake-exports/'
  CREDENTIALS = (AWS_KEY_ID = '<AWS_ACCESS_KEY>' 
                 AWS_SECRET_KEY = '<AWS_SECRET_KEY>')
  FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '"');
```

If you have a large amount of data, you may want to partition the files by a specific column (e.g., by order_date or region). This will create subdirectories in the S3 bucket for each partition, making the data more manageable.

```
COPY INTO @my_s3_stage/my_data_file_
  FROM (SELECT id, name, email, order_date FROM my_table)
  FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '"')
  PARTITION_BY = (TO_CHAR(order_date, 'YYYY/MM/DD'))
  OVERWRITE = TRUE;
```

### What is SCD Type 1 or Type 2 or Type 3 etc.?

SCD stands for Slowly Changing Dimension — a set of techniques used in data warehousing to manage changes in dimension data over time.

#### SCD Type 1

SCD Type 1 (also called "Overwrite" or "Replace") is the simplest and most common way to handle changes in dimension data in a data warehouse.

- You simply overwrite the old value with the new value
- No history is preserved
- The dimension table always shows only the current state

#### SCD Type 2

SCD Type 2 (also called "Versioning" or "Add new row") is the most common Slowly Changing Dimension technique when you need to preserve history of changes in dimension attributes.

- You do NOT overwrite the existing row
- Instead, you add a completely new row with the updated values
- The old row is closed (marked as no longer current)
- Both old and new versions remain in the table → full history is preserved

Example:
| sk | customer_id | name       | email               | city       | valid_from          | valid_to            | is_current
|----|-------------|------------|---------------------|------------|---------------------|---------------------|-----------
| 1  | 1001        | Alice Chen | alice@gmail.com     | Piscataway | 2023-05-12 00:00:00 | 2025-06-15 00:00:00 | FALSE
| 2  | 1001        | Alice Chen | alice.new@proton.me | Piscataway | 2025-06-15 00:00:00 | 9999-12-31 23:59:59 | TRUE

- surrogate_key (sk): Unique identifier for each version1, 2, 3, ... (auto-increment or sequence)
- business_key (customer_id): Natural key from source system
- attributes: The actual dimension columns: name, email, city, department, etc
- valid_from: When this version became valid 
- valid_to: When this version stopped being valid
- is_current: Quick flag: is this the active version?

#### SCD Type 3

SCD Type 3 (Slowly Changing Dimension Type 3) is a method used in data warehousing to track limited history of changes to dimension attributes — typically just the current value and the immediately previous value

Type 3 adds extra columns to the same row to store the historical value(s). This keeps the dimension table compact.

| CustomerID | CustomerName | Current_City | Previous_City | Current_State | Previous_State
|------------|--------------|--------------|---------------|---------------|------------------
| 1001       | Alice        | Seattle      | Portland      | WA            | OR
| 1002       | Bob          | Austin       | NULL          | TX            | NULL

Use it when:
- Attribute changes very rarely (1–2 times in the lifetime of the record)
- You only need the most recent change (or original value) for reporting
- You want to avoid row explosion / table growth (Type 2 problem)

#### SCD Type 4

##### Kimball's Original / Official Type 4: Mini-Dimension

Ralph Kimball (in The Data Warehouse Toolkit) defines Type 4 as splitting rapidly or frequently changing attributes out of a large "monster" dimension into a separate mini-dimension table.

- Main dimension table → contains stable / slowly changing attributes + current value of the volatile ones (often updated as Type 1 = overwrite)
- Mini-dimension table → contains the frequently changing attributes + a surrogate key; new row added for each meaningful change (Type 2 style)
- Fact table → gets two foreign keys:
  - One to the main dimension (stable part)
  - One to the mini-dimension (captures the "as-of" profile at the time of the fact)

Advantages: History of volatile attributes preserved without exploding the main table

### How does Snowflake handle concurrency?

Snowflake handles concurrency by using separate virtual warehouses for compute, multi-cluster warehouses for scaling, and shared cloud storage—allowing many users and queries to run simultaneously without contention.

Separation of Storage and Compute:
- All data is stored once in centralized cloud storage
- Each virtual warehouse provides independent compute
- Multiple warehouses can access the same data simultaneously

Virtual Warehouses = Isolation
- Each warehouse:
  - Has its own CPU, memory, and cache
  - Runs queries independently
- If one query is slow or heavy, it does not impact others

Multi-Cluster Warehouses (Key for High Concurrency)
- When many queries hit the same warehouse:
  - Snowflake automatically starts additional clusters
  - Queries are distributed across clusters
  - Clusters scale up and down automatically
- Without Multi-Cluster
  - Queries queue
  - Users experience delays

No Locks on Reads
- Snowflake uses MVCC (Multi-Version Concurrency Control)
- Readers don’t block writers
- Writers don’t block readers

### Explain the Cloud Services layer.

The Cloud Services layer manages metadata, authentication, query optimization, transactions, and orchestration in Snowflake. It does not store data or run user compute-heavy queries.

### How big is a micro-partition?

A micro-partition is typically 50 MB to 500 MB of compressed data, with an average around 100–200 MB.

### What metadata does Snowflake store?

Snowflake stores metadata about objects, micro-partitions, files, security, and query execution to enable automatic optimization, pruning, governance, and concurrency.

### What is pruning in Snowflake?

Pruning in Snowflake means eliminating micro-partitions from a query scan using metadata (like min/max column values), so only relevant data is read.

How Pruning Works:
- Data Stored in Micro-Partitions
  - Tables are stored as immutable micro-partitions
  - Each micro-partition contains metadata per column: Min value, Max value, Null count, Distinct count
- Query Predicate Evaluation
  - Snowflake Looks at micro-partition metadata
  - Identifies partitions where: min_date <= '2025-01-01', max_date >= '2025-01-01'
  - Skips all other partitions

### How does Snowflake handle indexing?

Snowflake handles indexing automatically using micro-partition metadata, pruning, and optional search optimization instead of traditional indexes.

### What happens when a warehouse is suspended?

- Compute resources are shut down — Snowflake immediately releases all idle compute nodes/clusters. This stops further credit consumption for that warehouse.
- Running queries are not aborted — Any statements (queries, loads, etc.) that were actively executing at the moment of suspension are allowed to complete normally. The warehouse doesn't kill them.
- No new queries can run
- Credit consumption stops
- Result cache / local disk cache is dropped

### How does Snowflake ensure high availability?

Snowflake provides a 99.9% monthly uptime SLA

- Centralized storage layer — All data is durably stored in cloud object storage (e.g., S3, Azure Blob, GCS) in micro-partitions. This storage is highly durable (typically 11–12 9s durability from the underlying cloud provider) and independently scalable from compute.
- Independent compute clusters (virtual warehouses) — Each warehouse is an isolated MPP (massively parallel processing) cluster. Failure in one warehouse doesn't affect others.
- Cloud services layer — Metadata, authentication, query optimization, and coordination are managed in a highly available, distributed manner.
- Snowgrid — Snowflake's internal global network layer enables consistent behavior, security, and connectivity across regions and clouds, supporting cross-region/cross-cloud operations.

### What are stages in Snowflake?

Stages in Snowflake are named objects (or implicit locations) that serve as intermediate storage areas for data files. They are primarily used for bulk loading data from files into Snowflake tables (via COPY INTO <table>) and unloading data from tables to files (via COPY INTO <location>).

Stages act as a bridge between external sources (like your local machine or cloud storage) and Snowflake tables, enabling efficient, parallel data ingestion/unloading without direct table access during staging.

Snowflake supports two main categories of stages: internal (managed by Snowflake) and external (referencing cloud storage outside Snowflake).

Common Commands for Working with Stages:
- CREATE STAGE — Create named stages (internal or external).
- PUT — Upload local files to internal stages (from SnowSQL, drivers, etc.).
- GET — Download files from internal stages to local.
- LIST @stage_name — List files in a stage.
- COPY INTO my_table FROM @stage_name ... — Load data.
- COPY INTO @stage_name FROM my_table ... — Unload data.
- REMOVE @stage_name ... — Delete files from stage.
- DESCRIBE STAGE my_stage — View properties.
- DROP STAGE my_stage — Remove named stages

### How does Snowpipe work internally?

Snowpipe is Snowflake's serverless, continuous data ingestion service for loading files from a stage (internal or external) into tables automatically and near real-time. It operates in micro-batches rather than large scheduled bulk loads.
There are two main ingestion paths:

Auto-ingest (most common): Event-driven via cloud storage notifications.
REST API triggered: Client applications explicitly notify Snowpipe of files.

Snowpipe differs from classic COPY INTO bulk loads because it uses Snowflake-managed serverless compute (no virtual warehouse required), is triggered automatically or via API, and loads in smaller increments.

Core Internal Components
- Pipe object — A first-class Snowflake object created with CREATE PIPE. It embeds a fixed COPY INTO <table> statement (including stage, file format, transformations via SELECT, ON_ERROR behavior, etc.). This COPY definition is reused for every load triggered by the pipe.
- Ingestion queue — An internal Snowflake-managed queue (per pipe) that holds pending file load requests. Files are appended as they are detected/ notified.
- File loading metadata — Stored in the pipe object's metadata (not the table). Tracks path + filename (and internally eTag/checksum) of successfully loaded files. Prevents duplicates: same filename is never reloaded, even if file content changes later. This history is retained for 14 days (after which modified files could reload and cause duplicates).
- Serverless compute layer — Snowflake provisions and scales ephemeral compute resources automatically to execute the pipe's COPY statement on queued files. Billing is per-second for actual compute used + per-file notification fees.

### What is schema-on-read?

Schema-on-read in Snowflake means that data is stored without enforcing a rigid schema upfront, and the structure is applied only when the data is queried (read)—not when it’s loaded.

This approach is especially useful for semi-structured data like JSON, Avro, Parquet, or XML.

- Data is ingested as-is into Snowflake (often into a __VARIANT__ column).
- Snowflake does not require a predefined table schema for the internal fields of the data.

```
CREATE TABLE raw_events (
    event_data VARIANT
);
```

Interpret the schema at query time:
```
SELECT
    event_data:user_id::STRING AS user_id,
    event_data:event_time::TIMESTAMP AS event_time
FROM raw_events;
```

Trade-offs:
- slower queries
- Less optimization

### How do you load semi-structured data?

In Snowflake, semi-structured data (JSON, Avro, Parquet, ORC, XML) is typically loaded using stages + COPY INTO, with the data stored in a VARIANT column. Here’s the standard, end-to-end approach.

### What is VARIANT data type?

In Snowflake, the VARIANT data type is a flexible, semi-structured data type used to store data whose structure is not fixed or known upfront—such as JSON, Avro, Parquet, ORC, or XML.

It is the foundation for schema-on-read in Snowflake.

### Difference between internal and external stages?

Internal stages: Internal stages store data inside Snowflake-managed storage.

Types of internal stages
- User stage – @~
- Table stage – @%table_name
- Named internal stage

External stages reference data stored in external cloud storage.

Supported storage
- Amazon S3
- Azure Blob Storage
- Google Cloud Storage

### How do you unload data from Snowflake?

In Snowflake, you unload (export) data using the COPY INTO <stage> command. This writes query results from Snowflake tables into files in an internal or external stage.

```
COPY INTO @stage_name/path/
FROM <query_or_table>
FILE_FORMAT = (TYPE = CSV);
```

### How does Snowflake handle duplicate data?

Snowflake does not automatically prevent or remove duplicate data. 
How duplicates are handled depends on how you load, query, and design your pipelines. Snowflake gives you tools—but you control deduplication logic.

File-level deduplication (default behavior)
- When loading from stages, Snowflake tracks file metadata (file name + checksum).
- A file is loaded only once by default
- Reloading the same file is skipped automatically

Snowflake does not deduplicate rows automatically.

### How do you validate loaded data?

1. Validate During the Load (Pre- & In-Load Checks):
```
# check file structure and errors without inserting data
COPY INTO target_table
FROM @my_stage
FILE_FORMAT = (TYPE = CSV)
VALIDATION_MODE = RETURN_ERRORS;
```

2. Load into a Staging Table First (Best Practice)

3. Validate Load Success: 

Every COPY INTO returns a result set
```
SELECT *
FROM TABLE(RESULT_SCAN(LAST_QUERY_ID()));
```

Validate with LOAD_HISTORY: Use Snowflake metadata views:
```
SELECT *
FROM INFORMATION_SCHEMA.LOAD_HISTORY
WHERE TABLE_NAME = 'TARGET_TABLE'
ORDER BY LAST_LOAD_TIME DESC;
```

4. Data Quality Validation (Post-Load)
```
# Row Count Validation
SELECT COUNT(*) FROM target_table;

# NULL & Mandatory Field Checks
SELECT COUNT(*) 
FROM target_table
WHERE customer_id IS NULL;

# Data Type & Range Checks
SELECT *
FROM target_table
WHERE order_amount < 0
   OR order_amount > 100000;
```

5. Data Quality Frameworks
- dbt tests
- Great Expectations
- Soda
- Monte Carlo (observability)

### How does Snowflake optimize joins?

Snowflake optimizes joins using a combination of metadata, micro-partition pruning, cost-based optimization, and distributed execution. 
Unlike traditional databases, it does not use indexes—everything is optimized automatically.

1. When you run a query with joins, Snowflake’s cost-based optimizer decides:
- Join order (which table joins first)
- Join method (broadcast vs distributed)
- Which predicates to push down
- How many micro-partitions to scan
- How much parallelism to use

2. Micro-Partition Pruning (Biggest Performance Factor)
Tables are stored in immutable micro-partitions (~50–500 MB compressed)

Each micro-partition stores metadata:
- Min/max values per column
- NULL counts
- Row counts

3. Join Order Optimization. Snowflake automatically:
- Joins smaller / filtered tables first
- Pushes filters before joins when possible

4. Join Distribution Strategy. Snowflake chooses between two main join strategies:
- Broadcast Join (Replicated Join): One table is small can can be repliacted to all nodes
- Distributed (Shuffle) Join: Both tables are large: Rows are repartitioned (hashed) on join keys, Matching keys land on same nodes

5. Predicate Pushdown:
- Snowflake pushes filters as close to the scan as possible.

...

### What EXPLAIN Is Good For?

EXPLAIN shows the logical execution plan Snowflake intends to use for a query.

Verify Join Order & Join Type
- Broadcast vs distributed joins
- Whether small tables are joined first

Confirm Predicate Pushdown
- Check if filters are applied:
- Before joins (good)
- After joins (bad)

Detect Obvious Problems
- Cartesian joins
- Unnecessary subqueries
- Missing join conditions

### What is query profile?

The Query Profile is a full runtime breakdown of an executed query.

After running the query:
- Open Query Profile in the Snowflake UI.
- Query Profile shows:
  - Actual execution steps
  - Data scanned per step
  - Join strategy used
  - Partition pruning %
  - Time spent per operator

This is where real performance tuning happens.

See https://www.chaosgenius.io/blog/snowflake-query-optimization-query-profile/

### How do you troubleshoot slow queries?

- Confirm the Problem (Baseline First)
  - Is the query consistently slow, or just once?
  - Did it run fast before?
  - Did data volume change?
- Open Query Profile
  - Nodes with highest execution time
  - Operators scanning the most data
  - Join operators (broadcast vs shuffle)
  - Any spill to local storage
- Diagnose Common Root Causes
  - Too Much Data Scanned: Table Scan node dominates time: Add selective filters
  - Inefficient Joins: Large shuffle joins, High network transfer: Filter dimension tables first, Reduce join cardinality
- Poor Partition Pruning: % Partitions Scanned close to 100%
- Data Skew: One node much slower than others: Break query into steps, Pre-aggregate skewed data
- Warehouse Too Small: CPU-bound operators, Spills to local storage
- Concurrency Issues: Query waits in queue

### What is clustering key?

A clustering key tells Snowflake how rows should be ordered across micro-partitions based on one or more columns.
- Snowflake stores data in micro-partitions
- Each micro-partition has min/max metadata per column
- Clustering improves how well this metadata aligns with query filters

Without clustering:
- Data is written in load order
- Filters may scan many micro-partitions

Clustering works best for:
- Dates / timestamps
- Status codes
- Low-to-medium cardinality columns
- Range filters (BETWEEN, >=, <=)

### Difference between clustering and partitioning?

Partitioning is when you explicitly divide a table into separate physical chunks based on a column.
Snowflake does partition data internally, but users don’t manage it.

Clustering organizes data within Snowflake’s micro-partitions to improve pruning.

### What is SEARCH OPTIMIZATION?

Search Optimization (SO) creates a specialized search access path that allows Snowflake to quickly find specific rows without scanning large portions of a table.

Clustering struggles when:
- Queries look up single values
- Columns have very high cardinality
- Predicates use = , IN, or LIKE

__If many micro-partitions have overlapping min/max ranges, Snowflake must scan all of them.__

__customer_id Is a Bad Clustering Key because High-cardinality problem__

Example:
```
Partition 1: C000000001 → C999999999
Partition 2: C000000010 → C999999990
Partition 3: C000000005 → C999999995
```

Search Optimization solves this.

When enabled:
- Snowflake builds search metadata for specified columns
- Metadata maps values → micro-partitions
- At query time:
  - Snowflake directly locates relevant partitions
  - Skips scanning unrelated data

### What is the QUALIFY clause?

The QUALIFY clause is a filtering mechanism applied after window functions. It allows you to filter rows based on the result of window functions without using subqueries or CTEs.

```
SELECT column1, column2,
       ROW_NUMBER() OVER (PARTITION BY column1 ORDER BY column2 DESC) AS rn
FROM table_name
QUALIFY rn = 1;
```
- ROW_NUMBER() is a window function
- QUALIFY rn = 1 keeps only the first row per partition


### How does Snowflake handle large joins?

Snowflake handles large joins using a combination of distributed architecture, micro-partitions, query optimization, and adaptive execution strategies.

#### Broadcast Join

The smaller table is replicated across all nodes.

Each node joins the small table with its portion of the large table.

Works well when one table is much smaller than the other.

#### Shuffle / Partitioned Join

Both tables are redistributed across nodes based on join keys.

Required if both tables are large.

Ensures matching keys end up on the same node.

May involve heavy network transfer (the main bottleneck for large joins).

#### Merge Join

Snowflake can use sort-merge joins if tables are already sorted or clustered.

Efficient for range joins or pre-ordered datasets.

Avoids full redistribution.

### How do you reduce query cost?

Reducing query cost in Snowflake is mostly about __reducing the amount of data scanned__ and __optimizing compute usage__, because Snowflake charges based on compute time

Reduce Data Scanned:
- Filter Early: 
  - WHERE clauses to scan fewer micro-partitions
  - Avoid functions on columns in filters
- Use Clustering Keys: Cluster large tables on frequently filtered columns
- Use Search Optimization
- Avoid SELECT *

Optimize Compute Usage:
- Right-Size Your Warehouse: Scale up temporarily for big queries, then scale down
- Suspend Idle Warehouses
- multi-cluster warehouses instead of constantly scaling up

Use Caching:
| Cache Type       | Benefit                                              |
| ---------------- | ---------------------------------------------------- |
| Result Cache     | Query runs instantly if identical query ran recently |
| Local Disk Cache | Data reused if warehouse recently queried same table |
| Remote Cache     | Reduces S3 reads across warehouses                   |

Materialize Expensive Operations

Monitor Query Cost

### What is automatic query optimization?

Automatic Query Optimization is a set of built-in, behind-the-scenes techniques that Snowflake’s query engine uses to make queries run faster and more efficiently without requiring manual tuning.

When you submit a query, Snowflake’s engine:
- Analyzes the SQL statement
- Estimates table sizes, micro-partition metadata, and data distribution
- Chooses optimal execution strategies including:
  - Join order and join type
  - Partition pruning
  - Broadcast vs shuffle
  - Use of caching
- Rewrites queries internally if it improves performance

All of this happens automatically

### pros and cons for snowflake variant fields

Example:
```
CREATE TABLE events (
  id STRING,
  payload VARIANT
);

// example row
{
  "user_id": 123,
  "device": "iphone",
  "cart": {
    "items": 3
  }
}

// query:
SELECT
  payload:user_id,
  payload:cart.items
FROM events;
```

Pros:
- Flexible schema evolution: You can ingest changing JSON without constantly altering tables
  ```
  // day 1
  {"a":1}
  // day 2
  {"a":1,"b":2,"c":{"d":3}}
  ```
- Faster ingestion pipelines
- JSON query support
  ```
  SELECT
    payload:user.id::STRING,
    payload:items[0].price::NUMBER
  FROM orders;
  ```
- Good compression

Cons:
- Worse query performance
- Poor pruning and clustering
- SQL becomes ugly

### How to you process new data inserts into snowflake tables

1. Streams → detect row-level changes
```
// Raw ingestion table
CREATE TABLE raw_events (
  payload VARIANT,
  ingest_ts TIMESTAMP
);

// create stream
CREATE STREAM raw_events_stream
ON TABLE raw_events;

// curated table
CREATE TABLE curated_events (
  user_id NUMBER,
  event_type STRING,
  event_ts TIMESTAMP
);

// processing task
CREATE TASK process_events
WAREHOUSE = transform_wh
WHEN SYSTEM$STREAM_HAS_DATA('raw_events_stream')
AS
INSERT INTO curated_events
SELECT
  payload:user_id::NUMBER,
  payload:event_type::STRING,
  payload:event_ts::TIMESTAMP
FROM raw_events_stream;
```
2. Tasks → schedule SQL execution
3. Dynamic Tables → incremental materialization
4. Snowpipe / Streaming → ingest new data
```
MERGE INTO customers tgt
USING customers_stream src
ON tgt.customer_id = src.customer_id
WHEN MATCHED THEN
  UPDATE SET name = src.name
WHEN NOT MATCHED THEN
  INSERT (customer_id, name)
  VALUES (src.customer_id, src.name);
```

### how snowflake handles transactions

Snowflake uses a fully ACID transactional model with MVCC (Multi-Version Concurrency Control),

Snowflake separates compute from storage and uses immutable micro-partitions + metadata versioning to implement transactions efficiently.

Multi-Version Concurrency Control (MVCC). Instead of modifying data in place:
- Snowflake creates new versions of data
- readers see consistent snapshots
- writers don’t block readers

### how to handle schema changes in snowflake?

The biggest mistake teams make is either:
- enforcing rigid schemas too early OR
- letting uncontrolled JSON spread everywhere

```
Source Systems
      ↓
Raw/Bronze (flexible schema)
      ↓
Normalization / CDC handling
      ↓
Curated/Silver (stable schema)
      ↓
Business/Gold models
```

### Snowflake - kafka connector: how does it work?

Use Snowpipe Streaming: Kafka → Connector → Snowpipe Streaming API → Snowflake table
- Raw VARIANT table
- Ingestion into Snowflake: 

### how to govern Snowflake at enterprise scale

1. Security & Access Control
2. Data Organization & Architecture
  - medallion
  - domain based ownership
3. Data Quality & Lineage
  - dbt
  - etc
  - lineage
4. Cost & Resource Governance
5. Operational Governance (process + tooling)

### How do Streams work internally?

### Difference between Tasks and cron jobs?
### 
### What is serverless task?
### 
### ow does Snowflake handle security?
### 
### What is role-based access control (RBAC)?
### 
### Difference between SYSADMIN and SECURITYADMIN?
### 
### What is ACCOUNTADMIN?
### 
### How does Snowflake encrypt data?
### 
### Snowflake Security
### 
### How does Snowflake support compliance (HIPAA, GDPR)?
### 
### Difference between Snowpark and Spark?
### 
### How does Snowflake integrate with BI tools?
### 
### How do you optimize Snowflake cost?
### 
### How do you monitor credit usage?
### 
### How do you design a Snowflake ETL pipeline?
### 
### How do you handle incremental loads?
### 
### How do you migrate data from on-prem to Snowflake?
### 
### How do you design Snowflake for high concurrency?
### 
### What are common Snowflake performance issues?