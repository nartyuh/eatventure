import json

# load data from file1.json
json_file1 = open('data/file1.json')
json1 = json.load(json_file1)

# load data from file2.json
json_file2 = open('data/file2.json')
json2 = json.load(json_file2)

# load data from file3.json
json_file3 = open('data/file3.json')
json3 = json.load(json_file3)

# load data from file4.json
json_file4 = open('data/file4.json')
json4 = json.load(json_file4)

# load data from file5.json
json_file5 = open('data/file5.json')
json5 = json.load(json_file5)


canada_id = 37
canada_restaurants = []

for results in json1:
    try:
        for restaurant in results['restaurants']:
            restaurant_country_id = restaurant['restaurant']['location']['country_id']
            if (restaurant_country_id == canada_id):
                canada_restaurants.append(restaurant)
    except KeyError:
        pass

for results in json2:
    try:
        for restaurant in results['restaurants']:
            restaurant_country_id = restaurant['restaurant']['location']['country_id']
            if (restaurant_country_id == canada_id):
                canada_restaurants.append(restaurant)
    except KeyError:
        pass

for results in json3:
    try:
        for restaurant in results['restaurants']:
            restaurant_country_id = restaurant['restaurant']['location']['country_id']
            if (restaurant_country_id == canada_id):
                canada_restaurants.append(restaurant)
    except KeyError:
        pass

for results in json4:
    try:
        for restaurant in results['restaurants']:
            restaurant_country_id = restaurant['restaurant']['location']['country_id']
            if (restaurant_country_id == canada_id):
                canada_restaurants.append(restaurant)
    except KeyError:
        pass

for results in json5:
    try:
        for restaurant in results['restaurants']:
            restaurant_country_id = restaurant['restaurant']['location']['country_id']
            if (restaurant_country_id == canada_id):
                canada_restaurants.append(restaurant)
    except KeyError:
        pass

outfile = open('canada_restaurants.json', 'w')
outfile.write(json.dumps(canada_restaurants))
outfile.close()