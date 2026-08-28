# Data Lakehouse Architecture

## What is a Data Lake vs Lakehouse?

__Data Lake:__
- __Centralized__ storage for raw + processed data
- __Cheap__, scalable object storage
- __Schema-on-read__
- Historically weak on governance & performance

__Lakehouse__: A data lake + warehouse features:
- __ACID__ transactions
- __Schema__ enforcement & evolution
- __Time travel__
- Performance optimizations
- SQL-first analytics
- Key enablers: Delta Lake, Apache Iceberg, Apache Hudi

## Ingestion Layer

### Batch ingestion

- Used for:
  - Databases
  - Files
  - Periodic exports
- Techniques
  - Full loads (initial)
  - Incremental loads (timestamp, watermark)
  - CDC (change data capture)
- Tools
  - Airflow, Dagster (orchestration)
  - Spark, Flink (processing)
  - Debezium, Fivetran (CDC)

### Streaming ingestion

- Used for:
  - Events
  - Logs
  - Near-real-time analytics
- Flow: Source → Kafka/Kinesis → Stream processor → Lake
- Design choices
  - Exactly-once vs at-least-once
  - Event time vs processing time
  - Late-arriving data handling

## Storage Layer

__Object storage__: Foundation of the lake/lakehouse:
- __S3 / ADLS / GCS__
- Cheap, durable, infinite scale
- Append-only by nature

__File formats__:
- Columnar:
  - __Parquet__
    - Predicate pushdown
    - Compression
    - Vectorized reads
- Table formats (sit on top of parquet)
  - __Delta Lake__: Simplicity, ecosystem
  - __Apache Iceberg__: Open spec, engine-agnostic
  - __Apache Hudi__: Streaming & upserts
  - table formats add:
    - ACID transactions
    - Schema enforcement/evolution
    - Snapshots & time travel
    - Compaction & file management
  
__Partitioning & layout__:
- Good partitions
  - High cardinality filters (date, region)
  - Avoid over-partitioning
- Optimizations
  - File compaction
  - Z-ordering / clustering
  - Data skipping indexes

## Compute Engines

Compute is decoupled from storage.

Multiple engines, one source of truth.

### Batch & SQL engines

| Engine         | Strength                   |
| -------------- | -------------------------- |
| Spark          | Heavy ETL, ML              |
| Trino / Presto | Fast interactive SQL       |
| DuckDB         | Local / embedded analytics |
| Snowflake      | Managed, proprietary       |

### Streaming engines

- Spark Structured Streaming
- Flink
- Kafka Streams

## Metadata, Catalog & Lineage

Without strong metadata:
- Data is untrustworthy
- Self-service fails
- Governance is manual

Metadata types:
- Technical metadata
  - Schemas
  - Partitions
  - File locations
  - Statistics
- Business metadata
  - Definitions
  - Owners
  - SLAs
  - Sensitivity

| Tool               | Purpose              |
| ------------------ | -------------------- |
| Hive Metastore     | Legacy               |
| AWS Glue           | Managed              |
| Unity Catalog      | Databricks           |
| Apache Polaris     | Open Iceberg catalog |
| DataHub / Amundsen | Discovery & lineage  |

## Governance & Security

### Access control:
- Table / column / row-level security
- Attribute-based access control (ABAC)

Implemented via
- Catalog
- Query engine
- Identity provider

### Data classification:
- PII
- PHI
- Financial data

Drives:
- Masking
- Tokenization
- Audit logging

### Lineage

Tracks: Source → transformations → consumption

Critical for:
- Impact analysis
- Compliance
- Debugging

__AWS Glue__
- AWS Glue gives you some lineage, but not end-to-end by default. 
- OpenLineage + Marquez / DataHub
  - Instrument Glue Spark jobs
  - Emit lineage events
  - Capture:
    - Dataset in/out
    - Column mappings
    - Job runs

__Azure data lake and databrics__:
- Unity Catalog (UC) provides automatic lineage for:
  - Tables & views
  - Notebooks
  - Jobs
  - Delta tables
  - Lineage captured:
    - Table → table
    - Notebook → table
    - Job → table
    - View dependencies
  - This works automatically when:
    - You use UC-managed tables
    - You run queries in Databricks (SQL, notebooks, jobs)

### Data quality

Implemented as:
- Validation rules
- Freshness checks
- Volume anomaly detection

Often integrated into:
- Pipelines
- Orchestration layer

## Database / User Experience

SQL experience: A good lakehouse feels like a database:
- Fast queries
- Predictable performance
- Stable schemas
- Transactions

