# Databases

## Relational database management systems (rdbms)

### Relational algebra

E.F. Codd proposed the relational Model to model data in the form of relations or tables.

#### What is the Relational Model?

The relational model represents how data is stored in Relational Databases. 
Think of a relation as a file that is formatted in a special way.
Relations are Two-Dimensional Table.
A relational database consists of a collection of tables, each of which is assigned a unique name.

Table: STUDENT

| id  | name  | phone      | age  |
|---- | ----- | ---------- | ---- |
| 1   | Chris | 1234567890 | 40   |
| 2   | Tom   | 1234567891 | 10   |
| 3   | Kate  | 1234567892 | 11   |
| 4   | Mom   | 1234567893 | NULL |

* Attribute: Attributes are the properties that define an entity. e.g.: NAME, ADDRESS

* Column: The column represents the set of values for a particular attribute. The column 'id' = [1,2,3,4]

* Tuple: Each row in the relation is known as a tuple. The above relation contains 4 tuples

* NULL Values: The value which is not known or unavailable is called a NULL value.

[More about relational model](https://www.geeksforgeeks.org/relational-model-in-dbms/?ref=lbp)

[Read about Codd](https://www.ibm.com/ibm/history/ibm100/us/en/icons/reldb/)

[Relational algebra](https://en.wikipedia.org/wiki/Relational_algebra)

Relational algebra mainly provides a theoretical foundation for relational databases and SQL. 
The main purpose of using Relational Algebra is to define operators that transform one or more input relations into an output relation.

Operators on relations:
* selection
* projection
* union
* etc.

[Introduction of Relational Algebra in DBMS](https://www.geeksforgeeks.org/introduction-of-relational-algebra-in-dbms/?ref=lbp)

[Anomalies in Relational Model](https://www.geeksforgeeks.org/anomalies-in-relational-model/?ref=lbp)

### Keys

Keys are one of the basic requirements of a relational database model. 
It is widely used to identify the tuples(rows) uniquely in the table. 

[Keys in Relational Model](https://www.geeksforgeeks.org/types-of-keys-in-relational-model-candidate-super-primary-alternate-and-foreign/?ref=lbp)

### Extended operations

Table: STUDENT

| id  | name  | phone      | age  |
|---- | ----- | ---------- | ---- |
| 1   | Chris | 1234567890 | 40   |
| 2   | Tom   | 1234567891 | 10   |
| 3   | Kate  | 1234567892 | 11   |
| 4   | Mom   | 1234567893 | NULL |

Table: ADDRESS

| id  | street     | city     | zip   | 
|---- | ---------- | -------- | ------| 
| 1   | 1 main     | Boston   | 87654 |
| 2   | 1 broadway | New York | 01234 |

Table: STUDENT_ADDRESS

| student_id | address_id |
| ---------- | ---------- |
| 1          | 1          |
| 2          | 1          |
| 3          | 2          |
| 1          | 1          |

[Extended Operators in Relational Algebra](https://www.geeksforgeeks.org/extended-operators-in-relational-algebra/?ref=lbp)

### RDBMS design

#### Normalization

Database normalization is the process of organizing the attributes of the database to reduce or eliminate data redundancy (having the same data but at different places)

[Introduction of Database Normalization](https://www.geeksforgeeks.org/introduction-of-database-normalization/?ref=lbp)

[Normal Forms in DBMS](https://www.geeksforgeeks.org/normal-forms-in-dbms/?ref=lbp)

### SQL

SQL is a standard database language used to access and manipulate data in databases. SQL stands for Structured Query Language.

#### DDL = data definition language

```
CREATE TABLE student (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    phone VARCHAR(10),
    age int(2)
);
```

#### DML = data manipulation language

INSERT INTO student VALUES ('1','Chris','1234567890', 40);

#### DQL = data query language

SELECT name, age FROM student


[SQL tutorial](https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/?ref=lbp)

#### Joins

[SQL joins](https://www.geeksforgeeks.org/sql-join-set-1-inner-left-right-and-full-joins/?ref=lbp)

#### Group by

[SQL group by](https://www.geeksforgeeks.org/sql-group-by/?ref=lbp)

### Run PostgreSQL

#### run container on your laptop

#### SQL interface

### Transactions and concurrency

Transaction is a set of logically related operations is known as a transaction

[rdbms concurrency control](https://www.geeksforgeeks.org/concurrency-control-in-dbms/?ref=lbp)

#### ACID

* Atomicity defines all the elements that make up a complete database transaction.
* Consistency defines the rules for maintaining data points in a correct state after a transaction.
* Isolation keeps the effect of a transaction invisible to others until it is committed, to avoid confusion.
* Durability ensures that data changes become permanent once the transaction is committed.

[ACID](https://www.geeksforgeeks.org/acid-properties-in-dbms/?ref=lbp)

## Install and run postgres database

We will install:
* postgres rdbms: relational database system
* pgadmin : web based administration tool for the PostgreSQL database

### Install postgres and pgadmin using containers

I assume that you have docker desktop installed.

#### start postgres container:

You will install the following image: https://hub.docker.com/_/postgres

To do that open docker desktop -> images and search for postgres. Find the above docker image, download it and run it.

Start the container with the following settings:
* Name:	postgres
* Port: 	5432:5432
* POSTGRES_PASSWORD: create and remember the password

#### start pgadmin container:

You will install the following image: https://hub.docker.com/r/dpage/pgadmin4/

To do that open docker desktop -> images and search for pgadmin. Find the above docker image, download it and run it.

Start the container with the following settings:
* Name:	 pgadmin
* HOST PORT:	1234:80
* PGADMIN_DEFAULT_EMAIL: your fake email
* PGADMIN_DEFAULT_PASSWORD: create and remember the password

#### connect containers

Both containers work in isolation and do not see each other. They need to be put in the same network. To do that you will use 'docker network' command: create new network and add both containers to it:

In cmd (command line) type the following:

```
docker network ls
docker network create --driver bridge pgnetwork
docker network connect pgnetwork pgadmin
docker network connect pgnetwork postgres
docker network inspect pgnetwork
```

#### connect to database using pgadmin

Now you will use pgadmin web client to connect and manage your postgres database.

1. In your web browser open the following url: http://localhost:1234/browser/. Note that the '1234' is the port you have exposed in the setting of the docker container configuration
2. Login using the credentials specified in your docker container settings
3. Add Server
    1. General
        1. Name: postgres
    2. Connection
        1. Hostname: postgres
	    2. Port: 5432
	    3. database: postgres
	    4. username: postgres
	    5. password: password you have defined

You are connected to the database server

### SQL 

##### create database

Now create your database. In the pgadmin session do the following:

Object Explorer -> Query Tool

```
CREATE DATABASE TomDB ;
```

Refresh your panel to see the created database:

Object Explorer -> Servers -> postgres -> Refresh (right click)

#### connect to the new database

Right click on 'tomdb' database. Select the connection: 'tomdb/postgres@postgres'

#### create table

Object Explorer -> Query Tool

```
CREATE TABLE student (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    phone VARCHAR(10),
    age int
);
```

Execute query

Insert new rows:

```
INSERT INTO student VALUES ('1','Chris','1234567890', 40);
INSERT INTO student VALUES ('2','Tom','1234567891', 10);
INSERT INTO student VALUES ('3','Kate','1234567892', 11);
INSERT INTO student VALUES ('4','Mom','1234567893', NULL);
```

Execute query above

#### Run some queries

Object Explorer -> Query Tool

```
SELECT * FROM student
```

Execute query above

#### Exercise

##### Create more database tables

Create ADDRESS and STUDENT_ADDRESS database tables defined in the first section.

Insert data into them - as above.

##### Run Select and Join queries

* Write and run query to select all rows from ADDRESS table.
* Write query to select only one row from STUDENT table, where name = 'Tom'
* Join STUDENT, STUDENT_ADDRESS and ADDRESS tables to find the address of Tom

##### group by, order by

Use the UFO sightings data fromn https://nuforc.org/webreports/ndxevent.html and insert it into a table. To do that copy and past the following statement and run the query in pgadmin:

```
CREATE TABLE UFO_REPORT (timestamp, city, state, country, shape, duration) AS
SELECT '07/10/23 11:45 PM','Tacoma','WA','USA','Orb','5 mins'
UNION SELECT '07/09/23 11:54 PM','Melbourne','FL','USA','Circle','15 seconds'
UNION SELECT '07/09/23 11:15 PM','North Myrtle Beach','OH','USA','Light','45 Seconds'
UNION SELECT '07/09/23 10:40 PM','Moundridge','KS','USA','Other','3 seconds'
UNION SELECT '07/08/23 11:40 PM','South Saint Paul','MN','USA','Orb','Multiple time at least 4'
UNION SELECT '07/08/23 09:43 PM','Winston salem','NC','USA','Fireball','4.5 minutes'
UNION SELECT '07/08/23 09:40 PM','Crystal River','FL','USA','Fireball','45 seconds to 1 minute'
UNION SELECT '07/08/23 06:20 PM','Des Moines','WA','USA','Light','20 seconds I was driving'
UNION SELECT '07/08/23 03:24 PM','Turku','Varsinais-Suomi','Finland','Triangle','20 second'
UNION SELECT '07/08/23 09:30 AM','coatesville','PA','USA','Light','3 minutes'
UNION SELECT '07/08/23 12:45 AM','Rupert','WV','USA','Light','Maybe 10 to 15 seconds.'
UNION SELECT '07/07/23 10:09 PM','Durham','NC','USA','Light','Under 1 minute'
UNION SELECT '07/07/23 09:40 PM','Commerce','GA','USA','Triangle','5 minutes'
UNION SELECT '07/07/23 09:20 PM','Kansas City','MO','USA','Light','30 mins'
UNION SELECT '07/07/23 08:53 PM','Roseburg','OR','USA','Cylinder','4 minutes'
UNION SELECT '07/07/23 08:33 PM','Hurst','TX','USA','Oval','About 2 minutes'
UNION SELECT '07/07/23 12:36 PM','Proctor','VT','USA','Flash','~1 sec'
UNION SELECT '07/07/23 12:19 PM','Bamber Bridge','Lancashire','United Kingdom','Circle','30 seconds'
UNION SELECT '07/06/23 10:12 PM','Forest City','NC','USA','Orb','45 seconds'
UNION SELECT '07/06/23 10:00 PM','Blaine','MN','USA','Circle','2 min'
UNION SELECT '07/06/23 11:00 AM','Spokane Valley','WA','USA','Other','3 seconds'
UNION SELECT '07/06/23 07:50 AM','Pottstown','PA','USA','Circle','1-2 minutes'
UNION SELECT '07/05/23 11:38 PM','Reno','OH','USA','Light','5-7 seconds'
UNION SELECT '07/05/23 11:20 PM','Boise','ID','USA','Formation','30 seconds'
UNION SELECT '07/05/23 11:00 PM','Milton','VT','USA','Cylinder','15-20 seconds'
UNION SELECT '07/05/23 09:50 PM','Concord','CA','USA','Light',''
UNION SELECT '07/05/23 08:25 PM','Boston','MA','USA','Circle','10 minutes 34 seconds'
UNION SELECT '07/05/23 01:16 PM','San Jacinto','CA','USA','Light','2mins'
UNION SELECT '07/05/23 10:45 AM','Bad axe','MI','USA','Triangle','Five minutes'
UNION SELECT '07/05/23 09:15 AM','Ocean springs','MS','USA','Cylinder','2 minutes'
UNION SELECT '07/05/23 07:38 AM','Grand Prarie','TX','USA','Sphere','1-2 min'
UNION SELECT '07/04/23 11:40 PM','Cheektowaga','NY','USA','Light','1 minute or less'
UNION SELECT '07/04/23 11:30 PM','Tacoma','WA','USA','Circle','About 5 min'
UNION SELECT '07/04/23 10:33 PM','Westland','MI','USA','Changing','15 - 20 minutes'
UNION SELECT '07/04/23 10:30 PM','Red Bluff','CA','USA','Star','12 to 15 minutes'
UNION SELECT '07/04/23 10:19 PM','Macomb','MI','USA','Light','20 minutes'
UNION SELECT '07/04/23 10:12 PM','Mount Holly springs','PA','USA','Other','30 min'
UNION SELECT '07/04/23 10:00 PM','Gresham','OR','USA','Star','5 min or more'
UNION SELECT '07/04/23 10:00 PM','Spokane','WA','USA','Rectangle','est 15-20 mins'
UNION SELECT '07/04/23 09:38 PM','Fresno','CA','USA','Orb','15mins'
UNION SELECT '07/04/23 09:35 PM','Brunswick','MD','USA','Formation','2 or 3 minutes'
UNION SELECT '07/04/23 09:33 PM','Isiolo','Isiolo County','Kenya','Formation','Around a minute'
UNION SELECT '07/04/23 09:30 PM','Tucson','AZ','USA','Unknown','About a minute.'
UNION SELECT '07/04/23 09:30 PM','reno','NV','USA','Light','about 20 minutes'
UNION SELECT '07/04/23 09:25 PM','Mission Viejo','CA','USA','Rectangle','5 seconds'
UNION SELECT '07/04/23 09:21 PM','El Paso','TX','USA','Changing','45 mins'
UNION SELECT '07/04/23 09:14 PM','Pirtsmouth','VA','USA','Circle','10 minutes'
UNION SELECT '07/04/23 09:00 PM','Columbia','NC','USA','Light','5 minutes'
UNION SELECT '07/04/23 08:50 PM','Waynesville','MO','USA','Changing','3 minutes'
UNION SELECT '07/04/23 08:47 PM','Pelham','NY','USA','Other','7 minutes'
UNION SELECT '07/04/23 06:30 PM','Orange','VA','USA','Orb','10 minutes'
UNION SELECT '07/04/23 08:55 AM','sarasota','FL','USA','Circle','7 min'
UNION SELECT '07/03/23 11:00 PM','Lincoln','NE','USA','Chevron','30sec'
UNION SELECT '07/03/23 10:10 PM','Knoxville','TN','USA','Orb','Approximately 1 minute'
UNION SELECT '07/03/23 09:50 PM','Jackson','WI','USA','Orb','10 minutes'
UNION SELECT '07/03/23 09:48 PM','Bellevue','WA','USA','Changing','30 seconds'
UNION SELECT '07/03/23 09:20 PM','Justice','IL','USA','Light','two minutes'
UNION SELECT '07/03/23 08:42 PM','Phoenix','AZ','USA','Star','5:00 minutes'
UNION SELECT '07/03/23 10:26 AM','Timnath','CO','USA','Sphere','40 seconds maybe'
UNION SELECT '07/03/23 05:04 AM','NYC','NY','USA','Disk','1 second'
UNION SELECT '07/03/23 03:45 AM','Portland','OR','USA','Sphere','Brief… very fast.'
UNION SELECT '07/03/23 01:30 AM','Monroe','WA','USA','Light','3-4 sec'
UNION SELECT '07/02/23 09:45 PM','Elizabethtown','PA','USA','Light','30-40 seconds maybe.'
UNION SELECT '07/02/23 09:40 PM','Rapid City','SD','USA','Light','Approx 3 minutes'
UNION SELECT '07/02/23 09:35 PM','Vandergrift','PA','USA','Orb','4 minutes'
UNION SELECT '07/02/23 09:30 PM','St. George','UT','USA','Disk','45 min or so'
UNION SELECT '07/02/23 07:05 PM','Montgomeryville','PA','USA','Sphere','1 to 2 minutes'
UNION SELECT '07/02/23 01:34 PM','Abo ruins near Belen','NM','USA','Circle','2 sec'
UNION SELECT '07/02/23 01:26 AM','Ashford','Kent','United Kingdom','Star','Between 10 and 20minutes.'
UNION SELECT '07/02/23 01:19 AM','Coalinga','CA','USA','Other','2 mins'
UNION SELECT '07/01/23 11:23 PM','Avenal, CA','CA','USA','Rectangle','2 minutes'
UNION SELECT '07/01/23 09:57 PM','Eden Prairie','MN','USA','Cigar','15 seconds'
UNION SELECT '07/01/23 09:33 PM','Shenandoah','VA','USA','Cigar','Less than 1 second'
UNION SELECT '07/01/23 09:13 PM','West Orange','NJ','USA','Formation','5-6 minutes'
UNION SELECT '07/01/23 09:12 PM','Woodridge','IL','USA','Orb','5 minutes. Recording 2 mi'
UNION SELECT '07/01/23 08:57 PM','Milford','IA','USA','Circle','At least 10 mins'
UNION SELECT '07/01/23 08:50 PM','Marion','IL','USA','Orb','5 minutes'
UNION SELECT '07/01/23 11:30 AM','Warsaw','KY','USA','Disk',''
UNION SELECT '07/01/23 10:09 AM','Bogotá','Cundinamarca Department','Colombia','Triangle',''
UNION SELECT '07/01/23 03:30 AM','Approx. 2.5 NM off coast of Sloop Point','NJ','USA','Cube','1 minute'
UNION SELECT '07/01/23 12:07 AM','Killiney','County Dublin','Ireland','Oval','3 minutes'
```

To find out number of ufo sighttings by state run a query:

```
SELECT state, count(*)
FROM ufo_report 
GROUP BY state
```

Write similar query to find out number of ufo sightings by city.

Write query to find out ufo sighttings by shape

What was the state with most 'Fireball' ufo sightings? Hint: use 'ORDER BY' clause.

Write a query to find out all cities with more then one UFO sighting. Hint: GROUP BY ... HAVING COUNT

##### Joins

Run the following query to load the following country data:

```
CREATE TABLE COUNTRY (country, continent) AS
SELECT 'USA','North America'
UNION SELECT 'Finland','Europe'
UNION SELECT 'United Kingdom','Europe'
UNION SELECT 'Kenya','Africa'
UNION SELECT 'Colombia','South America'
UNION SELECT 'Ireland','Europe'
```

Write a query to find out the continent with most UFO sightings. Hint: use JOIN clause 

Write a query to find out all continents with more then 3 'Circle' sightings.

### Updates

CEO of the company you work asked you to change the UFO model in the following way:
* add currency symbol to each country. For USA the currency us 'american dollar' with symbol 'USD'.
* change country symbol from 3 to 2 letters: For 'USA' it should be 'US'

Write a SQL query that will do that:

ALTER TABLE UFO_REPORT ADD COLUMN 'currency'

UPDATE TABLE UFO_REPORT SET country = 'US' WHERE country = 'USA'

Issues:
* to change 'USA' to 'US' - you have to change many rows. This translates to many disk IO operations and will be expensive for large data sets.
* additionally you will need to make this change in all tables that use 3-character country code (the other table is 'COUNTRY')

To solve this data duplication problem you need to normalize the schema.

Database schema is considered the "blueprint" of a database which describes how the data may relate to other tables or other data models. It can be defined as a set of all 'CREATE' statements in the database that creates all database objects (tables, views, functions etc. )

### Database normalization

Database normalization is the process of organizing the attributes of the database to reduce or eliminate data redundancy

[Read about db normalization](https://www.geeksforgeeks.org/introduction-of-database-normalization/?ref=lbp)

[First Normal Form](https://www.geeksforgeeks.org/first-normal-form-1nf/?ref=lbp)

Second Normal Form: https://www.geeksforgeeks.org/second-normal-form-2nf/?ref=lbp

Third Normal Form: https://www.geeksforgeeks.org/boyce-codd-normal-form-bcnf/?ref=lbp

Change the UFO and COUNTRY into 3rd normal form. Create DB tables.

##### Normalization - solution

```
CREATE TABLE UFO_EVENT (timestamp, city_id, shape, duration)
```
| timestamp         | city_id | shape    | duration    |
| ----------------- | ------- | -------- | ----------- |
| 07/09/23 11:54 PM | 1       | 'Circle' | '15 seconds'|
| 07/09/23 11:15 PM | 2       | 'Light'  | '45 Seconds'|
| 07/09/23 10:40 PM | 1       | 'Other'  | '3 seconds' |

```
CREATE TABLE CITY (city_id, city, state, country)
```
| city_id | city        | state | country |
| ------- | ----------- | ----- | ------- |
| 1       | 'Tacoma'    | 'WA'  | 'USA'   |
| 2       | 'Melbourne' | 'FL'  | 'USA'   |


##### Disadvantages of normalization

Performance (need to do joins)

### Issues with rdbms

- Scalability: rdbms usually implements ACID transactions. To run transactions across multiple servers is slow and limits system performance. That is why you should run your database on one server. This means that you can improve the db server performance only by adding more resources to the server i.e. vertical scalability. The issue is that: there is a limit how many CPUs or memory you can add and the cost of very large servers with 100s of CPUs is very expensive.

- Difficult to change schema: systems evolve and you need to modify your database schema. Adding new tables, adding new columns to existing tables or changing the type of columns is possible in rdbms, but expensive: you need to update your applications that use the data, migrate the data to new schemas etc.

- Modelling: modelling data structure like graphs is difficult

- Difficult to operate on very large data sets (1PB), executing joins on 2 or more very large tables.

- Not great at managing binary data types like images, sound, videos

## NoSQL Databases

NoSQL databases (aka "not only SQL") are non-tabular databases and store data differently than relational tables. NoSQL databases come in a variety of types based on their data model. They provide flexible schemas and scale easily with large amounts of data and high user loads.

Usually they do not implement multi-entity transactions but provide better performance, horizontal scalability, flexibility for a given use case.

### Document databases

Databases that store data as semi-structured documents, such as JSON or XML, and can be queried using document-oriented query languages.
    
### Key-value stores 

Databases that store data as key-value pairs, and are optimized for simple and fast read/write operations.

### Graph databases

These databases store data as nodes and edges, and are designed to handle complex relationships between data.

### Exercise

#### Install MongoDB - document database

Open cmd and:

```
# create network
docker network create mongo-network

# install mongo database container
docker run -d -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=pass1 --name mongodb --net mongo-network mongo

# install mongo client: mongo-express
docker run -d -p 8081:8081 -e ME_CONFIG_MONGODB_ADMINUSERNAME=root -e ME_CONFIG_MONGODB_ADMINPASSWORD=pass1 -e ME_CONFIG_MONGODB_SERVER=mongodb --name mongo-express --net mongo-network mongo-express

```

Test: in web browser open: http://localhost:8081 

#### Create mongo database and populate it

Create database: tomek

Create collection: UFO_EVENT

Note: 
* 'collection' is equivalent to a 'table' in rdbms
* you do not need to specify database schema that defines all documents in this collection.

Create document:
```
{
   "timestamp":"07/10/23 11:45 PM",
   "city":"Tacoma",
   "state":"WA",
   "country":"USA",
   "shape":"Orb",
   "duration":"15 min"
}
```

Note:
* mongo is a document database and each document can have different fields. There is no formal schema
* each document must be in .json format

Create another document: some fields are mising:
```
{
   "timestamp":"07/09/23 11:54 PM",
   "city":"Melbourne",
   "state":"FL",
   "country":"USA"
}
```

Create another document: some fields have different name:
{
   "timestamp":"07/09/23 11:15 PM",
   "miasto":"North Myrtle Beach",
   "stan":"FL",
   "panstwo":"USA",
   "ksztalt:": "swiatlo",
   "czas_trwania": '45 Sekund'
}

Create another document: some fields have different type:
```
{
   "timestamp":123456,
   "city":"Moundridge",
   "state":"WA",
   "country":"KS",
   "shape":"Other",
   "duration":3
}
```

Inspect the collection and note that all documents look different.

### More about Mongo

#### Partitioning and Shards

Proper usage of document databases requires partition key. It consists of columns in a collection.

Partition key is used to calculate how to distribute documents between different servers. This is called sharding.

This is the way document databases achieve horizontal scaling.

Drawback: no ACID transactions

#### Schemas

NoSQL databases are sometimes called 'dynamic schema'.

They do not require a database schema and each document in such a database can have different schema.

However, this is bad modelling practice because it makes it difficult for users of these databaes to use them.
Basically the application does not know how to interpret the data.

That is why you should always have a database schema. It defines the contract that applications use to interpret the data.

This schema can be flexible and evolve. The schema evolution is much easier for noSQL vs rdbms
