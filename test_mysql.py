
from honeydew import mysql_connector, gcp_connector
import os
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_UID = os.environ.get('DB_UID')
DB_PWD = os.environ.get('DB_PWD')

mysql_conn = MysqlConnector(host = DB_HOST, port = DB_PORT, user = DB_UID, password = DB_PWD)
mysql_conn.load_csv_local(
    db_name='dashboards',
    table_name='test',
    file_name='/apps/test/test.csv',
    write_disposition='WRITE_TRUNCATE'
)