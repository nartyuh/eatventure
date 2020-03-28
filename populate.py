import os
import psycopg2

os.environ['DATABASE_URL'] = 'postgres://vnvriiwrjawvgl:4e22ceb6e4ba83c9881f37c7653a20b919210ebfc3859096e9381b67bc613d64@ec2-18-213-176-229.compute-1.amazonaws.com:5432/danpgrvb6ufbei'

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')