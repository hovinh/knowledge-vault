#### Code Snippets

Create simple local Spark session
```python
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("application name").master("local").getOrCreate()
```

Create local Spark session with config
```python
spark = SparkSession
        .builder
        .config("spark.yarn.queue", queue_name)
        .config("spark.executor.memory", "25g")
        .config("spark.executor.cores", "4")
        .config("spark.executor.memoryOverhead", "976")
        .config("spark.driver.memory", "48g")
        .config("spark.dynamicAllocation.maxExecutors", "30")
        .config("spark.sql.shuffle.partitions", "25g")
        .config("spark.sql.autoBroadcastJoinThreshold", "-1")
        .config("spark.sql.legacy.allowCreatingManagedTableUsingNonemptyLocation", "true")
        .config("spark.sql.crossJoin.enabled", True)
        .config("spark.driver.maxResultSize", "25g")
        .config("spark.rpc.message.maxSize", "2047")
        .config("spark.kryoserializer.buffer.max", "256m")
        .config("spark.files", jks_and_conf_file_path)
        .config("spark.jars", jar_file_path)
        .enableHiveSupport()
        .getOrCreate()
```

Convert SparkDF to PandasDF
```python
from pyspark.sql.functions import col, date_format

def sparkDF_to_pandas_DF(spark_df):
    target_cols = [i for i, j in spark_df.dtypes if j.startswith("date")]
    for col_name in target_cols:
        spark_df = spark_df.withColumn(
            col_name, date_format(col(col_name), "yyyy-MM-dd")
        )
    return spark_df.toPandas()
```

Read parquet file with Spark
```
spark_df = spark.read.parquet(s3_file_path)
```

Create Hive table with Spark
```python
def create_table(spark, table_location, table_name, list_of_tuple, db_name, partition_col=None):
    if partition_col:
        prt_col = ",".join(f"`{x[0]}` {x[1]}" for x in list_of_tuple if x[0] == partition_col)
        columns = ",".join(f"`{x[0]}` {x[1]}" for x in list_of_tuple if x[0] != partition_col)
        create_table_stmt = f"""
            CREATE EXTERNAL TABLE IF NOT EXISTS {db_name}.{table_name} ({columns})
            PARTITIONED BY ({prt_col})
            STORED AS PARQUET
            LOCATION `{table_location}`
        """
    else:
        columns = ",".join(f"`{x[0]}` {x[1]}" for x in list_of_tuple)
        create_table_stmt = f"""
            CREATE EXTERNAL TABLE IF NOT EXISTS {db_name}.{table_name} ({columns})
            STORED AS PARQUET
            LOCATION `{table_location}`
        """

    spark.sql(create_table_stmt)

def refresh_table(spark, table_name, db_name, partitioned=False):
    refresh_table_stmt = f"REFRESH TABLE {db_name}.{table_name}"
    spark.sql(refresh_table_stmt)
    if partitioned:
        repair_table_stmt = f"MSCK REPAIR TABLE {db_name}.{table_name}"
        spark.sql(repair_table_stmt)

def drop_table(spark, table_name, db_name):
    drop_table_stmt = f"DROP TABLE IF EXISTS {db_name}.{table_name}"
    spark.sql(drop_table_stmt)
```

Write to parquet with multiple partitions
```python
# do not have a hive table
spark_df.write.mode("overwrite").partitionBy("ds").parquet("parquet_file_path")

# have a hive table
spark_df.write.format("parquet").mode("overwrite").partitionBy(partition_col).saveAsTable("<db_name>.<table_name>")
```

Read Hive table with Spark & Presto connection via JDBC
```python
jdbc_properties = {
    "user": user_name, 
    "password": password,
    "driver": "io.trino.jdbc.TrinoDriver",
    "SSL": "true",
    }
df_jdbc = spark.read.jdbc(
    url=jdbc_url,
    table=hive_table,
    properties=jdbc_properties,
)
df_jdbc.show()
```

Check the existence of a table
```python
spark.catalog.listTables("<db_name>")
```

Get metadata from a Hive table
```python
table_metadata = spark.sql("DESCRIBE FORMATTED db.table_name")
table_metadata.show(truncate=False)
```



#### Common Issues

| Issue | Solution |
| -------- | -------- |
| `Kryo serialization failed: Buffer overflow. Available: 0...`| Increase `spark.kryoserializer.buffer.max` value|
| | Try a different cluster|
| Data skew that pushed the limit of one core| `df =  df.repartition(5, "column")`|
| | `df =  df.withColumn("salt", F.rand()` then repartition|
| Slow table loading and be used multiple times | `df.persist()` or `df.cache()`|