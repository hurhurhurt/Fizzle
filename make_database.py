import mysql.connector
from mysql.connector import Error


host = 'remotemysql.com'
database = '9lNwJdZh6i'
user = '9lNwJdZh6i'
password = '4mihbbwT4v'
try:
    connection = mysql.connector.connect(host=host,
                                         database=database,
                                         user=user,
                                         password=password)


except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if (connection.is_connected()):
        #cursor.close()
        connection.close()
        print("MySQL connection is closed")