Achieved via
- Materialized views
- Aggregations
- Caching
- Semantic layers

### Semantic layer: Maps technical data → business concepts.

Examples:
- dbt metrics
- LookML
- Cube

Benefits:
- Consistent definitions
- Less duplicated logic
- Easier self-service

### BI & ML consumption

BI tools: 
- Tableau, Power BI, Looker, 
- Direct query or extracts

ML workflows
- Feature stores

## Modern Lakehouse Reference Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                         DATA SOURCES                         │
│                                                              │
│  OLTP DBs   SaaS Apps   Logs   Events   Files   IoT   APIs    │
└───────────────┬───────────────┬───────────────┬─────────────┘
                │               │               │
                ▼               ▼               ▼
┌──────────────────────────────────────────────────────────────┐
│                      INGESTION LAYER                          │
│                                                              │
│  Batch / CDC                     Streaming                  │
│  - Airflow / Dagster             - Kafka / Kinesis           │
│  - Debezium / Fivetran           - Event Hubs                │
│  - Spark / Flink                 - Spark / Flink             │
│                                                              │
│  • Idempotent writes                                     │
│  • Schema capture & validation                           │
└───────────────┬──────────────────────────────────────────────┘
                ▼
┌──────────────────────────────────────────────────────────────┐
│                DATA LAKE STORAGE (OBJECT STORE)               │
│                                                              │
│  S3 / ADLS / GCS                                             │
│                                                              │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐     │
│  │  BRONZE      │ → │  SILVER      │ → │  GOLD        │     │
│  │  Raw data    │   │  Cleaned     │   │  Curated     │     │
│  │  Immutable   │   │  Standard    │   │  Business    │     │
│  └──────────────┘   └──────────────┘   └──────────────┘     │
│                                                              │
│  File Format: Parquet / ORC                                  │
└───────────────┬──────────────────────────────────────────────┘
                ▼
┌──────────────────────────────────────────────────────────────┐
│              TABLE FORMAT / TRANSACTION LAYER                 │
│                                                              │
│   Delta Lake / Apache Iceberg / Apache Hudi                  │
│                                                              │
│   • ACID transactions                                       │
│   • Schema enforcement & evolution                          │
│   • Time travel & snapshots                                 │
│   • Compaction & file optimization                          │
└───────────────┬──────────────────────────────────────────────┘
                ▼
┌──────────────────────────────────────────────────────────────┐
│                     METADATA & GOVERNANCE                    │
│                                                              │
│  Catalogs:                                                   │
│  - Hive Metastore / AWS Glue                                 │
│  - Unity Catalog / Apache Polaris                            │
│                                                              │
│  Governance:                                                 │
│  - RBAC / ABAC                                               │
│  - Row & column security                                    │
│  - Data classification (PII / PHI)                           │
│                                                              │
│  Observability:                                              │
│  - Lineage (DataHub / Amundsen)                              │
│  - Data quality checks                                      │
│  - Auditing & compliance                                    │
└───────────────┬──────────────────────────────────────────────┘
                ▼
┌──────────────────────────────────────────────────────────────┐
│                    COMPUTE / QUERY ENGINES                   │
│                                                              │
│  Batch / ETL             Interactive SQL                     │
│  - Spark                 - Trino / Presto                   │
│  - Flink                 - DuckDB                           │
│                          - Snowflake (optional)              │
│                                                              │
│  • Decoupled from storage                                   │
│  • Elastic scaling                                          │
└───────────────┬──────────────────────────────────────────────┘
                ▼
┌──────────────────────────────────────────────────────────────┐
│                 SEMANTIC & SERVING LAYER                     │
│                                                              │
│  - dbt / Metrics layer                                      │
│  - LookML / Cube                                            │
│  - Feature Store (ML)                                       │
│                                                              │
│  • Business definitions                                     │
│  • Reusable metrics                                         │
└───────────────┬──────────────────────────────────────────────┘
                ▼
┌──────────────────────────────────────────────────────────────┐
│                        CONSUMERS                             │
│                                                              │
│  BI Tools        Data Science        Applications             │
│  - Tableau       - Notebooks         - APIs                   │
│  - Power BI      - ML Pipelines      - Reverse ETL            │
│  - Looker                                                │
└──────────────────────────────────────────────────────────────┘

