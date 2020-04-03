from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.db import connection
import folium
import psycopg2
import os

# Establish cursor to database
cur = connection.cursor()

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

    cur.execute(
        'select restaurant_name, longitude, latitude, aggregate_rating ' +
        'from restaurants_restaurant ' +
        'inner join restaurants_coordinates on restaurant_id=coordinates_id_id ' +
        'inner join locations_address on address_id_id=address_id ' +
        'inner join restaurants_ratingstats on restaurant_id=rating_stats_id_id ' +
        'where restaurant_name=' + "'" + restaurant_name.replace("'", "''") + "'" + ' or ' +
               'postcode_id=' + "'" + postcode + "'" + ' or ' +
               'street_name=' + "'" + street_name.replace("'", "''") + "'"
    )

    ### print query to console
    print(
        "\n--------------------------------------------------------------------\n" +
        'select restaurant_name, longitude, latitude, aggregate_rating \n' +
        'from restaurants_restaurant \n' +
        'inner join restaurants_coordinates on restaurant_id=coordinates_id_id \n' +
        'inner join locations_address on address_id_id=address_id \n' +
        'inner join restaurants_ratingstats on restaurant_id=rating_stats_id_id \n' +
        'where restaurant_name=' + "'" + restaurant_name.replace("'", "''") + "'" + ' or ' +
               'postcode_id=' + "'" + postcode + "'" + ' or ' +
               'street_name=' + "'" + street_name.replace("'", "''") + "'"
        + "\n--------------------------------------------------------------------\n"
    )
    rows = cur.fetchall()
    for row in rows:
        restaurant_name = row[0]
        longitude = row[1]
        latitude = row[2]
        aggregate_rating = row[3]
        folium.Marker([latitude, longitude], tooltip='More Info', popup='<strong>' + restaurant_name + ": " + str(aggregate_rating) + " stars" +
                      '</strong>', icon=folium.Icon(color="lightgray", icon="cutlery", prefix='fa')).add_to(map)

    # get all entries in restaurants_restaurnant
    cur.execute(
        'select count(*)' + '\n' +
        'from restaurants_restaurant'
    )

    ### print query to console
    print(
        "\n--------------------------------------------------------------------\n" +
        'select count(*)' + '\n' +
        'from restaurants_restaurant'
        + "\n--------------------------------------------------------------------\n"
    )

    context = {'map': map.get_root().render(),
               'results_count': str(len(rows)) + ' results found ' + 'in ' + str(cur.fetchall()[0][0]) + ' entries'
              }

    return render(requests, 'map.html', context)


def show_map_stats(requests):
    
    # get the total number of restaurants in Vancouver
    cur.execute(
        'select count(*)\n' +
        'from restaurants_restaurant'
    )
    total_restaurants = cur.fetchall()[0][0]

    return HttpResponse('This view is being developed')
