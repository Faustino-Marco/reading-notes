# Introduction to SQL

## Lesson 1 
- SELECT statements retrieve data
- get data for a couple columns (properties) with all rows (instances)
```
SELECT column, another_column, …
FROM mytable;
```
- this results in a two dimensional set of rows and columns
- same table, but only requested rows/columns
- `SELECT * \n FROM mytable` gets everything

## Lesson 2 - Queries with Constraints pt 1
- `WHERE` clause in query
  - applied to each row of data by checking specific column values
  - `AND/OR` another_condition
- `col_name != 4`
- `BETWEEN ... AND ...`
- `NOT BETWEEN ... AND ...`
- `IN (...)`
- `NOT IN (...)`

## Lesson 3 - Queries with Constraints pt 3
- operators
  - `=`, `!=`, `<>`
    - case sensitive exact string comparison
  - `LIKE`, `NOT LIKE`
    - case insensitive
    - `%...%` only with like/not like
      - matches sequence of zero or more chars
    - `_`
      - match a single char (`AN_` matches 'and' but not 'an')
    - `IN (...)`, `NOT IN (...)`

## Lesson 4 - Filtering and Sorting Query Results
- DISTINCT keyword
  - blindly remove duplicate rows
  - `SELECT DISTINCT`
- ORDER BY clause
  - `ORDER BY <column> ASC/DESC;`
- LIMIT & OFFSET clause
  - reduce num of rows, and specifically where to begin counting rows from
  - `LIMIT num_limit OFFSET num_offset`

## Lesson 5 - Simple SELECT Queries
```
SELECT query
SELECT column, another_column, …
FROM mytable
WHERE condition(s)
ORDER BY column ASC/DESC
LIMIT num_limit OFFSET num_offset;
```

## Lesson 6 - Multi-table queries with JOINs
- Database Normalization
  - minimize duplicate data in any single table
  - allows for data in database to grow independently of each other
- JOIN clause
  - INNER JOIN
```
SELECT column, another_table_column, …
FROM mytable
INNER JOIN another_table 
    ON mytable.id = another_table.id
WHERE condition(s)
ORDER BY column, … ASC/DESC
LIMIT num_limit OFFSET num_offset;
```
- shared key definted by the ON constraint

## Lesson 13 - Inserting Rows
- Schema
  - structure of each table
  - year must be int
  - title must be string
- INSERT
  - specify table to append
  - values in list to add
- having hard coded default values makes it easier later
```
INSERT INTO mytable
(columns to update)
VALUES (values in correlation to above)
```

## Lesson 14 - Updating Rows
- UPDATE
  - datatypes must match original
```
UPDATE mytable
SET column = value_or_expr,
WHERE condition
```

## Lesson 15 - Deleting Rows
- DELETE FROM mytable
- Where condition

## Lesson 16 - Creating Tables
```
CREATE TABLE IF NOT EXISTS mytable (
    column DataType TableConstraint DEFAULT default_value,
    another_column DataType TableConstraint DEFAULT default_value,
    …
);
```
- support for int, bool, float, double, real, character, varchar, text, date, datetime, blob
- constraints
  - primary key
    - values in this col are unique
  - autoincrement
    - value automatically filled in and inc'd with each row insertion (not always supported)
  - unique
    - values in this col must be unique
  - not null
  - check (expression)
  - foreign key
    - consistency check to verify match with another value in a column in another table
```
CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    director TEXT,
    year INTEGER, 
    length_minutes INTEGER
);
```

## Lesson 17 - Altering Tables
- ALTER TABLE mytable
```
ALTER TABLE mytable
ADD column DataType OptionalTableConstraint 
    DEFAULT default_value;
```
- drop columns
```
ALTER TABLE mytable
DROP column_to_be_deleted;
```
- ALTER TABLE mytable
- RENAME TO new_table_name;

## Lesson 18 - Drop Table
- DROP TABLE IF EXISTS mytable