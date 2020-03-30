import json

jsonfile = open('yelp_api_request.json', 'r')
# load json
data = json.load(jsonfile)

yelp_canada_restaurants = []

for businesses in data:
    try:
        businesses = businesses['businesses']
        for business in businesses:
            yelp_canada_restaurants.append(business)
    except KeyError:
        pass

# remove duplicates from list of restaurants
seen_restaurant_ids = set()
temp_list = []
# Start the iteration over dict
for restaurant in yelp_canada_restaurants:
    restaurant_id = restaurant['id']
    if restaurant_id not in seen_restaurant_ids:
        seen_restaurant_ids.add(restaurant_id)
        temp_list.append(restaurant)

# set the out list to the temp list
yelp_canada_restaurants = temp_list
# get length of output list
print(len(yelp_canada_restaurants))

outfile = open('yelp_canada_restaurants.json', 'w')
outfile.write(json.dumps(yelp_canada_restaurants))
outfile.close()
