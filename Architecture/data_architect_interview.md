# Prepare for Data Architect Interview

## End-to-End Data Architecture Design

## Data Architecture patterns

- __Medallion Architecture__ (also called Bronze → Silver → Gold or Multi-layer Lakehouse)

  | Layer  | Content                              | Data Quality / Schema            | Typical Consumers                     | Format Examples                       |
  |--------|--------------------------------------|----------------------------------|---------------------------------------|---------------------------------------|
  | Bronze | Raw data "as arrived"                | Almost none                      | Data engineers (replay, debug)        | Parquet / Avro / JSON on object store |
  | Silver | Cleansed, conformed, lightly modeled | Good quality, enforced types     | Analysts, data scientists,            | Delta / Iceberg / Hudi tables         |
  | Gold   | Aggregated, business-ready, dimensional models | High quality, governed | BI tools, executives, Apps, AI agents | Same open formats / semantic layer    |

- __Platform-level Architectural Paradigms__
  - __Data Lakehouse__ (currently the fastest-growing pattern)
    - One copy of data (usually on object storage)
    - Open table format (Iceberg, Delta Lake, Hudi most popular in 2026)
    - ACID transactions + schema evolution + time travel
    - Multiple engines can read/write (Spark, Trino, Snowflake, DuckDB, Polars, AI tools…)
  - __Data Mesh__
    - Organizational/social paradigm more than purely technical
    - Domain-oriented data products (each business domain owns & publishes its data)
    - Data is treated like a product (discoverable, addressable, trustworthy, self-describing)
    - Decentralized ownership + centralized standards & discoverability
    - Best when: >1,000–2,000 engineers or very autonomous business units
  - __Data Fabric__
    - Data stays where it lives (Salesforce, SAP, Snowflake warehouse, Databricks lakehouse, Azure SQL DB, S3 raw files, Kafka streams, on-prem Oracle, etc.).
    - A fabric layer (active metadata + automation) discovers, catalogs, virtualizes, governs, and sometimes lightly transforms data without forcing mass movement.
    - You query through a unified semantic / virtual view — it often looks like one big database to the user/analyst/AI agent.
    - Metadata-driven, automated integration & governance layer
    - Active metadata + AI-assisted discovery, lineage, access control
    - Virtual views across heterogeneous sources (no massive copying)
    - Goal: "find, understand, use any data without 50 ETL jobs"
    - Data Fabric on AWS:
      - storage: S3
      - metadata catalog: AWS Lake Formation + AWS Glue Data Catalog
      - federation: AWS Athena or ResShift Spectrum or Trino
      - Integration: AWS Glue + Lambda
      - Semantic layer: dbt semantic / cubeJS
      - Governance + Security: AWS IAM, Macie, LakeFormation
      - Observability: CloudWatch
      - AI: Sagemaker, Bedrock
    - Data Fabric on Azure:
      - Storage: Azure Data Lake Storage Gen2: bronze->silver->gold
        - ADLS Gen2: enhanced mode of Blob Storage: +Hierarchical namespace, Fine-grained security
      - metadata catalog: Microsoft Purview: ADLS Gen2, Blob Storage, AzureSQL, CosmosDB: automated scanning, scehma extraction, lineage
      - federation (query across data):
        - Azure Synapse Analytics (serverless SQL, external tables)
        - Azure Databricks (Delta Lake, SQL endpoints)
      - integration (ETL / pipelines): Azure Data Factory, Azure Functions
      - semantic layer: power BI (semantic models) or dbt (runs on Synapse / Databricks)
      - governance + security: Microsoft Purview, Azure Active Directory, Azure Key Vault
      - observability: Azure Monitor, Azure Log Analytics
      - AI / ML: Azure Machine Learning, Azure OpenAI Service

    | Component                 | Purpose                                                            | Typical Tech Examples (2026)                                 |
    |---------------------------|--------------------------------------------------------------------|--------------------------------------------------------------|
    | Active Metadata Engine    | Continuously crawls/scans sources, builds knowledge graph of data  | Atlan, Collibra, Alation, Microsoft Purview + AI extensions  |
    | Data Catalog & Discovery  | Self-service search + lineage + "find similar datasets"            | Above + embedded AI recommendations                          |
    | Federated Query Engine    | Push-down queries to source systems when possible                  | Starburst/Trino, Dremio, Presto variants, Snowflake External Tables |
    | Virtualization / Views    | Create unified views without copying data                          | dbt Semantic Layer + virtualization, Denodo, IBM watsonx.data |
    | Automated Integration     | AI-suggested or auto-generated light transforms when needed        | Informatica CLAIRE, Talend AI, Matillion AI                  |
    | Policy & Access Enforceme | Consistent RBAC, data masking, compliance across all sources       | Immuta, Okera (legacy), Purview + integrations               |
    | Orchestration & Observability     | Monitors data flows, freshness, quality across the "fabric"| Monte Carlo, Anomalo, integrated in Atlan/Collibra           |

    ```
    Sources (DBs, SaaS, streams)
          ↓
    Ingestion (Glue, Kinesis, Lambda)
            ↓
    Storage (S3 + Iceberg tables)
            ↓
    Metadata (Glue Catalog + Lake Formation)
            ↓
    Query/Federation (Athena, Redshift, Trino)
            ↓
    Semantic Layer (dbt / Denodo)
            ↓
    Consumption (BI, ML, Apps)
    ```

