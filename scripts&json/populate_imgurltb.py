import os
import psycopg2
import json
from pypostalcode import PostalCodeDatabase

jsonfile = open('yelp_canada_restaurants.json')
# convert jsonfile to dict
restaurants = json.load(jsonfile)

restaurant_ids = []
image_urls = []

# get the postcode database
pcdb = PostalCodeDatabase()

for restaurant in restaurants:
    # check for postcode availability
    postcode = restaurant['location']['zip_code']
    try:
        postcode_info = pcdb[postcode[0:3]]
    except IndexError:
        continue

    restaurant_id = restaurant['id']
    image_url = restaurant['image_url']
    if len(image_url) == 0: image_url = 'https://getdrawings.com/image/restaurant-drawing-52.png'
    restaurant_ids.append(restaurant_id)
    image_urls.append(image_url)

assert len(restaurant_ids) == len(image_urls)

# Connect to Postgres DB
conn = psycopg2.connect(os.environ['EATVENTURE_DATABASE_URL'], sslmode='require')
# Create cursor
cur = conn.cursor()

# check if value is already in table
def check_exist(table, key, value):
    select_query = 'select ' + key + ' from ' + table + " where " + key + " = '" +  value + "'"
    cur.execute(select_query)
    results = cur.fetchall()
    return results

def insert_imageurl(restaurant_id_id, image_url):
    # check if value is already in table
    results = check_exist('restaurants_imageurl', 'restaurant_id_id', restaurant_id_id)
    # if not, insert value into table
    if len(results) == 0:
        insert_query = 'insert into ' + 'restaurants_imageurl' + '(restaurant_id_id, image_url) '
        values = "values ('" + restaurant_id_id + "', " + "'" + image_url + "')"
        cur.execute(insert_query + values)
        return restaurant_id_id
    else:
        return results[0][0]    # return the restaurant_id_id if it is already in the table

i = 0
while i < 1501: # due to Heroku Postgres free plan only allows 10000 rows, we will only insert first 1500 entires 
    insert_imageurl(restaurant_ids[i], image_urls[i])
    i += 1
    print(i)




conn.commit()
conn.close()