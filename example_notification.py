from honeydew import Notification
from dotenv import load_dotenv
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--proxy', default='')
args = parser.parse_args()

CREDS_FILE = os.environ.get('HONEYDEW_CREDS_FILE')
HONEYDEW_OUTPUT_DIR = os.environ.get('HONEYDEW_OUTPUT_DIR')
PROXY = args.proxy

g_client = Notification(proxy='')
count = 0

print(f"\n# Test {count}: send_google_chat_message()")
webhook_url = ''
results = g_client.send_google_chat_message(webhook_url=webhook_url, message='Hello from Honeydew')
print(results)
count += 1