| Concept  | Data Lakehouse                                                                                                                                   | Data Fabric                                                                                                     |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| Purpose  | **Store and query all enterprise data** in one place, combining features of data lakes (cheap storage) and data warehouses (structured querying) | **Unify and integrate data** across multiple sources and locations; provide a consistent, governed access layer |
| Focus    | **Storage + analytics**                                                                                                                          | **Integration + access + governance**                                                                           |
| Examples | Snowflake, Databricks Lakehouse, Delta Lake                                                                                                      | Informatica, Talend, IBM Cloud Pak for Data                                                                     |


### Ingestion: batch + streaming (Kafka, CDC, APIs)

### Storage:

- Data lake (S3)
- Warehouse (Snowflake / Redshift / BigQuery)
- Lakehouse (Databricks)

### Processing:

- ETL/ELT (Spark, dbt)
- Streaming (Flink, Kafka Streams)

### Serving:

- BI tools
- APIs
- ML pipelines

### Governance:

- Catalog, lineage, quality checks



## Tradeoffs

Structure answers like: Context, Options, Tradeoffs, Decision

### Snowflake vs Databricks?

Two different philosophies:
- Snowflake → warehouse-first, simplicity, SQL-centric
- Databricks → lakehouse-first, flexibility, data + AI unification

|           | Snowflake              | Databricks                     |
| --------- | ---------------------- | ------------------------------ |
| Core idea | Cloud data warehouse   | Lakehouse (data + AI platform) |
| Storage   | Proprietary + external | Open formats (Delta Lake)      |
| Users     | Analysts, BI teams     | Data engineers, ML teams       |
| Interface | SQL-first              | Notebook + SQL + Python        |

Comparison:
| Category | Snowflake | Databricks |
|----------|----------|------------|
| Core Concept | Cloud data warehouse | Lakehouse (data + AI platform) |
| Primary Users | Analysts, BI teams | Data engineers, data scientists |
| __Ease of Use__ | Very easy, fully managed | Steeper learning curve |
| __Interface__ | SQL-first | SQL + Python + Scala + Notebooks |
| Data Engineering | Limited flexibility | Very strong (Spark-based) |
| __BI / Analytics__ | Excellent performance & concurrency | Good, improving (Photon) |
| __Machine Learning / AI__ | Moderate capabilities | Best-in-class, ML-native |
| __Streaming__ | Limited | Strong (real-time pipelines) |
| Storage Format | Proprietary + external tables | Open formats (Delta Lake, Parquet) |
| Vendor Lock-in | Higher | Lower (open ecosystem) |
| Performance Tuning | Mostly automatic | Requires tuning (clusters, jobs) |
| Governance | Strong, built-in | Powerful but more complex (Unity Catalog) |
| Data Sharing | Excellent (native sharing) | Improving |
| Cost Model | Can get expensive with scale | Can be optimized but complex |
| Ecosystem Integration | Strong with BI tools | Strong with ML/AI ecosystem |
| __Best Use Case__ | BI, dashboards, SQL analytics | Data engineering, ML, AI pipelines |

