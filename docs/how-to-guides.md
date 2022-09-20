# MySQL
## Importing a CSV file into MySQL by replacing a table

```Python
from honeydew import mysql_connector

# Instantiate a mysql connector
mysql_conn = MysqlConnector(host = 'mysql.mydomain.com', port = '3306', user = 'my_user', password = 'my_password', allow_local_infile=True)

# Import a CSV file into a table by replacing the content
result = mysql_conn.load_csv_local(
    db_name='db_name',
    table_name='table_name',
    file_name='test.csv',
    write_disposition='WRITE_TRUNCATE'
)

```

## Importing a CSV file into MySQL by appending a table
```Python
from honeydew import db_connector

# Instantiate a mysql connector
mysql_conn = db_connector(db_type = 'mysql', host = 'mysql.mydomain.com', port = '3306', user = 'my_user', password = 'my_password', allow_local_infile=True)

# Import a CSV file into a table by replacing the content
result = mysql_conn.load_csv_local(
    db_name='db_name',
    table_name='table_name',
    file_name='test.csv',
    write_disposition='WRITE_APPEND'
)

```

# GCP
## Instantiating a GCP connector with or without proxy
```Python
from honeydew import GcpConnector

# Instantiate a GCP connector with internet connection behind proxy
g_client = gcp_connector(credential_file='my-secret-credential.json', proxy='http://proxy.mydomain.com:8080')

# Instantiate a GCP connector with direct internet connection
g_client = gcp_connector(credential_file='my-secret-credential.json')
```


## Querying BigQuery table and store the result into a DataFrame
```Python
from honeydew import gcp_connector

# Instantiate a GCP connector with internet connection behind proxy
g_client = gcp_connector(credential_file='my-secret-credential.json', proxy='http://proxy.mydomain.com:8080')
project_id = 'sweet-honeydew-125283'

# Submit a query and store the result into a DataFrame
query = 'SELECT * FROM `sweet-honeydew-125283.universe.galaxies` LIMIT 5'
df = g_client.bq_query_to_dataframe(project_id, query)
print(df.head())
```