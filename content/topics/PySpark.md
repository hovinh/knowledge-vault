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