# DBT

dbt is a transformation workflow

__Dbt, the T in ELT__

dbt provides an easy way to create, transform, and validate the data within a data warehouse

## Concepts

### dbt model

* Represent a data transformation (like performing a cleaning operation)
* Typically written with SQL in .sql files (Python is allowed in newer versions of dbt)
* Usually consists of one SELECT query

```
{{ config(materialized='table') }}
with source_data as (
    select 1 as id
    union all
    select null as id
)
select * from source_data
```

In a real-world project, your models will most likely be dependent on each other, forming some kind of hierarchy. In the data world, this hierarchy is called a Direct Acyclic Graph (DAG) or a lineage graph.

#### Jinja Templating in dbt

To link models we use templating

```
select *
from {{ ref('my_first_dbt_model') }}
where id = 1
```

OR

```
SELECT some_column
 FROM {{ ref("stg_users") }} as su
 JOIN {{ ref("stg_user_groups" )}} as sug
   ON su.a = sug.a

```

Use Jinja to create variables in model files:
```
{% set status = 'active' %}  -- Define a variable

SELECT *
FROM customers
WHERE status = {{ status }};
```

Use conditionals and loops (what a surprise this was!):

```
{% if some_condition %}
 SELECT * FROM test_data
{% else %}
 SELECT * FROM production_data
{% endif %}
```

loop:
```
select
    customer_id,
    {% set amounts = ['product_a', 'product_b', 'product_c'] %}
    {% for column in amounts %}
        {{ column }}{% if not loop.last %},{% endif %}
    {% endfor %}

from {{ ref('customers') }}
```

#### Define constraints and tests

In model_properties.yml create file containing tests:

```
version: 2

models:
 - name: average_diamond_price_per_group
   columns:
     - name: cut
       tests:
         - not_null

```

#### Table types

##### Source tables

tables loaded into the warehouse by an ELT process

Sources are defined in .yml files nested under a sources: key.

```
version: 2

sources:
  - name: jaffle_shop
    database: raw  
    schema: jaffle_shop  
    tables:
      - name: orders
      - name: customers

  - name: stripe
    tables:
      - name: payments
```

Once a source has been defined, it can be referenced from a model using the {{ source() }} function.

```
select
  ...

from {{ source('jaffle_shop', 'orders') }}

left join {{ source('jaffle_shop', 'customers') }} using (customer_id)

```


### snapshots

A way to capture the state of your mutable tables so you can refer to it later.

A dbt snapshot table is a table that lets you track changes to records over time.

slowly changing dimension tables (type 2) using the snapshot feature. 
dbt creates a snapshot table on the first run, and on consecutive runs will check for changed values and update older rows

snapshots/orders_snapshot.yml:
```
snapshots:
  - name: orders_snapshot
    relation: source('jaffle_shop', 'orders')
    config:
      schema: snapshots          
      database: analytics
      unique_key: id                // id column uniquely identifies an order.
      strategy: timestamp           // tells dbt how to detect changes.
      updated_at: updated_at        // column that tells me when this order was last changed is called updated_at
```

example:
```
Imagine your source initially contains:
id | status    | updated_at
---|-----------|-------------------
1  | pending   | 2026-09-01 10:00

Snapshot will look like this:
id | status  | dbt_valid_from       | dbt_valid_to
---|---------|-----------------------|-------------
1  | pending | 2026-09-01 10:00      | NULL

Then someone changes the order:
id | status   | updated_at
---|----------|-------------------
1  | shipped  | 2026-09-02 15:00

Snapshot will look like this:
id | status  | dbt_valid_from  | dbt_valid_to
---|---------|-----------------|-----------------
1  | pending | Sep 1 10:00     | Sep 2 15:00
1  | shipped | Sep 2 15:00     | NULL
```

### Seeds

CSV files with static data that you can load into your data platform with dbt.

seeds/country_codes.csv:
```
country_code,country_name
US,United States
CA,Canada
GB,United Kingdom
...
```

### Data tests

SQL queries that you can write to test the models and resources in your project.

tests/assert_total_payment_amount_is_positive.sql:
```
-- Refunds have a negative amount, so the total amount should always be >= 0.
-- Therefore return records where total_amount < 0 to make the test fail.
select
    order_id,
    sum(amount) as total_amount
from {{ ref('fct_payments') }}
group by 1
having total_amount < 0
```

### Sources

A way to name and describe the data loaded into your warehouse by your Extract and Load tools.

models/<filename>.yml:
```
version: 2

sources:
  - name: jaffle_shop
    database: raw  
    schema: jaffle_shop  
    tables:
      - name: orders
      - name: customers

  - name: stripe
    tables:
      - name: payments
```

## DBT Project

### initialize

```
dbt init dbt_learn
```

### create dbt project profile

You need to create project profile that defines how to connect to databases

### Create models



### dbt Tests

dbt offers the following four built-in tests:

* unique - verify all values are unique
* not_null - check missing
* accepted_values - verify all values are within a specified list, has a values argument
* relationships - verifies a connection to a specific table or column, has to and field arguments

