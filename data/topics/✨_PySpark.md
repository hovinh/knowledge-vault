#### Code Snippets

Convert SparkDF to PandasDF
```python
from pyspark.sql.functions import col, date_format

def sparkDF_to_pandas_DF(spark_df):
    target_cols = [i for i, j in spark_df.dtypes if j.startswith('date')]
    for col_name in target_cols:
        spark_df = spark_df.withColumn(
            col_name, date_format(col(col_name), 'yyyy-MM-dd')
        )
    return spark_df.toPandas()
```