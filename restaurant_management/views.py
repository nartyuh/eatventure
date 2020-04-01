from django.shortcuts import render, HttpResponse

import psycopg2
import os
import pandas

# Establish connection to database
conn = psycopg2.connect(
    os.environ['EATVENTURE_DATABASE_URL'], sslmode='require')
# create cursor
cur = conn.cursor()

# Create your views here.

def index(requests):
    return HttpResponse('Oops you\'re not supposed to be here...' )

def render_login(requests):
    return render(requests, 'login.html')

def login(requests, username, password):

    cur.execute(
        'select username ' + '\n' +
        'from restaurant_management_manageraccount ' + '\n' +
        'where username=' + "'" + username + "'"
    )
    # print('select username ' + '\n' +
    #     'from restaurant_management_manageraccount ' + '\n' +
    #     'where username=' + "'" + username + "'")
    rows = cur.fetchall()
    if len(rows) == 0:
        context = {
            'message' : '<html><p>There is no account associated with this username and password</p></html>',
        }
        return render(requests, 'failed_login.html', context)
    else:

        

        cur.execute(
            'select restaurant_name, concat(cast(longitude as varchar), \', \', cast(latitude as varchar)), concat(street_num, \', \', street_name, \', \', city, \', \', state, \' \', postcode), aggregate_rating, review_count ' + "\n" +
            'from (select restaurant_id from restaurant_management_matchmanagertorestaurant where manager_id=' + "'" + rows[0][0] + "') as manager_restaurants " + '\n' + 
            'inner join restaurants_restaurant on restaurants_restaurant.restaurant_id=manager_restaurants.restaurant_id ' + '\n' + 
            'inner join locations_address on address_id_id=address_id ' + '\n' +
            'inner join locations_postcode on postcode=postcode_id ' + '\n' +
            'inner join restaurants_coordinates on restaurants_restaurant.restaurant_id=restaurants_coordinates.coordinates_id_id ' + '\n' +
            'inner join restaurants_ratingstats on restaurants_restaurant.restaurant_id=restaurants_ratingstats.rating_stats_id_id' 
        )
        # print('select restaurant_name, longitude, latitude, street_num, street_name, city, state, province, postalcode, aggregate_rating, num_of_reviews ' + "\n" +
        #     'from (select restaurant_id from restaurant_management_matchmanagertorestaurant where manager_id=' + "'" + rows[0][0] + "') as manager_restaurants " + '\n' + 
        #     'inner join restaurants_restaurant on restaurants_restaurant.restaurant_id=manager_restaurants.restaurant_id ' + '\n' + 
        #     'inner join restaurants_coordinates on restaurants_restaurant.restaurant_id=restaurants_coordinates.restaurant_id_id ' + '\n' +
        #     'inner join locations_address on address_id_id=address_id ' + '\n' +
        #     'inner join restaurants_ratingstats on restaurants_restaurant.restaurant_id=restaurants_ratingstats.restaurant_id_id' )
        rows = cur.fetchall()
        df = pandas.DataFrame(rows, columns=('Restaurant', 'Coordinates', 'Address', 'Ratings', 'Number of Reviews'))
        html = df.to_html(classes=["table-bordered", "table-striped", "table-hover"])
        context = {
            'table': html
        }
        return render(requests, 'logged_in.html', context)
        