Query Performance:
| Scenario / Factor | Snowflake | Databricks |
|------------------|----------|------------|
| __Out-of-the-box SQL speed__ | Very fast, no tuning needed | Good, but often needs tuning |
| __Ad hoc queries (BI)__ | Excellent | Good (improving with Photon) |
| __Complex joins__ / window functions | Very strong optimizer | Strong, but may require tuning |
| Large-scale ETL queries | Good | Excellent (Spark advantage) |
| __Semi-structured data (JSON, logs)__ | Good | Excellent |
| __Concurrency__ (many users) | Best-in-class | Good, requires configuration |
| Cold start latency | Very low (seconds) | Higher (cluster spin-up unless serverless) |
| Caching | Automatic, very effective | Available, but less transparent |
| Performance consistency | Very consistent | Varies depending on tuning |
| Max performance ceiling | High | Very high (with optimization) |

### Batch vs streaming?

### Data lake vs warehouse vs lakehouse

| Category | Data Lake | Data Warehouse | Lakehouse |
|----------|----------|----------------|-----------|
| Core Concept | Store all raw data (schema-on-read) | Structured, curated analytics system (schema-on-write) | Combines lake + warehouse capabilities |
| __Data Types__ | Structured, semi-structured, unstructured | Mostly structured | All data types |
| __Schema__ | Applied at read time | Applied at write time | Hybrid (flexible + enforced) |
| __Storage__ | Cheap object storage (e.g., S3) | Proprietary or managed storage | Object storage + table formats |
| __Performance__ | Slower for SQL analytics | Very fast for BI queries | Fast (approaching warehouse performance) |
| Data Quality | Low (raw data) | High (cleaned, modeled) | Medium → High (with governance) |
| __Use Cases__ | Data ingestion, ML, raw storage | BI, dashboards, reporting | Unified analytics + ML + BI |
| Users | Data engineers, data scientists | Analysts, business users | Engineers, analysts, scientists |
| Cost | Low storage cost | Higher cost | Optimized (low storage + scalable compute) |
| Governance | Weak (unless added) | Strong | Strong (with tools) |
| Flexibility | Very high | Low | High |
| Data Processing | External engines needed | Built-in optimized SQL engine | Built-in + open engines |
| Examples | S3 + Hadoop ecosystem | Snowflake, Redshift | Databricks, Snowflake (hybrid), Iceberg-based stacks |
| __Key Weakness__ | “Data swamp” risk | Rigid, expensive | Complexity, still evolving |

### ETL vs ELT?

### Kafka vs Kinesis?



## Cloud + Infrastructure

### S3, Redshift, DynamoDB

### Kafka / MSK

### Lambda / ECS / EKS

### Terraform (IaC)


## Event-Driven / Microservices Data

### Event streams (Kafka topics)

### Schema evolution (Avro, Protobuf)

### CDC (Debezium)

### Handling late / out-of-order data



## AI/ML + Data Architecture

Supporting AI means shifting from just “tables for analysts” to a flexible, high-throughput, ML-ready data platform

| Aspect    | Traditional BI         | AI / ML Workloads                                                                  |
| --------- | ---------------------- | ---------------------------------------------------------------------------------- |
| Data Type | Structured, curated    | Structured, semi-structured, unstructured (text, images, video, logs, time-series) |
| Latency   | Minutes → hours        | Seconds → real-time (for streaming or inference)                                   |
| Volume    | Moderate               | Very large (TBs → PBs)                                                             |
| Schema    | Fixed, schema-on-write | Flexible, schema-on-read (especially for raw / feature data)                       |
| Users     | Analysts               | Data scientists, ML engineers, AI researchers                                      |
| Workload  | Aggregates, dashboards | Feature engineering, model training, inference, retraining                         |
| Compute   | SQL queries            | Heavy compute (GPU/CPU), distributed processing, batch + streaming                 |

- Flexible, unified __storage__ layer
  - Move beyond structured warehouses
  - Use a data lake or lakehouse:
