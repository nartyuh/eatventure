import os
import psycopg2

DATABASE_URL = os.environ['EATVENTURE_DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

conn.close()