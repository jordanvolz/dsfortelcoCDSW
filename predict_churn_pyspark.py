from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.ml import PipelineModel

spark = SparkSession.builder \
      .appName("Telco Customer Churn") \
      .master("local[*]") \
      .getOrCreate()
  
model = PipelineModel.load("file:///home/cdsw/models/spark") 

features = ["intl_plan", "account_length", "number_vmail_messages", "total_day_calls",
                        "total_day_charge", "total_eve_calls", "total_eve_charge",
                        "total_night_calls", "total_night_charge", "total_intl_calls", 
                        "total_intl_charge","number_customer_service_calls"]

def predict(args):
  account=args["feature"].split(",")
  feature = spark.createDataFrame([account[:1] + map(float,account[1:12])], features)
  result=model.transform(feature).collect()[0].prediction
  return {"result" : result}

