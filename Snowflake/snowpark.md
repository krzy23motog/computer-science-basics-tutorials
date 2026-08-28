# Snowpark

Snowpark is a set of libraries and runtimes in Snowflake that deploy and process non-SQL code (python, java, scala) to develop data pipelines, ML models, applications

Spark pipelines require minimal code change

Offers Data frame API (spark) and ML APIs

It also allows to process unstructured ata like image, video, audio from internal and external sources

Schedule snowflake tasks with Python Task API

Snowpark operations are executed lazily on the server. All computations are done on snowflake servers.

### Pros

* Push code to data. If you use 'spark' then you move data to spark.

### Cons

* Move from low-code or SQL approach to engineering with data-frames oriented approach
* Only snowflake. All ML code is contraint with snowpark

### Implementation

Snowpark data-frames are similar to spark data-frames

#### Development environment

On your local computer:
* jupyter notebook on your laptiop
* snowpark session
* trigger transformation on your laptop
* execute it in snowflake

```
from snowflake.snowpark import Session

def InitiateSession(): {
    ....
}
session = InitiateSession()
data_frame_orders = session.table(...)
```

#### Deploy to production

Use UDFs or stored procedures. It will allow you to trigger your code by snoqflake SQL statements or tasks or similar.

```
query = "CREATE STAGE snowpark_udf_stage..."
session.sql( query )

def calculate_1():
  return 123

session.udf.register(
    func = alculate_1,
    ...
)

sql = "SELECT calculate_1()"
```
#### ML with Snowpark

Ingest data from csv to table:

```
from snowflake.snowpark.session import Session
import pandas as pd

housing = pd.read_csv("data/housing.csv")

session = Session.builder.configs(...).create()

session.sql( "CREATE TABLE HOUSING_DATA ...." ).collect()

snowpark_df = session.write_pandas( housing, "HOUSING_DATA")

session.closse()
```


Data pre-processing and model training:
```
import snowflake.snowpark
import sklearn
import pandas
import numpy

session = Session.builder.configs(...).create()

session.add_packages('snowflake-snowpark-python', 'scikit-learn', 'pandas', 'numpy',...)


```
SEE https://github.com/siddd88/snowflake-aws-udemy/blob/main/Section%2013-Snowpark/Machine-Learning/Deploy-HousePricing-Model.ipynb for full example

Serialize model:

Model Inference:

