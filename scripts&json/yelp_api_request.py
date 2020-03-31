import requests
import json

api_key = 'R5yCVcL2qlC1XtPmfCPX0fx6xm2Ng0kmTuXV8c7mWd_iKSnv90Isfb2tx8vTKccoi3AO9AZqE7QQxElYzmgGWKliSSWmzKx-XAXrW1tjrGosJbyiaPR9VB8MjiaAXnYx'
headers = {'Authorization': 'Bearer %s' % api_key}
url = 'https://api.yelp.com/v3/businesses/search'

# starting result entry
offset_inc = 20
data = []

offset = 0
for i in range(int(1000/offset_inc)):
    print(offset)
    params = {
        'term': 'breakfast',
        'location': 'Vancouver',
        'radius': 40000,
        'offset': offset  # increase offset everytime the api is called until reach 1000
    }
    request = requests.get(url, params=params, headers=headers)
    offset += offset_inc    # increment offset by offset_inc
    data.append(json.loads(request.text))

offset = 0
for i in range(int(1000/offset_inc)): 
    print(offset)
    params = {
        'term': 'brunch',
        'location': 'Vancouver',
        'radius': 40000,
        'offset': offset  # increase offset everytime the api is called until reach 1000
    }
    request = requests.get(url, params=params, headers=headers)
    offset += offset_inc    # increment offset by offset_inc
    data.append(json.loads(request.text))

offset = 0
for i in range(int(1000/offset_inc)): 
    print(offset)
    params = {
        'term': 'lunch',
        'location': 'Vancouver',
        'radius': 40000,
        'offset': offset  # increase offset everytime the api is called until reach 1000
    }
    request = requests.get(url, params=params, headers=headers)
    offset += offset_inc    # increment offset by offset_inc
    data.append(json.loads(request.text))

offset = 0
for i in range(int(1000/offset_inc)):  
    print(offset)
    params = {
        'term': 'dinner',
        'location': 'Vancouver',
        'radius': 40000,
        'offset': offset  # increase offset everytime the api is called until reach 1000
    }
    request = requests.get(url, params=params, headers=headers)
    offset += offset_inc    # increment offset by offset_inc
    data.append(json.loads(request.text))

offset = 0
for i in range(int(1000/offset_inc)):
    print(offset)
    params = {
        'term': 'eat',
        'location': 'Vancouver',
        'radius': 40000,
        'offset': offset  # increase offset everytime the api is called until reach 1000
    }
    request = requests.get(url, params=params, headers=headers)
    offset += offset_inc    # increment offset by offset_inc
    data.append(json.loads(request.text))

offset = 0
for i in range(int(1000/offset_inc)):
    print(offset)
    params = {
        'term': 'eats',
        'location': 'Vancouver',
        'radius': 40000,
        'offset': offset  # increase offset everytime the api is called until reach 1000
    }
    request = requests.get(url, params=params, headers=headers)
    offset += offset_inc    # increment offset by offset_inc
    data.append(json.loads(request.text))

offset = 0
for i in range(int(1000/offset_inc)):
    print(offset)
    params = {
        'term': 'food',
        'location': 'Vancouver',
        'radius': 40000,
        'offset': offset  # increase offset everytime the api is called until reach 1000
    }
    request = requests.get(url, params=params, headers=headers)
    offset += offset_inc    # increment offset by offset_inc
    data.append(json.loads(request.text))

offset = 0
for i in range(int(1000/offset_inc)):
    print(offset)
    params = {
        'term': 'restauraunt',
        'location': 'Vancouver',
        'radius': 40000,
        'offset': offset  # increase offset everytime the api is called until reach 1000
    }
    request = requests.get(url, params=params, headers=headers)
    offset += offset_inc    # increment offset by offset_inc
    data.append(json.loads(request.text))

offset = 0
for i in range(int(1000/offset_inc)):
    print(offset)
    params = {
        'term': 'restauraunts',
        'location': 'Vancouver',
        'radius': 40000,
        'offset': offset  # increase offset everytime the api is called until reach 1000
    }
    request = requests.get(url, params=params, headers=headers)
    offset += offset_inc    # increment offset by offset_inc
    data.append(json.loads(request.text))

print(data)

outfile = open('yelp_api_request.json', 'w')
outfile.write(json.dumps(data))
outfile.close()