```
dbt test
```

### run and debug

```
dbt run
```

## Example

### Project Structure

```
models/
├── staging/  
│   ├── stg_orders.sql
│   ├── stg_order_items.sql
│   ├── stg_product.sql
│   ├── stg_payment.sql
│   └── stg_address.sql
│
├── dimensions/
│   ├── dim_person.sql
│   ├── dim_product.sql        -- SCD Type 2
│   ├── dim_payment.sql
│   ├── dim_address.sql
│   ├── dim_state.sql
│   └── dim_country.sql
│
├── marts/
│   └── fct_order_items.sql
```

### Staging layer

This model cleans raw data.

```
-- models/staging/stg_orders.sql

SELECT
    order_id,
    customer_id,
    order_date,
    amount
FROM raw.orders
WHERE order_id IS NOT NULL
```

### intermediate models

intermediate models → joins + transformations

### Fact Model: fct_order_items.sql

```
SELECT
    oi.order_item_id,
    o.order_id,
    p.person_id,

    -- SCD product key
    pr.product_key,

    oi.quantity,
    oi.unit_price,

    -- Payment
    pay.payment_id,

    -- Address
    addr.shipping_addr_id,

    o.order_date

FROM {{ ref('stg_order_items') }} oi

JOIN {{ ref('stg_orders') }} o          // relationship
    ON oi.order_id = o.order_id

JOIN {{ ref('dim_person') }} p
    ON o.person_id = p.person_id

-- SCD join (important: business key → versioned dim)
JOIN {{ ref('dim_product') }} pr
    ON oi.product_id = pr.product_id
    AND o.order_date BETWEEN pr.effective_start_dt AND pr.effective_end_dt

JOIN {{ ref('dim_payment') }} pay
    ON o.payment_id = pay.payment_id

JOIN {{ ref('dim_address') }} addr
    ON o.shipping_addr_id = addr.shipping_addr_id
```

### SCD Type 2 Product in dbt

```
{{ config(
    materialized='incremental',
    unique_key='product_key'
) }}

WITH source AS (
    SELECT * FROM {{ ref('stg_product') }}
),

scd AS (

    SELECT
        product_id,                -- business key
        product_name,
        category_id,

        -- SCD fields
        CURRENT_TIMESTAMP AS effective_start_dt,
        NULL AS effective_end_dt,
        TRUE AS is_current

    FROM source

)

SELECT * FROM scd
```

materialized='incremental':
- dbt will not rebuild the whole table every run
- Instead, it:
  - inserts new rows
  - optionally updates existing rows (depending on logic)

unique_key='product_key':
- This tells dbt how to identify duplicates during incremental runs

## deploy

https://medium.com/hashmapinc/deploying-and-running-dbt-on-azure-container-instances-f6136f8ea74c

https://medium.com/@guangx/run-dbt-in-azure-data-factory-a-clean-solution-for-azure-cloud-edddf0c85849

# References

https://www.youtube.com/watch?v=b2nSMPiXdXk&list=PLc2EZr8W2QIBegSYp4dEIMrfLj_cCJgYA&index=1&pp=iAQB


# DBT Interview questions

## What is the difference between ref() and source()?

ref() is used to reference another dbt model. ref() also allows dbt to automatically build the dependency graph and execute models in the correct order.

source() is used to reference a raw/source table defined in your source YAML.

## What is the difference between a view, table, and incremental model in dbt?

Example:
```
{{ config(materialized='table') }}
with source_data as (
    select 1 as id
    union all
    select null as id
)
select * from source_data
```

- view: dbt creates a database view. It doesn't physically store the result as a table.
- table: dbt physically creates a table by running the model query
- incremental: dbt initially creates the entire table, then on subsequent runs processes only the rows you specify as new/changed.

### Incremental Strategies

| Strategy | What it does | Typical use |
|---|---|---|
| `append` | Inserts new rows | Events that are immutable |
| `merge` | Updates matching rows + inserts new rows | Most CDC/upsert use cases |
| `delete+insert` | Deletes matching keys, then inserts new rows | When merge isn't suitable |
| `insert_overwrite` | Replaces affected partitions/data | Partition-based workloads |
| `microbatch` | Processes large time-series data in batches | Very large event/fact tables |


## How does an incremental model work?

```
select
    id,
    customer_id,
    amount,
    updated_at
from {{ source('app', 'orders') }}

{% if is_incremental() %}
    where updated_at > (
        select max(updated_at)
        from {{ this }}
    )
{% endif %}
```

On the first run, is_incremental() is false, so dbt loads everything.

