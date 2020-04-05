from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.db import connection

import folium
import pandas

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

    # Establish cursor to database
    cur = connection.cursor()

    map = create_map()

    # get restaurants who have donated to all food banks in vancouver that is on the record
    cur.execute(
        'select restaurant_name, longitude, latitude, aggregate_rating, image_url, concat(street_num, \', \', street_name, \', \', city, \', \', state, \' \', postcode)\n' +
        'from restaurants_restaurant\n' +
        'inner join (\n'
        'select distinct donation.restaurant_id_id from restaurants_foodbankdonation as donation\n' +
        'where not exists (\n' +
        '(select foodbank.food_bank from charities_foodbank as foodbank)\n' +
        'except\n' +
        '(select _donation.food_bank from restaurants_foodbankdonation as _donation where donation.restaurant_id_id=_donation.restaurant_id_id)))\n' +
        'as div_results on div_results.restaurant_id_id=restaurants_restaurant.restaurant_id\n' +
        'inner join restaurants_coordinates on restaurants_restaurant.restaurant_id=coordinates_id_id \n' +
        'inner join restaurants_ratingstats on restaurants_restaurant.restaurant_id=rating_stats_id_id\n' +
        'inner join restaurants_imageurl on restaurants_restaurant.restaurant_id=restaurants_imageurl.restaurant_id_id\n' +
        'inner join locations_address on address_id_id=address_id\n' +
        'inner join locations_postcode on postcode=postcode_id'
    )
    ### print query to console
    print(
        "\n--------------------------------------------------------------------\n" +
        'select restaurant_name, longitude, latitude, aggregate_rating, image_url, concat(street_num, \', \', street_name, \', \', city, \', \', state, \' \', postcode)\n' +
        'from restaurants_restaurant\n' +
        'inner join (\n'
        'select distinct donation.restaurant_id_id from restaurants_foodbankdonation as donation\n' +
        'where not exists (\n' +
        '(select foodbank.food_bank from charities_foodbank as foodbank)\n' +
        'except\n' +
        '(select _donation.food_bank from restaurants_foodbankdonation as _donation where donation.restaurant_id_id=_donation.restaurant_id_id)))\n' +
        'as div_results on div_results.restaurant_id_id=restaurants_restaurant.restaurant_id\n' +
        'inner join restaurants_coordinates on restaurants_restaurant.restaurant_id=coordinates_id_id \n' +
        'inner join restaurants_ratingstats on restaurants_restaurant.restaurant_id=rating_stats_id_id\n' +
        'inner join restaurants_imageurl on restaurants_restaurant.restaurant_id=restaurants_imageurl.restaurant_id_id\n' +
        'inner join locations_address on address_id_id=address_id\n' +
        'inner join locations_postcode on postcode=postcode_id'
        + "\n--------------------------------------------------------------------\n"
    )
    rows = cur.fetchall()

    for row in rows:
        restaurant_name = row[0]
        longitude = row[1]
        latitude = row[2]
        aggregate_rating = row[3]
        image_url = row[4]
        address = row[5]
        split_addr = address.split(',')
        addr_line1 = split_addr[0].strip() + ' ' + split_addr[1].strip()
        addr_line2 = split_addr[2].split('(')[0].strip() + ', ' + split_addr[3].strip()


        popup_html = '<div class="card" style="width: 24rem;"><img src="' + image_url + '" class="card-img-top" alt=""><div class="card-body"><strong class="card-title">' + restaurant_name + ': ' + str(aggregate_rating) + ' stars' + '</strong><p class="card-text">' + addr_line1 + '</br>' + addr_line2 + '</p></div>'

        folium.Marker([latitude, longitude], tooltip='More Info', popup=popup_html, icon=folium.Icon(color="lightgray", icon="cutlery", prefix='fa')).add_to(map)

    context = {'map': map.get_root().render()}

    return render(requests, 'map.html', context)


