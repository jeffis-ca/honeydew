from honeydew import GcpBigQuery
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

test_project_id = 'bigquery-public-data'
test_dataset_id = 'deps_dev_v1'
test_table_id = 'Advisories'

g_client = GcpBigQuery(credential_file=CREDS_FILE, quota_project=PROJECT_ID, proxy='')
count = 0

# print(f"\n# Test {count}: get_dataset_access()")
# test_project_id = 'bigquery-public-data'
# test_dataset_id = 'deps_dev_v1'
# test_table_id = 'Advisories'
# results = g_client.get_dataset_access(project_id=test_project_id, dataset_id=test_dataset_id)
# print(results)
# count += 1

# print(f"\n# Test {count}: get_table_partition_list()")

# results = g_client.get_table_partition_list(project_id=test_project_id, dataset_id=test_dataset_id, table_id=test_table_id)
# print(results[0:5])
# count += 1

# print(f"\n# Test {count}: get_table_partition_list()")
# results = g_client.get_table_partition_list(project_id=test_project_id, dataset_id=test_dataset_id, table_id=test_table_id)
# print(results[0:5])
# count += 1

# print(f"\n# Test {count}: get_table_row_count()")
# results = g_client.get_table_row_count(project_id=test_project_id, dataset_id=test_dataset_id, table_id=test_table_id)
# print(results)
# count += 1

# print(f"\n# Test {count}: get_table_schema()")
# results = g_client.get_table_schema(project_id=test_project_id, dataset_id=test_dataset_id, table_id=test_table_id)
# print(results)
# count += 1

print(f"\n# Test {count}: get_table_schema_to_dataframe()")
results = g_client.get_table_schema_to_dataframe(project_id=test_project_id, dataset_id=test_dataset_id, table_id=test_table_id)
print(results)
count += 1