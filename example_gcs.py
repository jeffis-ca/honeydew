from honeydew import GcpCloudStorage as GCS
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

g_client = GCS(credential_file=CREDS_FILE, proxy='')
count = 0

print(f"\n# Test {count}: upload_blob()")
local_file = f'{HONEYDEW_OUTPUT_DIR}/{TABLE_ID}.csv.gz'
destination_blob = f'{DATASET_ID}/{TABLE_ID}.csv.gz'
results = g_client.upload_blob(project_id=PROJECT_ID, bucket_id=BUCKET_ID, local_file=local_file, destination_blob=destination_blob)
print(results)
count += 1

print(f"\n# Test {count}: upload_many_blobs()")
local_dir = HONEYDEW_OUTPUT_DIR
destination_dir = DATASET_ID
results = g_client.upload_many_blobs(project_id=PROJECT_ID, bucket_id=BUCKET_ID, local_dir=local_dir, destination_dir=destination_dir)
print(results)
count += 1


print(f"\n# Test {count}: download_blob()")
source_blob_path=f'{DATASET_ID}/{TABLE_ID}.csv.gz'
destination_path = f'{HONEYDEW_OUTPUT_DIR}/{TABLE_ID}.csv.gz'
results = g_client.download_blob(project_id=PROJECT_ID, bucket_id=BUCKET_ID, source_blob_path=source_blob_path, destination_path=destination_path)
print(results)
count += 1


print(f"\n# Test {count}: download_many_blobs()")
blob_prefix = f'{DATASET_ID}/{TABLE_ID}'
destination_dir_path = f'{HONEYDEW_OUTPUT_DIR}/{TABLE_ID}.csv.gz'
results = g_client.download_many_blobs(project_id=PROJECT_ID, bucket_id=BUCKET_ID, blob_prefix=blob_prefix, destination_dir_path=destination_dir_path)
print(results)
count += 1

print(f"\n# Test {count}: delete_blob()")
blob_name = f'{DATASET_ID}/{TABLE_ID}.csv.gz'
results = g_client.delete_blob(project_id=PROJECT_ID, bucket_id=BUCKET_ID, blob_name=blob_name)
print(results)
count += 1

print(f"\n# Test {count}: delete_many_blobs()")
blob_prefix = f'{DATASET_ID}/{TABLE_ID}'
results = g_client.delete_many_blobs(project_id=PROJECT_ID, bucket_id=BUCKET_ID, blob_prefix=blob_prefix)
print(results)
count += 1

print(f"\n# Test {count}: list_blobs()")
blob_prefix = f'{DATASET_ID}/{TABLE_ID}'
results = g_client.list_blobs(project_id=PROJECT_ID, bucket_id=BUCKET_ID, blob_prefix=blob_prefix)
print(results)
count += 1


