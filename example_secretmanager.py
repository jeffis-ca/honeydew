from honeydew import GcpSecretManager
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

g_client = GcpSecretManager(credential_file=CREDS_FILE, proxy='')

count = 0
print(f"\n# Test {count}: list_secret()")
secret_list = g_client.list_secret(project_id=PROJECT_ID)
print(secret_list)
count += 1


