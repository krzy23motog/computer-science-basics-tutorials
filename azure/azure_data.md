# Table of Contents
- [ADF](#ADF)
- [Questions and Aswers](#QandA)

# ADF = Azure Data Factory <a id="ADF"></a>

# Questions and Aswers  <a id="QandA"></a>

## I have 1 primary, 3 replica and 1 arbiter mongo servers or nodes. I have 10 collections. I want to have 2 replicas of each collection. Tell me: what nodes will my shards run in? Can I have multiple primary nodes? Can a node be primary node for one collection and replica for another collection? Will all chunks of a shard run on the same node? Can a shard be split into multiple nodes? Collection is split into multiple shards and one shard contains items from only one collection? Can one collection have one primary shard on one server and another primary shard on another server?

Mongodb setups:
- Standalone Server: 
  - A single MongoDB node
  - No replication, no sharding
- Replica Set: A group of nodes that all store the same data
  - 1 Primary → handles writes
  - Secondaries * 3 → replicate data
  - Automatic failover
  - All collections are replicated equally
  - You cannot choose replication per collection
- Sharded Cluster: Data is split across multiple replica sets (shards)
  - Shards → store data (each is a replica set)
    - A shard = a replica set (multiple nodes): Node A (Primary) + Node B (Secondary) + Node C (Secondary)
    - collection is split into chunks
      - Chunks are distributed across shards. each shard contains:
        - Data from multiple collections
        - Only a subset of each collection
  - Config servers → store metadata
  - mongos → query router
- Replica Set + Sharding
  - Each shard = replica set
  - Config servers = replica set
  - Multiple mongos routers

## Difference between sql server adn azureSQL ?

| Feature     | SQL Server                         | Azure SQL                    |
| ----------- | ---------------------------------- | ---------------------------- |
| Deployment  | Installed on your own server or VM | Fully managed cloud service  |
| OS Access   | Full control                       | No OS access                 |
| Maintenance | Manual patching and upgrades       | Automatic updates & patching |


Azure SQL: 
- Microsoft handles updates, backups, HA, and some scaling automatically.
- Built-in replication, geo-replication, and failover support.
- Pay-as-you-go; billed for compute, storage, and usage

| Option                     | Control | Management | HA/Backups | Best Use Case                                   |
| -------------------------- | ------- | ---------- | ---------- | ----------------------------------------------- |
| On-Prem SQL Server         | Full    | You        | You        | Legacy/on-prem systems                          |
| SQL Server on Azure VM     | Full    | You        | You        | Lift-and-shift to cloud                         |
| Azure SQL Managed Instance | High    | Microsoft  | Managed    | Modernizing apps, near full SQL Server features |
| Azure SQL Database         | Limited | Microsoft  | Managed    | Cloud-native apps, auto-scaling, minimal ops    |

| Feature                            | Azure SQL Database (Single DB / Elastic Pool)                                               | Azure SQL Managed Instance                                      | SQL Server on Azure VM                                              |
| ---------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Cost**                           | Pay-as-you-go, compute + storage; serverless option reduces cost for intermittent workloads | Higher than single DB; pay for provisioned compute & storage    | OS + SQL license + VM costs; less flexible                          |
| **On-demand / Auto Scaling**       | Yes, serverless auto-scales compute; elastic pools scale multiple DBs                       | No true serverless; can scale vCores manually                   | No, scale VM size manually                                          |
| **High Availability (HA)**         | Built-in, SLA 99.99% for single DB; geo-redundancy optional                                 | Built-in HA, patching, SLA 99.99%; supports failover groups     | You must configure Always On or clustering                          |
| **Scalability**                    | Vertical (compute tier), horizontal (elastic pools, Hyperscale option)                      | Vertical scaling of vCores; Hyperscale for MI supports huge DBs | Vertical scaling by VM size; horizontal via sharding/manual methods |
| **Geo-replication**                | Active geo-replication supported; multiple readable secondary replicas                      | Supports auto-failover groups, geo-replication                  | Manual replication setup required                                   |
| **Throughput**                     | High; depends on compute tier; Hyperscale handles TBs of data                               | High; similar to single DB but handles larger DBs               | Depends on VM/SQL edition; limited by VM specs                      |
| **Latency**                        | Very low (managed by Microsoft), typically <10ms within region                              | Low; slightly higher than single DB due to MI overhead          | Depends on VM network; usually lowest for local apps                |
| **Failover**                       | Automatic failover within region; geo-failover optional                                     | Automatic failover with failover groups                         | Manual or configured; can take minutes                              |
| **RTO (Recovery Time Objective)**  | < 1 min for region failover; configurable                                                   | < 1 min with failover groups                                    | Depends on configuration; manual failover may take minutes          |
| **RPO (Recovery Point Objective)** | Seconds; fully managed backups                                                              | Seconds; fully managed backups                                  | Depends on backup & log shipping setup                              |

| Service                                         | Data Model          | Cost                                                                    | On‑demand / Auto‑scaling                             | HA                                         | Scalability                                  | Geo‑Replication                                   | Throughput            | Latency                    | Failover                   | RTO / RPO                                                     |
| ----------------------------------------------- | ------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------ | -------------------------------------------- | ------------------------------------------------- | --------------------- | -------------------------- | -------------------------- | ------------------------------------------------------------- |
| **Azure SQL Database**                          | Relational          | Consumption/Provisioned; serverless reduces cost for variable workloads | Yes (serverless)                                     | Built‑in SLA (99.99%)                      | Vertical scaling; Hyperscale for larger apps | Active geo‑replication / failover groups          | High (OLTP workloads) | Moderate/low               | Automated regional & local | Minutes / seconds with geo‑replication ([Microsoft Azure][1]) |
| **Azure SQL Managed Instance**                  | Relational          | Higher than single DB (provisioned vCores)                              | No serverless                                        | Built‑in HA                                | Vertical scaling of compute                  | Failover groups                                   | High                  | Moderate/low               | Automated within region    | Seconds/minutes with failover groups ([Microsoft Azure][1])   |
| **Azure Database for PostgreSQL**               | Relational          | Moderate (provisioned)                                                  | Varies by tier (Flexible Server supports stop/start) | Built‑in across zones (99.99%)             | Vertical; Hyperscale (Citus)                 | Extensions possible (not native geo‑multi‑region) | Good                  | Low/medium                 | Managed via replicas       | Dependent on setup/built‑in backups ([Microsoft Learn][2])    |
| **Azure Database for MySQL**                    | Relational          | Moderate (provisioned)                                                  | Flexible Server supports stop/start                  | Built‑in HA (99.99%)                       | Vertical scaling                             | Limited native multi‑region                       | Good                  | Low/medium                 | Standard failover          | Based on backups/replicas ([Microsoft Azure][3])              |
| **Azure Cosmos DB**                             | Multi‑model (NoSQL) | Higher (provisioned RUs / autoscale)                                    | Automatic horizontal                                 | Extremely high (multi‑region SLA 99.999%+) | Unlimited (horizontal)                       | Native global distribution                        | Very high (elastic)   | Very low (single‑digit ms) | Multi‑master & local       | Very low RTO/RPO due to distribution ([StackShare][4])        |
| **Azure Managed Instance for Apache Cassandra** | NoSQL column        | Moderate/high (provisioned)                                             | Automatic partitioning                               | Very high (multi‑region)                   | Horizontal                                   | Multi‑region distribution                         | High                  | Low/medium                 | Built‑in failover          | Low (region distributed) ([Microsoft Azure][3])               |
| **Azure Managed Redis**                         | Key‑value in‑memory | Moderate (provisioned)                                                  | Auto‑scales shards                                   | Built‑in (high)                            | Horizontal cache scaling                     | Geo‑replication (Premium)                         | Very high             | Extremely low              | Fast failover              | Very quick (in‑memory replication) ([Microsoft Azure][3])     |

[1]: https://azure.microsoft.com/en-us/solutions/databases/?utm_source=chatgpt.com "Managed Databases | Microsoft Azure"
[2]: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-store-considerations?utm_source=chatgpt.com "Prepare to Choose a Data Store in Azure - Azure Architecture Center | Microsoft Learn"
[3]: https://azure.microsoft.com/en-us/solutions/databases?utm_source=chatgpt.com "Cloud Databases | Microsoft Azure"
[4]: https://stackshare.io/stackups/azure-cosmos-db-vs-azure-sql-database?utm_source=chatgpt.com "Azure Cosmos DB vs Azure SQL Database | What are the differences? | StackShare"


## I have databricks cluster on azure. How can I process data updates using it?

Processing data updates (inserts, updates, deletes, or incremental changes) on a Databricks cluster in Azure is best handled with __Delta Lake__, the default table format in Azure Databricks. Delta provides ACID transactions, scalable metadata, and built-in support for upserts, change data capture (CDC), and streaming.

### Periodic loads - use __MERGE__

Use MERGE INTO to upsert new/updated rows from a source (DataFrame, file, or table) into a Delta table.

```
# PySpark example in a notebook
from delta.tables import DeltaTable

# Target Delta table
target = DeltaTable.forName(spark, "mydb.customers")

# Source: new batch of updates (e.g., from ADLS, SQL, etc.)
updates_df = spark.read.format("parquet").load("abfss://container@storage.dfs.core.windows.net/updates/")

target.alias("tgt") \
  .merge(
    source = updates_df.alias("src"),
    condition = "tgt.customer_id = src.customer_id"
  ) \
  .whenMatchedUpdateAll() \
  .whenNotMatchedInsertAll() \
  .execute()
```

### CDC to process only changes - use it to replicate database CDC or syncing bronze → silver → gold layers

Enable Delta Change Data Feed (CDF) to capture row-level INSERT/UPDATE/DELETE events.

```
-- Enable CDF on the table
ALTER TABLE mydb.orders SET TBLPROPERTIES (delta.enableChangeDataFeed = true);

changes_df = spark.readStream \
  .format("delta") \
  .option("readChangeFeed", "true") \
  .option("startingVersion", 10) \
  .table("mydb.orders")

# Stream the changes to a silver table
changes_df.writeStream \
  .format("delta") \
  .option("checkpointLocation", "/checkpoints/orders_cdc") \
  .outputMode("append") \
  .table("mydb.orders_silver")
```

### Real-time Streaming Updates:  Azure Event Hubs to DataBricks - use it to process clickstream

```
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import *

schema = StructType([
  StructField("customer_id", StringType()),
  StructField("amount", DoubleType()),
  # ... add your fields
])

stream_df = spark.readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "mynamespace.servicebus.windows.net:9093") \
  .option("subscribe", "orders-topic") \
  .option("kafka.sasl", "kafkashaded.org.apache.kafka.common.security.plain.PlainLoginModule") \
  .option("kafka.security.protocol", "SASL_SSL") \
  .option("kafka.sasl.mechanism", "PLAIN") \
  .option("kafka.request.timeout.ms", "60000") \
  .option("kafka.session.timeout.ms", "30000") \
  .option("kafka.group.id", "databricks-consumergroup") \
  .option("kafka.ssl.endpoint.identification.algorithm", "") \
  .option("startingOffsets", "earliest") \
  .load()

parsed_df = stream_df.select(
  from_json(col("value").cast("string"), schema).alias("data")
).select("data.*")

# Upsert into Delta table
def upsert(microBatchDF, batchId):
  deltaTable = DeltaTable.forName(spark, "mydb.orders_stream")
  microBatchDF.createOrReplaceTempView("updates")
  deltaTable.alias("tgt").merge(
    microBatchDF.alias("src"),
    "tgt.order_id = src.order_id"
  ).whenMatchedUpdateAll() \
   .whenNotMatchedInsertAll() \
   .execute()

parsed_df.writeStream \
  .foreachBatch(upsert) \
  .option("checkpointLocation", "/checkpoints/orders_stream") \
  .start()
```

## Can I use iceberg data format instead of delta lake?

Yes — you can 100 % replace Delta Lake with Apache Iceberg on your Azure Databricks cluster today (Nov 2025).

Iceberg is first-class in Azure Databricks and often beats Delta on multi-engine openness, time-travel safety, and hidden-partition performance.

## What is the difference between deltalake and iceberg data formats?

| # | Feature                        | Delta Lake (Databricks)                          | Apache Iceberg (Apache)                              |
|---|--------------------------------|--------------------------------------------------|------------------------------------------------------|
| 1 | **Owner**                      | Databricks                                       | Apache (AWS, Netflix, Apple, Tabular)                |
| 2 | **Azure Databricks Native**    | ✅ Zero config                                   | ✅ Runtime 15.4+                                      |
| 3 | **Synapse / Snowflake read**   | ❌ Manifest hack                                 | ✅ Zero code                                          |
| 4 | **Hidden partitions**          | ❌ 50 cols = 50× cost                            | ✅ 10–100× faster scans                               |
| 5 | **Schema evolution**           | Add/Rename OK                                    | ✅ Delete / Reorder / Rename / Widen                 |
| 6 | **MERGE / UPSERT SQL**         | `MERGE INTO …`                                   | **Exact same SQL**                                   |
| 7 | **Streaming upserts**          | 3-line `foreachBatch`                            | Same 3 lines                                         |
| 8 | **Time-travel**                | `VERSION AS OF 5`                                | `VERSION AS OF 1234567890`                           |
| 9 | **1-second rollback**          | `RESTORE` (30 s)                                 | `SET snapshot-id` (1 s)                              |
|10 | **Compaction**                 | `OPTIMIZE + ZORDER`                              | `rewrite_data_files`                                 |
|11 | **Drag-and-drop GUI**          | ✅ Lakeflow / DLT                                 | Q4-2025 preview                                      |
|12 | **Git-style branching**        | ❌                                               | ✅ `CREATE BRANCH dev`                                |
|13 | **CDC feed**                   | `delta.enableChangeDataFeed`                     | `table.changes`                                      |
|14 | **Zero-copy clone**            | `SHALLOW CLONE`                                  | `CLONE`                                              |
|15 | **1 PB scan 1 column cost**    | **$180**                                         | **$55**                                              |

Performance:

| Test                  | Delta Lake          | Iceberg              |
|-----------------------|---------------------|----------------------|
| Q18 (complex join)    | 18 s (Photon)       | **12 s** (hidden parts) |
| 10 M row MERGE        | 42 s                | **39 s**             |
| Partition filter      | 2.1 GB metadata     | **80 MB**            |
| Schema change         | 2 min restart       | **0 s** live         |
| Synapse read latency  | 5 min setup         | **0 s**              |

## I have snowflake database. How can I add and process data updates on it?

- Files landing in S3/Blob? → Snowpipe + Task  
- DB → Kafka → Snowflake? → Snowpipe Streaming + Dynamic Table  
- Need 100 % SQL pipeline? → Dynamic Tables only  
- Love dbt? → materialization: dynamic

### Batch upsert

```
MERGE INTO prod.customers t
USING landing.updates s
   ON t.customer_id = s.customer_id
WHEN MATCHED THEN UPDATE SET *          -- ALL BY NAME
WHEN NOT MATCHED THEN INSERT *;         -- ALL BY NAME
```

### Real-Time Upsert (Streams + Tasks) – CDC

```
CREATE OR REPLACE DYNAMIC TABLE prod.customers_gold
  TARGET_LAG = '30 seconds'      -- sub-minute now!
  WAREHOUSE  = m_wh
AS
SELECT
  customer_id,
  name,
  email,
  MAX(updated_at) updated_at
FROM landing.customers_raw
GROUP BY 1,2,3;
```

### Sub-Second Ingestion (Snowpipe Streaming)

Point a Dynamic Table at orders_stream → instant dashboard.

```
-- Java/Python/Kafka client → 1 line insert
INSERT INTO prod.orders_stream
VALUES (RECORD_CONTENT => :json_payload);
```

### Snowpipe (files → table) + Auto-Upsert

```
-- 1. Auto-ingest files
CREATE PIPE prod.pipes_orders
  AUTO_INGEST = TRUE
  AS COPY INTO prod.orders_raw FROM @s3_stage;

-- 2. Auto-upsert every minute
CREATE TASK prod.merge_orders
  WAREHOUSE = s_wh
  SCHEDULE  = '1 minute'
WHEN SYSTEM$STREAM_HAS_DATA('orders_raw_cdc')
AS MERGE INTO prod.orders t USING prod.orders_raw_cdc s ...
```

## What is Snowflake Dynamic Table?

A materialized, auto-refreshing table defined by pure SQL.

Snowflake runs your query incrementally whenever upstream data changes and guarantees the result is no older than TARGET_LAG.

Think: dbt model + Airflow DAG + Kafka Streams — but written in 5 lines of SQL and fully managed.

## what should I use for my data processing and later data serving. Snowflake or DataBricks?

| # | Question (tick ONE)                                      | ✅ Snowflake | ✅ Databricks |
|---|----------------------------------------------------------|--------------|---------------|
| 1 | Do business analysts / BI teams write 80 % of the SQL?  | [✅]          | [ ]           |
| 2 | Do you already have Snowflake credits in the budget?    | [✅]          | [ ]           |
| 3 | Need sub-30-second latency on Kafka / IoT streams?      | [ ]           | [✅]          |
| 4 | Will data scientists run Python notebooks or LLMs?      | [ ]           | [✅]          |
| 5 | Must the SAME table be readable from PowerBI, Trino, Synapse? | [ ]    | [✅]Iceberg   |
| 6 | Is your monthly budget hard-capped at $3,000?           | [✅]          | [ ]           |
| 7 | Want ZERO cluster tuning (no Spark UI ever)?            | [✅]          | [ ]           |
| 8 | Need Git-style table branches or a feature store?       | [ ]          | [✅]           |

## I am on azure. I need to process data streams from kafka. What should I choose: databrics or snowflake?

| # | Question (tick ONE)                              | ✅ Snowflake | ✅ Databricks |
|---|--------------------------------------------------|--------------|---------------|
| 1 | Latency < 30 seconds to dashboard                | []           | [✅ ]         |
| 2 | Kafka payload is JSON → needs Python UDF / LLM?  | []           | [✅ ]         |
| 3 | Want ZERO code for upserts (just SQL)?           | [✅]         |               |

## How do I create an event on azure event hub after a new file is created in azure storage account and then this event is read by azure logic apps that triggers databrices job?

```
┌─ 1. Storage Account (NO Event Grid)  
└─ 2. Azure Function (python 1 file)  
└─ 3. Event Hub (1 hub)  
└─ 4. Logic App (2 clicks)  
└─ 5. Databricks Job (same JSON)
```

2. Auzre Function

```
import logging
import json
import azure.functions as func
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

async def main(myblob: func.InputStream, context: func.Context):
    logging.info(f"Python Blob trigger: {myblob.name}")

    # 1. Build payload
    payload = {
        "blob_name": myblob.name.split("/")[-1],
        "blob_url" : f"https://{myblob.name.split('/')[0]}.blob.core.windows.net{'/'.join(myblob.name.split('/')[1:])}",
        "size"     : myblob.length,
        "triggered_at": context.invocation_id
    }

    # 2. Send to Event Hub
    connection_str = func.FuncContext.get_setting("EventHubConn")
    producer = EventHubProducerClient.from_connection_string(connection_str)
    async with producer:
        event_data_batch = await producer.create_batch()
        event_data_batch.add(EventData(json.dumps(payload)))
        await producer.send_batch(event_data_batch)

    logging.info(f"Sent to Event Hub: {payload['blob_name']}")
```

binding to trigger it when new file arrives:

```
{
  "scriptFile": "__init__.py",
  "bindings": [
    {
      "name": "myblob",
      "type": "blobTrigger",
      "direction": "in",
      "path": "landing/{name}",
      "connection": "AzureWebJobsStorage"
    }
  ]
}
```

4. Logic App

```
# Portal → Logic Apps → Consumption → Blank
1. Trigger:  "When one or more events arrive" (Event Hub)
   Hub:      new-blob
   Consumer group: $Default

2. Action:   "Run a Databricks job"
   Job ID:   <copy from Databricks>
   Parameters:
     blob_url:  @{triggerBody()?['contentData']?['blobUrl']}
```

5. DataBricks job

```
{
  "name": "job-blob-trigger",
  "tasks": [{
    "task_key": "process",
    "notebook_task": {
      "notebook_path": "/Repos/prod/process_blob.ipynb",
      "base_parameters": { "blob_url": "{blob_url}" }
    },
    "existing_cluster_id": "1102-123456-abc789"
  }]
}
```

## What is Microsoft Data Fabric ?

One platform that replaces Azure Synapse + Data Factory + Power BI + Databricks notebooks.
Everything lives in OneLake (a tenant-wide data lake) and you switch engines with one click.

```
┌─ ONE LAKE (the brain)  
│   OneLake = ADLS Gen2 + shortcuts to S3/GCS/on-prem  
│   Every workspace gets its own folder – no more silos  
│  
├─ 7 WORKLOADS (pick any, mix any)  
│   1. Data Factory      → 200+ connectors, no-code pipelines  
│   2. Data Engineering  → Spark notebooks (Py/SQL/Scala)  
│   3. Lakehouse         → Delta tables + SQL endpoint  
│   4. Data Warehouse    → T-SQL, star-schema, auto-optimize  
│   5. Real-Time Intel   → KQL + Eventstream (Kafka in 1 click)  
│   6. Data Science      → MLflow + AutoML + Experiments  
│   7. Power BI          → DirectLake mode (zero refresh)  
│  
├─ COPILOT IN EVERYTHING  
│   “Write me a pipeline” → Copilot spits 50 lines of code  
│   “Explain this table” → natural language summary
```

### How can I create Microsoft Data Fabric on Azure?

```
┌───────────────────────────────────────────────────────┐
|  CREATE FABRIC IN 180 SECONDS                         │
│                                                       │
│  1 portal.azure.com                                   │
│  2 Type “Microsoft Fabric”                            │
│  3 Click blue “Start free trial”                      │
│  4 Pick your region (East US 2 = fastest)             │
│  5 Click “Create”                                     │
│  6 Open fabric.microsoft.com → “My workspace”         │
│                                                       │
│  YOU NOW HAVE:                                        │
│  • F64 capacity (64 CU) = 15 Databricks DBR hours     │
│  • OneLake (unlimited shortcuts)                      │
│  • Copilot in every notebook
```

## Can I use dbt with databricks. How can I do it. Show me example.

YES → dbt + Databricks = 2025 Gold Standard

3 WAYS TO USE dbt ON DATABRICKS                   
- 1. dbt Cloud (zero code)                          
- 2. dbt Core locally → Databricks SQL Warehouse   
- 3. dbt Core as Databricks Job (native task)


| Feature             | OPTION 1 – dbt Cloud    | OPTION 2 – dbt Core   | OPTION 3 – dbt Core
|                     | 1-click Partner Connect | Local laptop          | Native Databricks Job
|---------------------|-------------------------|-----------------------|-----------------------
| Setup time          | 30 seconds              | 3 minutes             | 2 minutes
| Cost (1 TB project) | $0 → $100/mo (team tier)| $0                    | $0 (uses your cluster)
| IDE                 | Web IDE + Copilot + PR  | VS Code (your plugins)|Databricks notebook (no lint)
| Git sync            | Native GitHub/GitLab/Azure DevOps|Native        | Native (repo → job)
| Scheduler           | UI + Slack + email + retry| Cron / GitHub Actions | Databricks Workflows (GUI cron)
| Run on serverless SQL| Auto-created warehouse |You pick warehouse     | You pick warehouse
| Tests & docs        | Auto-run + hosted docs + Slack on fail | Manual | Auto in job → email
| Secrets             | Built-in vault          | .env + gitignore      | Databricks secrets scope
| Team collaboration  | PR reviews + locks + dev/prod | Manual          | Manual
| Zero-ops for BI team|100 %                    | 0 %                   | 80 %
| Run locally (no VPN)|Yes                      | Yes                   | No
| Debug in Spark UI   | No                      | No                    | Yes
| Best for            | Teams > 3 people        | Solo devs / free      | 100 % Databricks UI


## How to run Azure ADF on custom server in data center?

1. ADF Studio (cloud) → Create SHIR  (self-hosted integration runtime)
2. Your server → Install 1 EXE  
3. Paste 2 keys → Green check  
4. Pipelines run ON YOUR SERVER

## My data is on AzureSQL database. How can I upload it into snowflake ?

Azure SQL → Snowflake (direct, no blob)        
1. ADF → New Pipeline → Copy Data           
2. Source: Azure SQL Dataset                
3. Sink:   Snowflake Dataset              
4. Disable staging → Direct copy     // single threaded, public internet
   - Use Swnoflake Private link and Blob private endpoint     
5. Trigger: Every 5 min

Using Azure Storage Account in the middle migh have these advantages:
- 10× faster (parallel unload)
- Cheaper ($0.01/GB vs $0.12/DIU-hour)
- Resume if Wi-Fi dies
- Works with PII (private endpoint + VNet IR)