Better example:
```
{{
    config(
        materialized='incremental',
        unique_key='order_id',
        incremental_strategy='merge',
        on_schema_change='sync_all_columns'
    )
}}

with source_orders as (

    select
        order_id,
        customer_id,
        status,
        amount,
        created_at,
        updated_at

    from {{ source('raw', 'orders') }}

    {% if is_incremental() %}

        where updated_at >= (
            select
                dateadd(
                    hour,
                    -2,
                    max(updated_at)
                )
            from {{ this }}
        )

    {% endif %}

),

deduplicated as (

    select *
    from source_orders

    qualify row_number() over (
        partition by order_id
        order by updated_at desc
    ) = 1

)

select
    order_id,
    customer_id,
    status,
    amount,
    created_at,
    updated_at

from deduplicated

```

## What happens when you run dbt run?

- Parses your project.
- Builds the dependency graph.
- Determines which models need to run.
- Compiles Jinja/SQL.
- Executes models in dependency order.
- Creates/updates the configured database objects.

## How do I define db connection to snowflake in dbt?

In dbt, the Snowflake connection is usually defined in profiles.yml

```
pip install dbt-snowflake
```

~/.dbt/profiles.yml:
```
my_dbt_project:
  target: dev

  outputs:
    dev:
      type: snowflake
      account: xy12345.us-east-1
      user: my_user
      password: my_password
      role: TRANSFORMER
      database: ANALYTICS
      warehouse: TRANSFORMING
      schema: DBT_DEV
      threads: 4
```

## What is the purpose of dbt_project.yml?

It's the main configuration file for a dbt project.

It can configure things such as:
- Model materializations
- Model schemas
- Seeds
- Snapshots
- Tests
- Documentation
- Variables

Example:
```
models:
  my_project:
    staging:
      +materialized: view
    marts:
      +materialized: table
```

## How would you design an incremental model that handles updates to existing records?

I'd typically use an incremental strategy such as merge:
```
config:
  materialized: incremental
  unique_key: id
  incremental_strategy: merge

select
    id,
    customer_id,
    status,
    updated_at
from {{ source('app', 'orders') }}

{% if is_incremental() %}
where updated_at >= (
    select max(updated_at)
    from {{ this }}
)
{% endif %}
```

## What's the difference between an incremental model and a snapshot?

An incremental model is primarily about processing less data efficiently.

Incremental → performance / processing strategy

A snapshot is about preserving historical versions of records.

Snapshot → historical record tracking

## Explain how dbt determines model execution order.

dbt builds a DAG (Directed Acyclic Graph) based primarily on dependencies created through ref().

## What happens if you use SELECT * in a dbt model?

It can create several problems: your downstream model may unexpectedly gain a column.
- Unexpected schema changes
- Downstream failures
- Uncontrolled data propagation
- Difficulty understanding model contracts

## How would you optimize a slow dbt project?

First, identify where the time is being spent.

Then I'd look at:
- Incremental models: Avoid rebuilding huge tables unnecessarily.
- Materializations: Don't materialize everything as a table if a view is sufficient.
- SQL optimization: Reduce unnecessary joins, scans, and expensive transformations.
- Warehouse optimization: Consider partitioning, clustering, sorting, distribution, etc., depending on the warehouse.
- DAG structure: Identify models causing large downstream rebuilds.
- Tests: Large tests can themselves become expensive.

## What's the difference between a macro and a model?

- A model produces a database relation such as a table or view.
- A macro is reusable Jinja code that generates SQL or performs logic during compilation. Macros are useful when you have repeated SQL logic across many models. It is like function.

Example of macro:
```
{% macro cents_to_dollars(column_name) %}
    {{ column_name }} / 100.0
{% endmacro %}
```

## What is ephemeral materialization, and when would you use it?

An ephemeral model isn't created as a physical database table/view. 
dbt essentially incorporates its SQL into downstream models, commonly through a CTE.

## Your source table contains 1 billion rows. It receives 5 million new/updated rows every day. How would you build the dbt model?

I would probably use an incremental model rather than rebuilding 1 billion rows every day:
```
{{ config(
    materialized='incremental',
    unique_key='order_id',
    incremental_strategy='merge'
) }}

select
    order_id,
    customer_id,
    status,
    amount,
    updated_at
from {{ source('app', 'orders') }}

{% if is_incremental() %}

where updated_at >= (
    select max(updated_at)
    from {{ this }}
)

{% endif %}
```

I'd also consider:
- Partitioning by an appropriate date column.
  ```
  {{ config(
      materialized='incremental',
      partition_by={
        "field": "event_date",
        "data_type": "date",
        "granularity": "day"
      }
  ) }}

  select
      event_id,
      event_date,
      user_id,
      event_type
  from {{ ref('events') }}
  ```
- Clustering/sorting by commonly filtered columns.
- Handling late-arriving records.
  - intentianally process 2 hours earlier:
  ```
  where updated_at >= (
    select dateadd(
        hour,
        -2,
        max(updated_at)
    )
    from {{ this }}
  )
  ```
- Handling duplicate events.
  - deduplicate before the merge.
- Choosing an appropriate incremental strategy for the warehouse.
- Periodically doing a full refresh if necessary.
- Monitoring whether the incremental filter is actually reducing scanned data.

## How do you handle continuously arriving data?

You might run dbt every 5 minutes or better:  orchestration.


