from honeydew import GitConnector
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

g_client = GitConnector()
count = 0
# print("\n# Test {count}: get_file_commit_authors()")
# result = g_client.get_file_commit_authors_to_dataframe(repo_path='/data/vol/codes/src/honeydew')
# print(result)
# count += 1

print("\n# Test {count}: get_file_commit_authors_with_date()")
result = g_client.get_file_commit_authors_with_date(repo_path='/data/vol/codes/src/honeydew')
print(result)
count += 1


# print("\n# Test {count}: search_keywords_in_files_to_dataframe()")
# result = g_client.search_keywords_in_files_to_dataframe(repo_path='/data/vol/codes/src/honeydew', keywords=['pandas', 'google'])
# print(result)
# count += 1

