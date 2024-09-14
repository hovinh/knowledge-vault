
<img src="https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6a563e6f-db16-4e98-8713-d930b43b71b3_1536x1536.gif" alt="SQL Query" style="width:100%;">

#### Code Snippets

Check underlying table of a view
```sql
SHOW CREATE VIEW db_name.table_name
```

Reading query plan
```sql
EXPLAIN ANALYZE query
```

#### Writing Effective Query

1. Query using partition: ensure partitioned columns is used in query: WHERE clause, JOINS.
2. Joins:
    1. Join from larger table (subquery) to smaller table (subquery)
    2. Filter data as early as possible (within table rather than after a join).
        Example:  
        ```sql
            (SELECT * FROM a WHERE a.col != null) join b 
        ```
    3. Keep Joins simpler, avoid expressions in JOIN clause.
    4. Always join 2 tables based on partition columns first, then go for other (partitionless) columns.
    5. Avoid CROSS JOIN as it multiplies the total number of records.
3. WITH clause - Sub query refactoring: repeated subqueries/nested subqueies can be refactored into a WITH clause.
4. SELECT: Avoid *, only select the columns you are interested in. Choosing to many columns slow down query processing.
5. AGGREGATE function: faster way of accessing aggregated data by using Presto's native syntax, instead of traditional SQL Query. Example: MAX(column_name, X) extracts the top X elements of a particular column in table.
6. GROUP BY: Improve the performance by ordering a list of fields within the GROUP BY in an order of low to high of number of unique values (cardinality).