```

# Compare lakehouse vs traditional warehouse

Traditional Data Warehouse: A centralized, tightly coupled system optimized for:
- Structured data
- SQL analytics
- Strong governance
- Predictable performance
- Examples: Teradata, Oracle DW, SQL Server DW, Snowflake (modern but still warehouse-centric)

Lakehouse: A data lake with warehouse guarantees, built on:
- Object storage
- Open file + table formats
- Decoupled compute
- Multiple engines
- Examples: Delta Lake, Apache Iceberg, Apache Hudi (often with Spark / Trino / Databricks)

__A lakehouse is a flexible data platform that can behave like a warehouse, if you invest in metadata, governance, and tuning__

Comparison:
```
| Dimension    | Traditional Warehouse     | Lakehouse                                 |
| ------------ | ------------------------- | ----------------------------------------- |
| Storage      | Proprietary               | Object storage (S3/ADLS/GCS)              |
| Data types   | Structured                | Structured, semi-structured, unstructured |
| Schema       | Schema-on-write           | Schema-on-write + read                    |
| Compute      | Tightly coupled           | Decoupled, elastic                        |
| File formats | Proprietary               | Parquet / ORC                             |
| ACID         | Yes                       | Yes (via table formats)                   |
| Cost model   | Expensive, capacity-based | Cheap storage + pay-for-compute           |
| Openness     | Vendor lock-in            | Open standards                            |
| Streaming    | Limited                   | First-class                               |
| ML support   | Weak                      | Strong                                    |
| Governance   | Strong                    | Improving / depends on tooling            |
| Performance  | Very predictable          | Depends on tuning                         |
```

Data ingestion & modeling:
- Warehouse
  - Heavy upfront ETL
  - Star/snowflake schemas
  - Schema changes are painful
- Lakehouse
  - ELT-friendly
  - Raw → refined zones
  - Flexible schema evolution

Workloads:
```
| Use case               | Warehouse       | Lakehouse    |
| ---------------------- | --------------- | ------------ |
| BI dashboards          | Excellent       | Very good    |
| Ad-hoc analytics       | Good            | Excellent    |
| ML feature engineering | Poor            | Excellent    |
| Streaming ingestion    | Limited         | Native       |
| Data sharing           | Vendor-specific | Open formats |
| Data science notebooks | Awkward         | Natural      |

```

Choose a traditional warehouse if:
- BI is your primary workload
- Data is mostly structured
- You value predictability over flexibility
- Team is small or SQL-only
- Pros: Consistent query performance, Optimized for joins and aggregates, Easier to operate, Fewer moving parts
- Cons: Scaling is expensive, Pay for provisioned capacity, Storage is expensive

Choose a lakehouse if:
- You handle diverse data types
- You need streaming + batch
- ML is a priority
- Cost and openness matter
- You expect rapid evolution
- Pros: Massive parallelism, Object storage is very cheap, Compute can be turned off
- Cons: Requires tuning (partitioning, compaction), More components

# Explain Iceberg

Iceberg achieves ACID guarantees by treating metadata as the transaction boundary. 
Data files are immutable, and each table version is a snapshot pointing to manifests that describe data and deletes. 
This enables snapshot isolation, safe concurrent reads and writes, schema and partition evolution, and multi-engine interoperability — at the cost of requiring active metadata maintenance.

Iceberg turns object storage into a transactional database by managing immutable files with a metadata-driven commit protocol.

An Iceberg table is not a directory of files. It’s a metadata graph.
```
Iceberg Table
 ├── Catalog entry
 ├── Metadata files (JSON)
 ├── Manifest lists (Avro)
 ├── Manifests (Avro)
 └── Data files (Parquet / ORC / Avro)
```

The catalog (control plane) stores:
- Table name
- Current metadata file pointer
- Table properties
- Examples: Hive Metastore, AWS Glue, REST / Polaris

Metadata files
- Each metadata file represents a table snapshot and is immutable
- It contains: Schema(s), Partition spec(s), Snapshot list, Current snapshot ID, Table properties

Manifest lists & manifests:
- Manifest
  - Lists data files or delete files
  - Includes statistics:
    - Min/max values
    - Null counts
    - Record counts
  - This enables:
    - Predicate pushdown
    - File-level pruning
    - Fast planning

Data files
- Stored in object storage
- Immutable
- Columnar (Parquet most common)
- Iceberg never updates files in place.

ACID transactions (how writes work)
- Write flow
  - Writer reads current metadata pointer
  - Writes new data files
  - Writes new manifests
  - Writes new metadata file
  - Attempts to atomically update catalog pointer
  - If step 5 fails → transaction aborts safely
  - No locks on data files. Only atomic metadata swap.
- Multiple readers: Always safe.
- Multiple writers
  - Optimistic concurrency:
  - Conflict detection at commit time
  - Conflicting writes fail and retry

Schema evolution:
- Iceberg tracks schema by field IDs, not names.
- You can safely:
  - Rename columns
  - Reorder columns
  - Add / drop columns

# Explain Parquet

Apache Parquet is a columnar, compressed, self-describing file format optimized for analytical workloads.

It’s a storage format.

```
Parquet File
 ├── File Header
 ├── Row Groups
 │    ├── Column Chunks
 │    │    ├── Pages
 │    │    │    ├── Data Page(s)
 │    │    │    └── Dictionary Page (optional)
 └── File Footer (metadata)
