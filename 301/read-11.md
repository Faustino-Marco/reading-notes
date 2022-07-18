# Mongo and Mongoose

## Reading

[nosql vs sql](https://www.thegeekstuff.com/2014/01/sql-vs-nosql-db/?utm_source=tuicool)

SQL vs NoSQL Differences

- SQL
  - Primarily Relational Databases
  - table based
  - predefined schema
  - vertically scalable
    - increase Horsepower of hardware
  - use SQL(Structured Query Language)
  - eg MySQL, Oracle, Sqlite, Postgres, MS-SQL
- NoSQL
  - Non-relational Databases
  - Document Based
    - key-value pairs
    - documents
    - graph databases
    - wide-column stores w/ no standard schema
  - dynamic schema
    - for unstructured data
  - horizontally scalable
    - increasing DB servers in pool of resources to reduce the load
  - UnQL (Unstructured Query Language)
    - syntax varies from DB to DB
  - eg: MongoDB, BigTable, Redis, RavenDb, Cassandra, Hbase, Neo4j, CouchDb

1. What does SQL stand for?
  - Structured Query Language
2. What is a relational database?
  - data related to specifically structured schema from one table to another
3. What type of structure does a relational database work with?
  - tables mostly, if not always
4. What is a 'schema'?
  - basically parameters for the data
5. What is a NoSQL database?
  - data that is held in a less strictly formatted manner, k-v pairs, docs, graphs, etc.
6. How does it work?
  - accessed through relevant language to extract and manipulate data
7. What is inside of a Mongo database?
  - objects and docs full of data 
8. Which is more flexible - SQL or MongoDB? Why?
  - MongoDB, non-relational DB's are more flexible


## Videos

[sql vs nosql](https://www.youtube.com/watch?v=ZS_kXvOeQ5Y)

1. What does SQL stand for?
  - Structured Query Language
    - used to write queries
    - syntax/keywords & data/params
    - queries, extracting, manipulating ETL etc
2. What is a relational database?
  - Table-based, strticly organized with parameters
  - tables, fields (columns), records (rows)
  - precise 'schema'
    - all records must adhere to db schema
    - allows woking with multiple related tables
      - types of relation
        - many to many
        - one to one
3. What type of structure does a relational database work with?
  - tables (see above)
4. What is a 'schema'?
  - see above
5. What is a NoSQL database?
  - non-relational DB
6. How does it work?
  - documents stored in db
7. What is inside of a Mongo Database?
  - Database
    - Collections
      - Documents
8. Which is more flexible - SQL or MongoDB? Why?
  - MongoDB, can have data without adhering to strict schema, but depends on how you look at it
    - can be horizontally scaled
  - SQL uses relational db format to be potentially more efficient
  - faster queries
9. What is the disadvantage of a NoSQL database?
  - no relations, must query manually
  - all info in one place
    - may need extra docs/objects for separate data,
    - could be duplicate data stored
  - NoSQL not ideal for frquently updated data
  - good performance for mass read/write, though

## Bookmark and Review

[Mongoose API](https://mongoosejs.com/docs/api.html#Model)
[React Router](https://reactrouter.com/web/api/BrowserRouter)

## Things I want to know more about
- which aspects of enterprise typically use sql or nosql databases? The video says typically both are used in business and modern apps.
  - clearly scalability and accessibility are important factors, but I'm curious to hear specific examples. 