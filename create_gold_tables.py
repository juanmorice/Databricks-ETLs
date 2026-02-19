# Databricks notebook source
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS formula1_dev.gold.driver_wins;
# MAGIC CREATE TABLE IF NOT EXISTS formula1_dev.gold.driver_wins
# MAGIC
# MAGIC AS
# MAGIC
# MAGIC SELECT d.name, count(1) as number_of_wins
# MAGIC FROM formula1_dev.silver.drivers d
# MAGIC JOIN formula1_dev.silver.results r
# MAGIC ON (d.driver_id = r.driver_id)
# MAGIC WHERE r.position = 1
# MAGIC GROUP BY d.name;
# MAGIC
# MAGIC