- Centralized metadata & feature catalogs
  - Maintain active metadata:
    - Schema, lineage, quality metrics
    - Feature definitions (e.g., normalized, encoded, aggregated variables)
- Feature stores
  - Dedicated layer for ML features:
    - Centralizes feature definitions
    - Supports batch + real-time ingestion
    - Handles versioning of features
- High-throughput compute
  - AI/ML requires distributed compute:
    - Batch processing → Spark, Databricks
    - GPU acceleration → SageMaker, Databricks GPU clusters
    - Stream processing → Kinesis, Kafka, Flink
- Flexible data access patterns
  - Programmatic access (Python, R, notebooks, APIs)
  - Streaming & batch ingestion
- Governance + reproducibility
  - Dataset versioning
  - Experiment tracking
  - Access control + compliance
- Observability & data quality

```
Sources (DBs, APIs, IoT, logs, SaaS)
        ↓
Ingestion (Streaming: Kinesis/Kafka, Batch: Glue/Lambda)
        ↓
Raw + curated storage (S3 + Delta Lake)
        ↓
Feature engineering / transformation (dbt, Spark, Databricks)
        ↓
Feature store (Feast or custom)
        ↓
Model training (SageMaker, Databricks ML, PyTorch/TensorFlow)
        ↓
Model registry + deployment (SageMaker / MLflow)
        ↓
Serving & inference (real-time API / batch scoring)
```

| Use Case               | AWS Service                                      | Notes                                                |
| ---------------------- | ------------------------------------------------ | ---------------------------------------------------- |
| Feature store          | **Amazon SageMaker Feature Store**               | Centralized, reusable, and versioned features for ML |
| Model training         | **Amazon SageMaker**                             | Scalable training (CPU/GPU), distributed ML          |
| Experiment tracking    | **SageMaker Experiments / MLflow on Databricks** | Track datasets, parameters, model versions           |
| Inference / deployment | **SageMaker Endpoints / Batch Transform**        | Serve ML models in production                        |


### Feature stores

In machine learning, a feature is simply an input variable used by a model to make predictions.

Example: Predicting house prices. Features might be:
- square_feet
- num_bedrooms
- location
- year_built

| Characteristic                              | Description                                                             |
| ------------------------------------------- | ----------------------------------------------------------------------- |
| **Online & Offline stores**                 | Separate low-latency (real-time) and batch (training) stores            |
| **As-of feature retrieval**                 | Can retrieve features as-of a specific timestamp → avoids label leakage |
| **Versioning / history**                    | Automatically tracks feature changes over time                          |
| **Consistency across training & inference** | Guarantees features used in training match what’s served to models      |
| **Data validation & schema enforcement**    | Ensures feature types, dimensions, and constraints are correct          |
| **Integration with SageMaker ML pipelines** | Native integration for training, batch transform, endpoints             |
| **Automatic indexing**                      | Fast retrieval for online inference with low latency                    |
| **Metadata tracking**                       | Supports lineage, dataset documentation, and monitoring                 |

```
Raw data → Data ingestion (Glue / Kinesis / Lambda)
        ↓
Feature engineering (Databricks / SageMaker Processing / Spark)
        ↓
Feature Store (SageMaker Feature Store)
        ↓
Training (SageMaker, TensorFlow, PyTorch)
        ↓
Deployment & real-time inference (SageMaker Endpoint)
```

Features are derived or computed from raw data, and they can change over time due to:
- Business logic changes: You redefine active_user to include mobile + web
- Data updates / corrections: A customer’s last purchase was recorded late or corrected

How to use Feature Store:
- Define a feature group: A Feature Group is like a table for your features.
  ```
  customer_features.create(
    s3_uri=f"s3://my-bucket/feature-store/",
    record_identifier_name='customer_id',
    event_time_feature_name='event_time',
    role_arn='arn:aws:iam::<account_id>:role/service-role/AmazonSageMaker-ExecutionRole-2026',
    enable_online_store=True,
    feature_definitions=feature_group_definition
  )
  ```
- Ingest data into Feature Store
  ```
  df = pd.DataFrame({
      'customer_id': ['C001', 'C002'],
      'age': [34, 27],
      'signup_days_ago': [100, 250],
      'avg_purchase_last_30_days': [120.5, 80.0],
      'event_time': [datetime.now(), datetime.now()]
  })

  customer_features.put_record(df.iloc[0].to_dict())
  customer_features.put_record(df.iloc[1].to_dict())
  ```