def search(requests, restaurant_name='', street_name='', postcode=''):

    # Establish cursor to database
    cur = connection.cursor()

    map = create_map()

    # reformat string args
    restaurant_name = restaurant_name.replace('-', ' ').strip().upper()
    postcode = postcode.replace('-', ' ').strip().upper()
    street_name = street_name.replace('-', ' ').strip().upper()


    cur.execute(
        'select restaurant_name, longitude, latitude, aggregate_rating, image_url, concat(street_num, \', \', street_name, \', \', city, \', \', state, \' \', postcode)\n' +
        'from restaurants_restaurant\n' +
        'inner join restaurants_coordinates on restaurant_id=coordinates_id_id\n' +
        'inner join locations_address on address_id_id=address_id\n' +
        'inner join locations_postcode on postcode_id=postcode\n' +
        'inner join restaurants_ratingstats on restaurant_id=rating_stats_id_id\n' +
        'inner join restaurants_imageurl on restaurants_restaurant.restaurant_id=restaurants_imageurl.restaurant_id_id\n' +
        'where upper(restaurant_name)=' + "'" + restaurant_name.replace("'", "''") + "'" + ' or ' +
               'upper(postcode_id)=' + "'" + postcode + "'" + ' or ' +
               'upper(street_name)=' + "'" + street_name.replace("'", "''") + "'"
    )
    ### print query to console
    print(
        "\n--------------------------------------------------------------------\n" +
        'select restaurant_name, longitude, latitude, aggregate_rating, image_url, concat(street_num, \', \', street_name, \', \', city, \', \', state, \' \', postcode)\n' +
        'from restaurants_restaurant\n' +
        'inner join restaurants_coordinates on restaurant_id=coordinates_id_id\n' +
        'inner join locations_address on address_id_id=address_id\n' +
        'inner join locations_postcode on postcode_id=postcode\n' +
        'inner join restaurants_ratingstats on restaurant_id=rating_stats_id_id\n' +
        'inner join restaurants_imageurl on restaurants_restaurant.restaurant_id=restaurants_imageurl.restaurant_id_id\n' +
        'where upper(restaurant_name)=' + "'" + restaurant_name.replace("'", "''") + "'" + ' or ' +
               'upper(postcode_id)=' + "'" + postcode + "'" + ' or ' +
               'upper(street_name)=' + "'" + street_name.replace("'", "''") + "'"
        + "\n--------------------------------------------------------------------\n"
    )
    rows = cur.fetchall()
    for row in rows:
        restaurant_name = row[0]
        longitude = row[1]
        latitude = row[2]
        aggregate_rating = row[3]
        image_url = row[4]
        address = row[5]
        split_addr = address.split(',')
        addr_line1 = split_addr[0].strip() + ' ' + split_addr[1].strip()
        addr_line2 = split_addr[2].split('(')[0].strip() + ', ' + split_addr[3].strip()
        popup_html = '<div class="card" style="width: 24rem;"><img src="' + image_url + '" class="card-img-top" alt=""><div class="card-body"><strong class="card-title">' + restaurant_name + ': ' + str(aggregate_rating) + ' stars' + '</strong><p class="card-text">' + addr_line1 + '</br>' + addr_line2 + '</p></div>'

        folium.Marker([latitude, longitude], tooltip='More Info', popup=popup_html, icon=folium.Icon(color="lightgray", icon="cutlery", prefix='fa')).add_to(map)

    # get total number of restaurant entries
    cur.execute(
        'select count(*) from restaurants_restaurant'
    )
    ### print query to console
    print(
        "\n--------------------------------------------------------------------\n" +
        'select count(*) from restaurants_restaurant'
        + "\n--------------------------------------------------------------------\n"
    )
    total_restaurants = cur.fetchall()[0][0]

    context = {'map': map.get_root().render(),
               'results_count': str(len(rows)) + ' results found in ' + str(total_restaurants) + ' entries'
              }

    return render(requests, 'map.html', context)


def show_map_stats(requests):
    
    # Establish cursor to database
    cur = connection.cursor()

    # get restaurants count based on postcode
    cur.execute(
        'select postcode_id, count(*) \n' + 
        'from restaurants_restaurant \n' +
        'inner join locations_address on address_id_id=address_id \n' +
        'group by postcode_id'
    )
    ### print query to console
    print(
        "\n--------------------------------------------------------------------\n" +
        'select postcode_id, count(*) \n' + 
        'from restaurants_restaurant \n' +
        'inner join locations_address on address_id_id=address_id \n' +
        'group by postcode_id'
        + "\n--------------------------------------------------------------------\n"
    )
    stats_by_postcode = cur.fetchall()
    # convert data to dataframe
    pcdf = pandas.DataFrame(stats_by_postcode, columns=('Postcode', 'Number of Restaurants'))

    # get restaurants count based on price_range
    cur.execute(
        'select price_range, count(*) \n' +
        'from restaurants_restaurant \n' +
        'group by price_range \n' +
        'order by length(price_range)'
    )
    ### print query to console
    print(
        "\n--------------------------------------------------------------------\n" +
        'select price_range, count(*) \n' +
        'from restaurants_restaurant \n' +
        'group by price_range \n' +
        'order by length(price_range)'
        + "\n--------------------------------------------------------------------\n"
    )
    stats_by_price_range = cur.fetchall()
    prdf = pandas.DataFrame(stats_by_price_range, columns=('Price Range', 'Number of Restaurants'))

    # get restaurants count based on ratings
    cur.execute(
        'select aggregate_rating, count(*) \n' +
        'from restaurants_restaurant \n' +
        'inner join restaurants_ratingstats on restaurant_id=rating_stats_id_id \n' +
        'group by aggregate_rating \n' +
        'order by aggregate_rating desc'
    )
    ### print query to console
    print(
        "\n--------------------------------------------------------------------\n" +
        'select aggregate_rating, count(*) \n' +
        'from restaurants_restaurant \n' +
        'inner join restaurants_ratingstats on restaurant_id=rating_stats_id_id \n' +
        'group by aggregate_rating \n' +
        'order by aggregate_rating desc'
        + "\n--------------------------------------------------------------------\n"
    )
    stats_by_ratings = cur.fetchall()
    rdf = pandas.DataFrame(stats_by_ratings, columns=('Rating', 'Number of Restaurants'))
    
    context = {
        'stats_by_postcode': pcdf.to_html(classes=['table'], index=False, justify='center'),
        'stats_by_price_range': prdf.to_html(classes=['table'], index=False, justify='center'),
        'stats_by_rating': rdf.to_html(classes=['table'], index=False, justify='center'),
    }

    return render(requests, 'mapstats.html', context)