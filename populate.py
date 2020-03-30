import os
import psycopg2
import json
import re
import hashlib
from pypostalcode import PostalCodeDatabase

#################################################################################
#################################################################################
#                         Parsing the data into attributes                      # 
#################################################################################
#################################################################################
jsonfile = open('yelp_canada_restaurants.json')
# convert jsonfile to dict
restaurants = json.load(jsonfile)

# Restaurant
restaurant_ids = []
restaurant_names = []
price_ranges = []
# foreign key address_id is part of restaurant

# RatingStats
rating_ids = []
aggregate_ratings = []
num_of_reviewss = []

# BestSellingItem
best_selling_item_ids = []
item_names = []
item_descriptions = []

# Coordinate
coordinate_ids = []
longitudes = []
latitudes = []

# Address
# Country
country = 'Canada' # only support canada at this time
# Postcode
postcodes = []
# city
cities = []
# province
provinces = []
# address_id
address_ids = []
# street_num
street_nums = []
# street_name
street_names = []

# get the postcode database
pcdb = PostalCodeDatabase()

for restaurant in restaurants:
    # Postcode
    postcode = restaurant['location']['zip_code']
    try:
        postcode_info = pcdb[postcode[0:3]]
    except IndexError:
        continue
    city = postcode_info.city
    province = postcode_info.province

    # Address
    address = restaurant['location']['address1']
    try:
        address_id = hashlib.sha1((address + postcode).encode('utf-8')).hexdigest()
    except TypeError:
        address_id = hashlib.sha1(('' + postcode).encode('utf-8')).hexdigest()
    try:
        split_string = address.split(' ')
        street_num = []
        street_name = []
        for str_item in split_string:
            if '-' in str_item:
                street_num.append(str_item)
                street_num.append(' ')
            elif str_item.isdigit():
                street_num.append(str_item)
                street_num.append(' ')
            else:
                street_name.append(str_item)
                street_name.append(' ')
        street_num = ''.join(street_num).strip()
        street_name = ''.join(street_name).strip()
    except:
        street_num = ''
        street_name = ''

    # Restaurant
    restaurant_id = restaurant['id']
    restaurant_name = restaurant['name']
    try:
        price_range = restaurant['price']
    except KeyError:
        price_range = 'no info'

    # RatingStats
    rating_id = restaurant_id
    aggregate_rating = restaurant['rating']
    num_of_reviews = restaurant['review_count']

    # BestSellingItem
    best_selling_item_id = restaurant_id
    item_name = 'no info'
    item_description = 'no info'

    # Coordinate
    coordinate_id = restaurant_id
    longitude = restaurant['coordinates']['longitude']
    latitude = restaurant['coordinates']['latitude']

    postcodes.append(postcode)
    cities.append(city)
    provinces.append(province)
    street_nums.append(street_num)
    street_names.append(street_name)
    restaurant_ids.append(restaurant_id)
    restaurant_names.append(restaurant_name)
    price_ranges.append(price_range)
    address_ids.append(address_id)
    rating_ids.append(rating_id)
    aggregate_ratings.append(aggregate_rating)
    num_of_reviewss.append(num_of_reviews)
    best_selling_item_ids.append(best_selling_item_id)
    item_names.append(item_name)
    item_descriptions.append(item_description)
    coordinate_ids.append(coordinate_id)
    longitudes.append(longitude)
    latitudes.append(latitude)

assert len(postcodes) == len(cities) == len(provinces) == len(street_nums) == len(street_names)
assert len(street_names) == len(restaurant_ids) == len(restaurant_names) == len(price_ranges)
assert len(price_ranges) == len(address_ids) == len(rating_ids) == len(aggregate_ratings)
assert len(aggregate_ratings) == len(num_of_reviewss) == len(best_selling_item_ids) == len(item_names)
assert len(item_names) == len(item_descriptions) == len(coordinate_ids) == len(longitudes) == len(latitudes)


[print(tpl) for tpl in list(zip(restaurant_ids, restaurant_names, price_ranges, address_ids))]
# [print(tpl) for tpl in list(zip(rating_ids, aggregate_ratings, num_of_reviewss))]
# [print(tpl) for tpl in list(zip(best_selling_item_ids, item_names, item_descriptions))]
# [print(tpl) for tpl in list(zip(coordinate_ids, longitudes, latitudes))]
# [print(tpl) for tpl in list(zip(address_ids, street_nums, street_names, postcodes))]
# [print(tpl) for tpl in list(zip(postcodes, cities, provinces))]



#################################################################################
#################################################################################
#                          Running the insertion queries                        # 
#################################################################################
#################################################################################

# Connect to Postgres DB
conn = psycopg2.connect(os.environ['EATVENTURE_DATABASE_URL'], sslmode='require')

# locations
country_tb = 'locations_country'
postcode_tb = 'locations_postcode'
address_tb = 'locations_address'

# restaurants
restaurant_tb = 'restaurants_restaurant'
ratingstats_tb = 'restaurants_ratingstats'
coordinates_tb = 'restaurants_coordinates'
best_selling_item_tb = 'restaurants_bestsellingitem'

# initialize cursor
cur = conn.cursor()

# check if value is already in table
def check_exist(table, key, value):
    select_query = 'select ' + key + ' from ' + table + " where " + key + " = '" +  value + "'"
    cur.execute(select_query)
    results = cur.fetchall()
    return results

def insert_country(country):
    # check if value is already in table
    results = check_exist(country_tb, 'country_name', country)
    # if not, insert value into table
    if len(results) == 0:
        insert_query = 'insert into ' + country_tb + '(country_name)' + " values ('" + country + "')"
        cur.execute(insert_query)

def insert_postcode(postcode, city, state, country):
    # check if value is already in table
    results = check_exist(postcode_tb, 'postcode', postcode)
    if len(results) == 0:
        insert_query = 'insert into ' + postcode_tb +  '(postcode, city, state, country_id) ' + "values (" + "'" + postcode + "'," + "'" + city + "'," + "'" + state + "'," + "'" + country + "'" + ")"
        cur.execute(insert_query)

def insert_address(address_id, street_num, street_name, postcode):
    # check if value is already in table
    results = check_exist(address_tb, 'address_id', address_id)
    if len(results) == 0:
        insert_query = 'insert into ' + address_tb + '(address_id, street_num, street_name, postcode_id) ' + "values (" + "'" + address_id + "'," + "'" + street_num + "'," + "'" + street_name + "'," + "'" + postcode + "'" + ")"
        cur.execute(insert_query)

# insert Canada to country table
insert_country('Vietnam')
insert_postcode('700000', 'Ho Chi Minh', 'Ho Chi Minh', 'Vietnam')
address = '123 Huy Tran, 700000'
address_id = hashlib.sha1((address).encode('utf-8')).hexdigest()
insert_address(address_id, '123', 'Huy Tran', '700000')



cur.execute('select * from ' + country_tb)
rows = cur.fetchall()
print(rows)
cur.execute('select * from ' + postcode_tb)
rows = cur.fetchall()
print(rows)
cur.execute('select * from ' + address_tb)
rows = cur.fetchall()
print(rows)

conn.commit()


conn.close()