- Retrieve features for training
  - Use the offline store (Parquet in S3) to get features for model training:
  ```
  query = f"""
  SELECT customer_id, age, signup_days_ago, avg_purchase_last_30_days
  FROM "{feature_group_name}"
  WHERE event_time <= '2026-03-21 00:00:00'
  """
  # Use Athena or Glue to query the offline store
  import boto3
  athena = boto3.client('athena')

  response = athena.start_query_execution(
      QueryString=query,
      QueryExecutionContext={'Database': 'feature_store_database'},
      ResultConfiguration={'OutputLocation': 's3://my-bucket/query-results/'}
  )
  ```
- Use features to train a model
  ```
  import xgboost as xgb

  # Assume df_train contains features retrieved from Feature Store + target column
  X_train = df_train[['age', 'signup_days_ago', 'avg_purchase_last_30_days']]
  y_train = df_train['churn']

  model = xgb.XGBClassifier()
  model.fit(X_train, y_train)
  ```

### Training vs inference pipelines

### Vector databases (for LLMs)

### Data versioning

Data versioning is the process of tracking and storing changes to datasets over time, similar to how Git tracks code.

| Reason                                | Example / Impact                                                                   |
| ------------------------------------- | ---------------------------------------------------------------------------------- |
| **Reproducibility**                   | You can train the same model again and get the same results.                       |
| **Training vs Inference consistency** | Features used in training match what’s served in production.                       |
| **Auditability / Compliance**         | Regulatory requirements often require tracking what data was used for predictions. |
| **Debugging & Experimentation**       | Easy to roll back to a previous dataset if a model fails.                          |
| **Collaboration**                     | Teams can work on different “versions” of datasets without conflict.               |

AWS Options for Data Versioning:
- Object Storage Versioning: Amazon S3 Versioning

### Migrate Data Lake into Data Lakehouse 

You progressively add a transactional table layer, governance, data-quality controls, and better data pipelines on top of your existing object storage.

Steps:
- Inventory the existing lake
- Choose your lakehouse technology 
  - delta lake vs Iceberg
  - Trino vs Athena vs DataBricks
- Design the target architecture
- Rebuild the pipelines
  - you want pipelines that process new or changed data, rather than rebuilding entire tables every night
- Add governance:
  - ownership
  - access control
  - data classification
  - lineage
  - quality

## Governance, Security, Compliance

### HIPAA GDPR CCPA

### Data classification

### Encryption (at rest / in transit)

### Access control (RBAC, ABAC)

### Audit logs

### Data masking / tokenization


## Data Quality & Reliability

### Validation layers

### Observability (metrics, alerts)

### SLAs

### Tools (Great Expectations, Monte Carlo, etc.)



## AI

### How would you design an agentic AI platform?

Separate the platform into planes:
- Experience plane: how users interact with it: API, chat, Notebook?
- Agent runtime plane
- Model plane: model management
- Data plane: agents with capabilities: search , sql, apis
- Memory plane: RAG, Vector Search, Experiment history
- Control plane: Authorization, Authentication, Observability, Augit, Cost management, Governance



## Leadership & Strategy

### “How do you influence product teams?”

- requirements, __goals__, vision: What decisions are you trying to make?
- Translate data work into __product impact__: This ensures your feature usage data is always queryable and doesn’t break dashboards
- Reduce friction: Provide self-service pipeline
- Create opinionated standards: 
- Embed with teams: Join sprint discussions, Sit in product reviews

### “How do you handle disagreements with leadership?”

- Start by understanding why they think differently
- Reframe your argument in business terms: “This isn’t scalable” vs risk, cost, time-to-market
- Bring options, not objections

### “How do you define a data strategy?”

A data strategy is a plan for how your organization uses data to make better decisions and build better products.

- Start with business outcomes (always): What decisions do we want to improve?
- Define the critical data domains: you need the right data
- Build the capabilities (the “how”): ingestion, storage, processing+integration, consumption, governance
- operating model: who owns data, how are data sets created, 
- Establish metrics for the data strategy itself: data quality scores, time to access, 

