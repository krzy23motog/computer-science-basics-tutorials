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
      unique_key: id
      strategy: timestamp
      updated_at: updated_at
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

