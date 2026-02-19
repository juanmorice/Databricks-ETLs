# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC --We are going to import a table in our Catalog, inside the Bronze schema. In order to do this, we need to define the table characteristics. Then, we specified the path where the data is going to be populated from.
# MAGIC -- External table: dropping the table in Databricks removes only the metadata.
# MAGIC -- The underlying data in the Data Lake is not deleted.
# MAGIC
# MAGIC DROP TABLE IF EXISTS formula1_dev.bronze.drivers;
# MAGIC CREATE TABLE IF NOT EXISTS formula1_dev.bronze.drivers
# MAGIC (
# MAGIC driverId INT,
# MAGIC driverRef STRING,
# MAGIC number INT,
# MAGIC code STRING,
# MAGIC name STRUCT<forename: STRING, surname: STRING>,
# MAGIC dob DATE,
# MAGIC nationality STRING,
# MAGIC url STRING
# MAGIC )
# MAGIC USING json 
# MAGIC OPTIONS (path "abfss://bronze@databrickscourucexdl.dfs.core.windows.net/drivers.json")
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DROP TABLE IF EXISTS formula1_dev.bronze.results;
# MAGIC CREATE TABLE IF NOT EXISTS formula1_dev.bronze.results
# MAGIC (
# MAGIC resultId INT,
# MAGIC raceId INT,
# MAGIC driverId INT,
# MAGIC constructorId INT,
# MAGIC number INT,
# MAGIC grid INT,
# MAGIC position INT,
# MAGIC positionText STRING,
# MAGIC positionOrder INT,  
# MAGIC points FLOAT,
# MAGIC laps INT,
# MAGIC time STRING,
# MAGIC milliseconds INT,
# MAGIC fastestLap INT,
# MAGIC rank INT,
# MAGIC fastestLapTime STRING,
# MAGIC fastestLapSpeed FLOAT,
# MAGIC statusId INT
# MAGIC )
# MAGIC USING json 
# MAGIC OPTIONS (path "abfss://bronze@databrickscourucexdl.dfs.core.windows.net/results.json")
# MAGIC