from honeydew import GcpTranslate
from dotenv import load_dotenv
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--proxy', default='')
args = parser.parse_args()

CREDS_FILE = os.environ.get('HONEYDEW_CREDS_FILE')
HONEYDEW_OUTPUT_DIR = os.environ.get('HONEYDEW_OUTPUT_DIR')
PROXY = args.proxy

g_client = GcpTranslate(credential_file=CREDS_FILE, proxy='')
count = 0

print(f"\n# Test {count}: translate_text()")
results = g_client.translate_text(text='How are you?', target_language='id')    
print(results)
count += 1



