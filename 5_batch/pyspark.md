export JAVA_HOME=/opt/homebrew/opt/openjdk
export PATH="$JAVA_HOME/bin/:$PATH"
export SPARK_HOME=/opt/homebrew/Cellar/apache-spark/3.5.0/libexec
export PATH="$SPARK_HOME/bin/:$PATH"
export PYTHONPATH="${SPARK_HOME}/python/:$PYTHONPATH"
export PYTHONPATH="${SPARK_HOME}/python/lib/py4j-0.10.9.7-src.zip:$PYTHONPATH"


-- export PATH="/opt/homebrew/Cellar/python@3.12/3.12.2_1/libexec/bin:$PATH"

types.StructType(
    types.StructField('hvfhs_license_num', types.StringType(), True),
    types.StructField('dispatching_base_num', types.StringType(), True),
    types.StructField('pickup_datetime', types.TimestampType(), True),
    types.StructField('dropoff_datetime', types.TimestampType(), True),
    types.StructField('PULocationID', types.IntegerType(), True),
    types.StructField('DOLocationID', types.IntegerType(), True),
    types.StructField('SR_Flag', types.StringType(), True)
)