# Create a new database connection.
# The connection parameters can be specified as a string:
#     conn = psycopg2.connect("dbname=test user=postgres password=secret")
# or using a set of keyword arguments:
#     conn = psycopg2.connect(database="test", user="postgres", password="secret")
# Or as a mix of both. The basic connection parameters are:

# *dbname*: the database name
# *database*: the database name (only as keyword argument)
# *user*: user name used to authenticate
# *password*: password used to authenticate
# *host*: database host address (defaults to UNIX socket if not provided)
# *port*: connection port number (defaults to 5432 if not provided


import psycopg2

hostname = 'localhost'
database = 'DataWarehousex'
username = 'postgres'
pwd = '1407'
port_id = '5432'

conn = psycopg2.connect(database = database , user = username , password = pwd , port = port_id)
cur = conn.cursor()

query1 = 'show databases'

res1 = cur.execute(query1)
print(res1)


conn.close()