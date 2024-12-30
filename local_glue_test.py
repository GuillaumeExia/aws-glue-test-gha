from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql import SQLContext

# Initialize Spark and Glue contexts
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Logging for debugging
print("AWS Glue Local Test Script Started.")

# Sample data for local testing
data = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "city": "Seattle"}
]

# Create a Spark DataFrame from the sample data
print("Creating DataFrame...")
dataframe = spark.createDataFrame(data)

# Show the DataFrame
print("DataFrame Created:")
dataframe.show()

# Perform a simple transformation (filtering)
print("Applying Transformation: Filter rows where age > 30...")
transformed_dataframe = dataframe.filter(dataframe.age > 30)

# Show the transformed DataFrame
print("Transformed DataFrame:")
transformed_dataframe.show()

print("AWS Glue Local Test Script Completed.")