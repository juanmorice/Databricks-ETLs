# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC --Although this is a Unity Catalog managed table, its data is physically stored as Delta (Parquet) files in the schema’s managed ADLS location (e.g. the silver container). Files are visible at the storage layer but should be accessed only through Databricks.
# MAGIC
# MAGIC
# MAGIC DROP TABLE IF EXISTS formula1_dev.silver.drivers;
# MAGIC CREATE TABLE IF NOT EXISTS formula1_dev.silver.drivers
# MAGIC
# MAGIC AS 
# MAGIC
# MAGIC SELECT
# MAGIC driverId AS driver_id,
# MAGIC driverRef AS driver_ref,
# MAGIC number,
# MAGIC code,
# MAGIC concat(name.forename,'',name.surname) AS name,
# MAGIC dob,
# MAGIC nationality,
# MAGIC current_timestamp() AS ingestion_date
# MAGIC FROM formula1_dev.bronze.drivers;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS formula1_dev.silver.results;
# MAGIC CREATE TABLE IF NOT EXISTS formula1_dev.silver.results
# MAGIC
# MAGIC AS
# MAGIC
# MAGIC SELECT
# MAGIC resultId AS result_id,
# MAGIC raceId AS race_id,
# MAGIC driverId AS driver_id,
# MAGIC constructorId AS constructor_id,
# MAGIC number,
# MAGIC grid,
# MAGIC position,
# MAGIC positionText AS position_text,
# MAGIC positionOrder AS position_order,  
# MAGIC points,
# MAGIC laps,
# MAGIC time,
# MAGIC milliseconds,
# MAGIC fastestLap AS fastest_lap,
# MAGIC rank,
# MAGIC fastestLapTime AS fastest_lap_time,
# MAGIC fastestLapSpeed AS fastest_lap_speed,
# MAGIC statusId AS status_id,
# MAGIC current_timestamp() AS ingestion_date
# MAGIC
# MAGIC FROM formula1_dev.bronze.results;
# MAGIC