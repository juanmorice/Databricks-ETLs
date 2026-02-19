# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC --Creating external locations to the storage account containers. This external location give us access to the storage account linked to the MetaStore by using the storage credential created before in Catalog. This Storage credential is used to establish a relationship between our MetaStore and the Access Conector (created to allow the access to the Storage Account like Blob Storage Contributor).
# MAGIC
# MAGIC --This would be like:
# MAGIC
# MAGIC -- MetaStore -> Unity Catalog -> Storage Credential ----> Access Conector -> Storage Account
# MAGIC
# MAGIC
# MAGIC --We need an external location declaration for each container in the storage account.
# MAGIC --Remember that it is possible to create the external location in Catalog tab, by using UI options, but here we are doing it by using SQL.
# MAGIC
# MAGIC
# MAGIC CREATE EXTERNAL LOCATION IF NOT EXISTS external_location_bronze_container
# MAGIC URL "abfss://bronze@databrickscourucexdl.dfs.core.windows.net/"
# MAGIC WITH (
# MAGIC STORAGE CREDENTIAL `databrickcourse-ext-storage-credential`
# MAGIC )
# MAGIC ;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC DESC EXTERNAL LOCATION external_location_bronze_container

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE EXTERNAL LOCATION IF NOT EXISTS external_location_silver_container
# MAGIC URL "abfss://silver@databrickscourucexdl.dfs.core.windows.net/"
# MAGIC WITH (
# MAGIC STORAGE CREDENTIAL `databrickcourse-ext-storage-credential`
# MAGIC )
# MAGIC ;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE EXTERNAL LOCATION IF NOT EXISTS external_location_gold_container
# MAGIC URL "abfss://gold@databrickscourucexdl.dfs.core.windows.net/"
# MAGIC WITH (
# MAGIC STORAGE CREDENTIAL `databrickcourse-ext-storage-credential`
# MAGIC )
# MAGIC ;