```

Physical File Structure:
- __File Header__: Contains the magic number PAR1.
- __Data__: The actual column data, broken into row groups and compressed using various encodings (like Run-Length Encoding for repeating values).
- __File Metadata__: Located at the end of the file, it describes the __schema__, __compression__ used, __statistics (min/max values)__ for each column in each row group, and the location of the data blocks.
- __File Footer__: Contains the size of the metadata and the magic number PAR1 again, allowing readers to quickly locate the metadata at the end of the file without reading the entire data portion

# Explain and compare Streaming vs micro-batch

Streaming (true streaming):  Process events one at a time as they arrive.
- Continuous execution
- Event-driven
- Latency measured in milliseconds

Micro-batch: Process events in small batches at fixed intervals (e.g., every 1–60 seconds).
- Discrete execution
- Time-sliced
- Latency measured in seconds

## Execution model

Streaming:
```
Event → Operator → State → Output
       (always running)
```

Micro-batch execution:
```
Collect events (Δt)
→ Create batch
→ Run batch job
→ Commit results
→ Repeat
```

## how Spark Structured Streaming works? Can it use presto and iceberg?

Structured Streaming runs in micro-batch mode:
```
Trigger fires (e.g. every 10s)
→ Read new data since last offset
→ Build a logical plan (like batch Spark SQL)
→ Execute physical plan
→ Commit results
→ Update offsets & state
```

Each micro-batch is:
- A normal Spark SQL job
- Deterministic
- Fully fault-tolerant

Kafka → Spark Structured Streaming → Iceberg table

Per micro-batch:
- Spark writes new Parquet files
- Iceberg commits snapshot atomically
- Exactly-once at snapshot level

# Iceberg vs Delta Lake — comparison

__Apache Iceberg__: Open, engine-agnostic table format with metadata-driven transactions.

__Delta Lake__: Tightly integrated transactional layer optimized for Spark ecosystems.
- Log-based
- Databricks-led roadmap
- Best experience inside Databricks


Storage & metadata model:
- Iceberg: Catalog → Metadata JSON → Manifest lists → Manifests → Data files

- Delta (centralized transaction log):
  - Append-only log
```
_delta_log/
  ├── 000000.json
  ├── 000001.json
  ├── ...
  └── checkpoints
```

# how data platform should enable AI?

- __Unified storage & open table formats__ (Iceberg, Delta Lake, Hudi)
  - One copy of data serves batch analytics, real-time, ML feature store AND vector workloads → avoids duplication tax
- Native __vector__ + __multimodal__ support
  - Columnar vector indexing (or integration with specialized vector DBs)
  - Embedding storage, similarity search at scale (HNSW, IVF, etc.)
  - Multimodal support (text + image + audio + video embeddings in same table/query)
- Very high-scale & cost-efficient object __storage__ tier
  - AI training/fine-tuning eats petabytes → must use S3/Azure ADLS/GCS cheaply
- __Real-time__ & streaming-first ingestion
  - Kafka / Pulsar / Redpanda + streaming tables
  - Change Data Capture (CDC) treated as first-class citizen
- Strong data __lineage__ + observability at column/field level
- __Semantic layer__ / business glossary enforced at query time
  - Prevents hallucination via inconsistent metric/term definitions
- PII / __sensitive data__ classification + masking / anonymization pipeline
- RAG / agent-friendly retrieval patterns

# Re:Invent

## Open and Secure Lakehouse

- Zero ETL
- Query Federation
- Catalog Federation: glue to connect to Polaris Catalog, Databricks Unity etc.
- Polaris metadata catalog and snowflake
- Tag db columns to identify pii data
- Apache Iceberg: ACID + Scalable metadata + Schema enforcment and evolution + Time-Travel
  . issues with iceberg: loading small files, new versions of data (more files, often not used)
