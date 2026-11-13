This pipeline will pull FCC consumer complaints, with a special focus on billing and cramming.
In the data pipeline, that data will be loaded into BigQuery on a schedule, and after tested transformations will be pushed to a dashboard.



In this test query, I examine the top 10 states by total number of babies.
The result prints 10 rows of 2 columns, with the states abbreviated, and the total in the second column.
The Python script connects through GoogleCloud to run this query in BigQuery using the bigquery-public-data.usa_names.usa_1910_2013 data.