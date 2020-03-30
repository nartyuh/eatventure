import os
import psycopg2
import json
from pypostalcode import PostalCodeDatabase

conn = psycopg2.connect(os.environ['EATVENTURE_DATABASE_URL'], sslmode='require')

jsonfile = open('canada_restaurants.json')
# convert jsonfile to dict
json = json.load(jsonfile)

# Restaurant
restaurant_ids = []
restaurant_names = []
price_ranges = []
address_ids = []

# RatingStats
rating_ids= []
aggregate_ratings = []
num_of_reviewss = []

# BestSelling
best_selling_item_ids = []
item_names = []
item_descriptions = []

# Coordinate
coordinate_ids = []
longitudes = []
latitudes = []

# Address
## Country
countries = ['Canada']
## Postcode
postcodes = []
## city
cities = []
## province
provinces = []
## street_num
street_nums = []
## street_name
street_names = []

# get the postcode database
pcdb = PostalCodeDatabase()

# start the fun baby!!!!!
for datum in json:

    # getting the restaurant field    
    restaurant = datum['restaurant']

    # Country
    country = 'Canada'

    # Postcode
    postcode = restaurant['location']['zipcode']
    postcode_info = pcdb[postcode[0:3]]
    city = postcode_info.city
    province = postcode_info.province

    # Address
    address = restaurant['location']['address']
    street_num = 'not yet parsed'
    street_name = 'not yet parsed'

    # Restaurant 
    restaurant_id = restaurant['id']
    restaurant_name = restaurant['name']
    price_range = restaurant['price_range']
    address_id = 0

    # RatingStats
    rating_id = restaurant_id
    aggregate_rating = restaurant['user_rating']['aggregate_rating']
    num_of_reviews = restaurant['user_rating']['votes']

    # BestSellingItem
    best_selling_item_id = restaurant_id
    item_name = 'no info'
    item_description = 'no info'

    # Cooridinate
    coordinate_id = restaurant_id
    longitude = restaurant['location']['longitude']
    latitude = restaurant['location']['latitude'] 

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


# remove duplicates
'''
list_of_lists = [postcodes, cities, provinces, street_nums, street_names,
                 restaurant_ids, restaurant_names, price_ranges, address_ids,
                 rating_ids, aggregate_ratings, num_of_reviewss, best_selling_item_ids,
                 item_names, item_descriptions, coordinate_ids, longitudes,
                 latitudes]
assert len(list_of_lists) == 18
for lst in list_of_lists:
    lst = list(dict.fromkeys(lst))
'''

assert len(postcodes) == len(cities) == len(provinces) == len(street_nums) == len(street_names)
assert len(street_names) == len(restaurant_ids) == len(restaurant_names) == len(price_ranges)
assert len(price_ranges) == len(address_ids) == len(rating_ids) == len(aggregate_ratings)
assert len(aggregate_ratings) == len(num_of_reviewss) == len(best_selling_item_ids) == len(item_names)
assert len(item_names) == len(item_descriptions) == len(coordinate_ids) == len(longitudes) == len(latitudes)

print(postcodes)

conn.close()