from honeydew import gcp_connector
import os
CREDENTIAL_FILE = os.environ.get('CREDENTIAL_FILE')
GCP_PROXY = os.environ.get('GCP_PROXY')
GCP_PROJECT_ID = os.environ.get('GCP_PROJECT_ID')
GCP_DATASET_ID = os.environ.get('GCP_DATASET_ID')
GCP_BUCKET_ID = os.environ.get('GCP_BUCKET_ID')
GCP_TABLE_ID = os.environ.get('GCP_TABLE_ID')

g_client = GcpConnector(credential_file='/creds/pluto.json', proxy=GCP_PROXY)
project_id = GCP_PROJECT_ID
dataset_id = GCP_DATASET_ID
bucket_id = GCP_BUCKET_ID
table_id = GCP_TABLE_ID

print("\n## Test: bq_query_to_dataframe()")
query = 'SELECT * FROM `{project}.{dataset}.{table}` LIMIT 5'.format(project=project_id, dataset=dataset_id, table=table_id)
df = g_client.bq_query_to_dataframe(project_id, query)
print(df.head())


print("\n## Test: bq_query_non_dql()")
query = 'DROP TABLE IF EXISTS `{project}.{dataset}.test1`'.format(project=project_id, dataset=dataset_id)
results = g_client.bq_query_non_dql(project_id, query)
print(results)

print("\n## Test: bq_export_table_to_gcs()")
gcs_uri = 'gs://{bucket}/test/tickets-*.csv.gz'.format(bucket=bucket_id)
results = g_client.bq_export_table_to_gcs(project_id=project_id, dataset_id=dataset_id, table_id=table_id, gcs_uri=gcs_uri, format='CSV', delimiter=',', enable_compression=True, compression='GZIP', overwrite=True, region='northamerica-northeast1')
print(results)

print("\n## Test: gcs_download_single_file()")
source_blob_path='test/tickets-000000000000.csv.gz'
destination_path = '/creds/test/tickets-000000000000.csv.gz'
results = g_client.gcs_download_single_file(project_id=project_id, bucket_id=bucket_id, source_blob_path=source_blob_path, destination_path=destination_path)
print(results)


print("\n## Test: gcs_download_objects_with_pattern()")
blob_prefix = 'test/tickets-'
destination_dir_path = '/creds/test'
results = g_client.gcs_download_objects_with_pattern(project_id=project_id, bucket_id=bucket_id, blob_prefix=blob_prefix, destination_dir_path=destination_dir_path)
print(results)
