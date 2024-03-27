import json
import psycopg2
from psycopg2 import sql
from psycopg2.extras import Json
import sys

class db:
    def __init__(self):
        self.db_params = {
            'dbname': 'lane',
            'user': 'postgres',
            'password': '1234',
            'host': 'localhost',
            'port': '5432'
        }

    def get(self, table, fields="*", conditions=None, orderby=None, limit=None):
        connection = psycopg2.connect(**self.db_params)
        cursor = connection.cursor()

        request = "SELECT " + ", ".join(fields) + " FROM public." + table + (" WHERE " + " AND ".join(conditions)) if conditions else "" + (" ORDER BY " + orderby) if orderby else "" + (" LIMIT " + limit) if limit else "" + ";"
        result = cursor.execute(request)

        cursor.close()
        connection.close()

        return result

# query = "INSERT INTO public.init (source, file_data) VALUES ("");"
# psycopg2.extras.execute_values(cursor, query)
# print(cursor.execute(request))

# connection.commit()

# cursor.close()
# connection.close()

my = db()
my.get(table='users', conditions=['id<>1'], orderby="id DESC", limit=1)
my.get(table='users',fields=['id'], conditions=['id<>1'], orderby="id DESC", limit=1)
my.get(table='users',fields=['id', 'username'], conditions=['id<>1', 'id>5'], orderby="id DESC, username ASC")