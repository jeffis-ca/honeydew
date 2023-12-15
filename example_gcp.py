from honeydew import GcpConnector
from dotenv import load_dotenv
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--proxy', default='')
args = parser.parse_args()

CREDS_FILE = os.environ.get('HONEYDEW_CREDS_FILE')
HONEYDEW_OUTPUT_DIR = os.environ.get('HONEYDEW_OUTPUT_DIR')
PROXY = args.proxy
PROJECT_ID = os.environ.get('HONEYDEW_PROJECT_ID')
DATASET_ID = 'sales'
TABLE_ID = 'fruits'
BUCKET_ID = 'honeydew-test'

g_client = GcpConnector(credential_file=CREDS_FILE, proxy='')

print("\n## Test: bq_query_to_dataframe()")
query = f'SELECT * FROM `{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}` LIMIT 5'
df = g_client.bq_query_to_dataframe(PROJECT_ID, query)
print(df.head())


print("\n## Test: bq_query_non_dql()")
query = f'DROP TABLE IF EXISTS `{PROJECT_ID}.{DATASET_ID}.test1`'
results = g_client.bq_query_non_dql(PROJECT_ID, query)
print(results)

print("\n## Test: bq_export_table_to_gcs()")
gcs_uri = f'gs://{BUCKET_ID}/{DATASET_ID}/{TABLE_ID}.csv.gz'
results = g_client.bq_export_table_to_gcs(project_id=PROJECT_ID, dataset_id=DATASET_ID, table_id=TABLE_ID, gcs_uri=gcs_uri, format='CSV', delimiter=',', enable_compression=True, compression='GZIP', overwrite=True, region='northamerica-northeast1')
print(results)

print("\n## Test: gcs_download_single_file()")
source_blob_path=f'{DATASET_ID}/{TABLE_ID}.csv.gz'
destination_path = f'{HONEYDEW_OUTPUT_DIR}/{TABLE_ID}.csv.gz'
results = g_client.gcs_download_single_file(project_id=PROJECT_ID, bucket_id=BUCKET_ID, source_blob_path=source_blob_path, destination_path=destination_path)
print(results)


print("\n## Test: gcs_download_objects_with_pattern()")
blob_prefix = f'{DATASET_ID}/{TABLE_ID}'
destination_dir_path = f'{HONEYDEW_OUTPUT_DIR}/{TABLE_ID}.csv.gz'
results = g_client.gcs_download_objects_with_pattern(project_id=PROJECT_ID, bucket_id=BUCKET_ID, blob_prefix=blob_prefix, destination_dir_path=destination_dir_path)
print(results)
