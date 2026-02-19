# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC --Now we are creating Catalogs and Schemas in our MetaStore to be managed by Unity Catalog
# MAGIC -- For this project we need to create external tables in Bronze container and managed tables in Silver and Gold Containers.
# MAGIC
# MAGIC CREATE CATALOG IF NOT EXISTS formula1_dev;
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC --if we dont do this, the schema will be created in the default catalog, which is not necessary the last one we created
# MAGIC
# MAGIC USE CATALOG formula1_dev;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS bronze
# MAGIC MANAGED LOCATION "abfss://bronze@databrickscourucexdl.dfs.core.windows.net/"

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS silver
# MAGIC MANAGED LOCATION "abfss://silver@databrickscourucexdl.dfs.core.windows.net/"

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS gold
# MAGIC MANAGED LOCATION "abfss://gold@databrickscourucexdl.dfs.core.windows.net/"

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW SCHEMAS;