### Driving architecture decisions

- Anchor every decision in a clear problem: We need to process 5TB/day with low latency and support data science workflows.
- Make trade-offs explicit: Fast to deliver, harder to scale
- Bring structured options: Option B: Azure Databricks (pros/cons): cost, time-to-deliver, risk, long term implications
- Create “default patterns” instead of one-off decisions: All raw data lands in Azure Data Lake Storage Gen2
- Involve stakeholders early: Bring engineers, product, and analytics into the discussion early
- Use data and examples to support decisions
- Document decisions (lightweight but clear)

### Scaling a data platform

### Handling production incidents

### Mentoring teams




## Interview questions

1. Clarify requirements: Scale? latency? users? compliance?
2. Propose architecture: High-level components
3. Dive deeper: Storage, pipelines, compute
4. Discuss tradeoffs: Why this design?
5. Add operational concerns: Monitoring, cost, security

### Design a cloud-based data platform to support analytics and AI/ML for a microservices-based product.

1. Clarify requirements
- Data volume (TB/day? PB?)
- Real-time vs batch needs
- ML use cases (training, inference, both?)
- Compliance requirements (PII, GDPR, etc.)
- Expected users (analysts, data scientists, APIs)
2. High-level architecture
- Ingestion
  - Streaming - kafka, Microservices create events
  - Batch - API, file drops, third party data
  - CDC
  - schema contracts 
- Storage:
  - RAW: S3, partitioned, immutable, versioned
  - Curated: databricks / snowflake i.e. lakehouse vs warehouse
  - Specialized/Final: noSQL, VectorDB, Feature Store
    - Feature Store: 
      - single source of truth for features across an organization
      - Common backends: Redis, DynamoDB, Cassandra
- Processing
  - Batch: spark
  - Stream: kafka streams, flink, windowing, aggregation
- Serving
- Governance & Observability

### Data Governance for one of your projects

It’s about controlling data quality, lineage, security, and accountability across every hop:

1. Start with a Governance Model (not tools): define ownership and rules:
  - Data owners: Who owns each dataset (e.g., product, user, logs)?
  - Data stewards: Who ensures quality and definitions?
  - Policies: 
    - Retention (e.g., Kafka topics kept 7 days, ES indices 30 days)
    - PII handling (masking, encryption)
2. Schema Governance (CRITICAL for Kafka pipelines): Use a schema registry
3. Data Lineage: Know where data came from
   - there are tools (databricks unity calatlog)
   - manually - logging: 
   ```
    lineage = {
      "job": "sales_etl",
      "source": "kafka.sales_topic",
      "target": "prod.sales",
      "timestamp": current_timestamp()
    }
    spark.createDataFrame([lineage]).write.mode("append").saveAsTable("governance.lineage_log")
   ```
     - later store the log file in azure storage account (parquet)
     - Use Azure Synapse Analytics to run SQL queries on it
   - Tag Data with Metadata
4. Data Quality Checks: At ingestion (null checks, field validation), Kafka consumers (schema validation, deduplication), ES (mappings)
5. Access Control & Security: Control who can access to Mongo, ES etc.
6. Data Classification: public, internal, PII
7. Retention & Lifecycle Policies
8. Observability & Auditing
9. Handle Schema Evolution Properly: 
10. Data Contracts

### 

### Design a data platform for a company with microservices and ML use cases.

### “Design a real-time analytics platform.”

### “Build a data platform for an AI-driven product.”

### “Design a multi-tenant data architecture.”

### “How do you handle schema evolution in streaming systems?”

### “How do you optimize query performance in a warehouse?”

### “How do you manage data versioning?”

### “How would you modernize a legacy data warehouse?”

### “How do you choose between tools like Snowflake and Databricks?”

### “Tell me about a time you influenced architecture without authority.”

### “Describe a failure in a data system and what you learned.”

### How would you decide

## My questions

- “What does your current data architecture look like?”
- “What are your biggest bottlenecks today?”
- “How mature is your data governance?”
- “How are AI/ML workloads integrated today?”
- “What decisions do you expect this role to own?”

