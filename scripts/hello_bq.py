from google.cloud import bigquery

client = bigquery.Client()

sql = """
SELECT state, SUM(number) AS total_babies
FROM `bigquery-public-data.usa_names.usa_1910_2013`
GROUP BY state
ORDER BY total_babies DESC
LIMIT 10
"""

# Safety cap: BigQuery refuses any query that would bill more than ~1 GB
job_config = bigquery.QueryJobConfig(maximum_bytes_billed=1_000_000_000)

rows = client.query_and_wait(sql, job_config=job_config)

for row in rows:
    print(row.state, row.total_babies)