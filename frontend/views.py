from django.shortcuts import render
from django.shortcuts import HttpResponse
import folium
import psycopg2
import os

# Establish connection to database
conn = psycopg2.connect(
    os.environ['EATVENTURE_DATABASE_URL'], sslmode='require')
# create cursor
cur = conn.cursor()

# Create your views here.


def create_map():
    # create map object
    map = folium.Map(location=[49.246292, -123.116226],
                     zoom_start=12, tiles="Cartodb Positron")
    folium.TileLayer('cartodbpositron').add_to(map)

    return map


def map(requests):

    map = create_map()

    context = {'map': map.get_root().render()}

    return render(requests, 'map.html', context)


def search(requests, restaurant_name, street_name='', postcode=''):

    map = create_map()

    # reformat string args
    restaurant_name = restaurant_name.replace('-', ' ')
    postcode = postcode.replace('-', ' ')
    street_name = street_name.replace('-', ' ')
    
    


    # search_restaurant_query = 'select restaurant_id, longitude, latitude from restaurants_restaurant inner join restaurants_coordinates on restaurant_id=coordinates_id_id where restaurant_name=' + "'" + restaurant_name.replace("'", "''") + "'"
    # print(search_restaurant_query)
    # cur.execute(search_restaurant_query)
    # rows = cur.fetchall()
    # for row in rows:
    #     restaurant_id = row[0]
    #     longitude = row[1]
    #     latitude = row[2]
    #     folium.Marker([latitude, longitude], tooltip='More Info', popup='<strong>' + restaurant_id +
    #                   '</strong>', icon=folium.Icon(color="lightgray", icon="cutlery", prefix='fa')).add_to(map)
    
    cur.execute(
        'select restaurant_name, longitude, latitude ' +
        'from restaurants_restaurant ' +
        'inner join restaurants_coordinates on restaurant_id=coordinates_id_id ' +
        'inner join locations_address on address_id_id=address_id ' +
        'where restaurant_name=' + "'" + restaurant_name.replace("'", "''") + "'" + ' or ' +
               'postcode_id=' + "'" + postcode + "'" + ' or ' +
               'street_name=' + "'" + street_name.replace("'", "''") + "'"
    )
    rows = cur.fetchall()
    for row in rows:
        restaurant_name = row[0]
        longitude = row[1]
        latitude = row[2]
        folium.Marker([latitude, longitude], tooltip='More Info', popup='<strong>' + restaurant_name +
                      '</strong>', icon=folium.Icon(color="lightgray", icon="cutlery", prefix='fa')).add_to(map)

    # cur.execute(
    #     'select count(*) from (' +
    #     'select restaurant_name, longitude, latitude ' +
    #     'from restaurants_restaurant ' +
    #     'inner join restaurants_coordinates on restaurant_id=coordinates_id_id ' +
    #     'inner join locations_address on address_id_id=address_id ' +
    #     'where restaurant_name=' + "'" + restaurant_name.replace("'", "''") + "'" + ' or ' +
    #            'postcode_id=' + "'" + postcode + "'" + ' or ' +
    #            'street_name=' + "'" + street_name.replace("'", "''") + "'" +
    #     ")" + "as results_found"
    # )
    # results_count = cur.fetchall()[0][0]

    context = {'map': map.get_root().render(),
               'results_count': str(len(rows)) + ' results found'
              }

    return render(requests, 'map.html', context)