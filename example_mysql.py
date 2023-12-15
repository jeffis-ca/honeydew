
from honeydew import MysqlConnector, GcpConnector
import os
from dotenv import load_dotenv
load_dotenv()

mysql_conn = MysqlConnector(host = MYSQL_DB_HOST, port = MYSQL_DB_PORT, user = MYSQ_DB_UID, password = MYSQL_DB_PWD)
mysql_conn.load_csv_local(
    db_name='dashboards',
    table_name='test',
    file_name='./test/test.csv',
    write_disposition='WRITE_TRUNCATE'
)