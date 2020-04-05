from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpRequest
from django.db import connection

import pandas

# Create your views here.

def index(requests):
    return HttpResponse('Oops you\'re not supposed to be here...')


def render_login(requests):
    return render(requests, 'login.html')


def login(requests, username, password):

    # Establish cursor to database
    cur = connection.cursor()

    # check database if this is a registered account
    cur.execute(
        'select username ' + '\n' +
        'from restaurant_management_manageraccount ' + '\n' +
        'where username=' + "'" + username + "'" +
        " and " + "password=" + "'" + password + "'"
    )

    ### print query to console
    print(
        "\n--------------------------------------------------------------------\n" +
        'select username ' + '\n' +
        'from restaurant_management_manageraccount ' + '\n' +
        'where username=' + "'" + username + "'" +
        " and " + "password=" + "'" + password + "'"
        + "\n--------------------------------------------------------------------\n"
    )

    rows = cur.fetchall()

    if len(rows) == 0:
        context = {
            'message': '<html><p>There is no account associated with this username and password</p></html>',
        }
        return render(requests, 'failed_login.html', context)
    else:

        cur.execute(
            'select restaurants_restaurant.restaurant_id, restaurant_name, concat(street_num, \', \', street_name, \', \', city, \', \', state, \' \', postcode), manager_id ' + "\n" +
            'from (select restaurant_id, manager_id from restaurant_management_matchmanagertorestaurant where manager_id=' + "'" + rows[0][0] + "') as manager_restaurants " + '\n' +
            'inner join restaurants_restaurant on restaurants_restaurant.restaurant_id=manager_restaurants.restaurant_id ' + '\n' +
            'inner join locations_address on address_id_id=address_id ' + '\n' +
            'inner join locations_postcode on postcode=postcode_id '
        )
        ### print query to console
        print(
            "\n--------------------------------------------------------------------\n" +
            'select restaurants_restaurant.restaurant_id, restaurant_name, concat(street_num, \', \', street_name, \', \', city, \', \', state, \' \', postcode), manager_id ' + "\n" +
            'from (select restaurant_id, manager_id from restaurant_management_matchmanagertorestaurant where manager_id=' + "'" + rows[0][0] + "') as manager_restaurants " + '\n' +
            'inner join restaurants_restaurant on restaurants_restaurant.restaurant_id=manager_restaurants.restaurant_id ' + '\n' +
            'inner join locations_address on address_id_id=address_id ' + '\n' +
            'inner join locations_postcode on postcode=postcode_id '
            + "\n--------------------------------------------------------------------\n"
        )
        rows = cur.fetchall()

        df = pandas.DataFrame(rows, columns=(
            'ID', 'Restaurant', 'Address', 'Manager'))

        # attaching url to df for cells under Restaurant
        def make_clickable(url, name):
            return '<a href="{}">{}</a>'.format(url, name)
        df['Restaurant'] = df.apply(
            lambda x: make_clickable(x['ID'], x['Restaurant']), axis=1)

        df.drop('ID', axis=1, inplace=True)

        html = df.to_html(classes=['table', 'table-bordered', 'table-hover', ], table_id='df_table',
                          justify='center', render_links=True, escape=False, index=False, border=0)
        context = {
            'manager_view': html
        }

        return render(requests, 'manager_view.html', context)


def view_restaurant(requests, username, password, restaurant_id):

    print(username)
    print(password)
    print(restaurant_id)

    # Establish cursor to database
    cur = connection.cursor()

    # check database if this is a registered account
    cur.execute(
        'select username ' + '\n' +
        'from restaurant_management_manageraccount ' + '\n' +
        'where username=' + "'" + username + "'" +
        " and " + "password=" + "'" + password + "'"
    )
    rows = cur.fetchall()

    if len(rows) == 0:
        context = {
            'message': '<html><p>There is no account associated with this username and password</p></html>',
        }
        return render(requests, 'failed_login.html', context)
    else:

        cur.execute(
            'select ' +
            'restaurant_name, ' +
            'concat(street_num, \', \', street_name, \', \', city, \', \', state, \' \', postcode), ' + '\n' +
            'concat(cast(longitude as varchar), \', \', cast(latitude as varchar)), ' + '\n' +
            'price_range, aggregate_rating, review_count, item_name, item_description ' + '\n' +
            'from restaurants_restaurant ' + '\n' +
            'inner join locations_address on address_id_id=address_id ' + '\n' +
            'inner join locations_postcode on postcode=postcode_id ' + '\n' +
            'inner join restaurants_coordinates on restaurants_restaurant.restaurant_id=restaurants_coordinates.coordinates_id_id ' + '\n' +
            'inner join restaurants_ratingstats on restaurants_restaurant.restaurant_id=restaurants_ratingstats.rating_stats_id_id' + '\n' +
            'inner join restaurants_bestsellingitem on restaurants_restaurant.restaurant_id=restaurants_bestsellingitem.best_selling_item_id_id ' + '\n' +
            'where restaurants_restaurant.restaurant_id=' + "'" + restaurant_id + "'"
        )
        ### print query to console
        print(
            "\n--------------------------------------------------------------------\n" +
            'select ' +
            'restaurant_name, ' +
            'concat(street_num, \', \', street_name, \', \', city, \', \', state, \' \', postcode), ' + '\n' +
            'concat(cast(longitude as varchar), \', \', cast(latitude as varchar)), ' + '\n' +
            'price_range, aggregate_rating, review_count, item_name, item_description ' + '\n' +
            'from restaurants_restaurant ' + '\n' +
            'inner join locations_address on address_id_id=address_id ' + '\n' +
            'inner join locations_postcode on postcode=postcode_id ' + '\n' +
            'inner join restaurants_coordinates on restaurants_restaurant.restaurant_id=restaurants_coordinates.coordinates_id_id ' + '\n' +
            'inner join restaurants_ratingstats on restaurants_restaurant.restaurant_id=restaurants_ratingstats.rating_stats_id_id' + '\n' +
            'inner join restaurants_bestsellingitem on restaurants_restaurant.restaurant_id=restaurants_bestsellingitem.best_selling_item_id_id ' + '\n' +
            'where restaurants_restaurant.restaurant_id=' + "'" + restaurant_id + "'"
            + "\n--------------------------------------------------------------------\n"
        )
        # get output from query
        rows = cur.fetchall()
        restaurant_data = rows[0]

        context = {
            'restaurant': 'Restaurant',
            'restaurant_str': restaurant_data[0],
            'address': 'Address',
            'address_str': restaurant_data[1],
            'coordinates': 'Coordinates',
            'coordinates_str': restaurant_data[2],
            'price_range': 'Price range',
            'price_range_str': restaurant_data[3],
            'rating': 'Rating',
            'rating_str': restaurant_data[4],
            'review_count': 'Number of Reviews',
            'review_count_str': restaurant_data[5],
            'best_selling_item': 'Best Selling Item',
            'best_selling_item_str': restaurant_data[6],
            'best_selling_item_dsc': 'Best Selling Item Description',
            'best_selling_item_dsc_str': restaurant_data[7],
            'food_bank': 'Support a food bank'
        }

        return render(requests, 'restaurant_view.html', context)


def update_restaurant(requests, username, password, restaurant_id, restaurant_name, best_selling_item, best_selling_item_dsc, food_bank):

    # Establish cursor to database
    cur = connection.cursor()

    # check database if this is a registered account
    cur.execute(
        'select username ' + '\n' +
        'from restaurant_management_manageraccount ' + '\n' +
        'where username=' + "'" + username + "'" +
        " and " + "password=" + "'" + password + "'"
    )
    rows = cur.fetchall()

    if len(rows) == 0:
        context = {
            'message': '<html><p>There is no account associated with this username and password</p></html>',
        }
        return render(requests, 'failed_login.html', context)
    else:
        cur.execute(
            'select * ' + '\n' +
            'from restaurant_management_matchmanagertorestaurant ' + '\n' +
            'where restaurant_id=' + "'" + restaurant_id + "'" +
            " and " + "manager_id=" + "'" + username + "'"
        )
        ### print query to console
        print(
            "\n--------------------------------------------------------------------\n" +
            'select * ' + '\n' +
            'from restaurant_management_matchmanagertorestaurant ' + '\n' +
            'where restaurant_id=' + "'" + restaurant_id + "'" +
            " and " + "manager_id=" + "'" + username + "'"
            + "\n--------------------------------------------------------------------\n"
        )
        rows = cur.fetchall()

        if (len(rows) == 0):
            return HttpResponse("There are no restaurants managed by this account.")
        else:
            # format string
            restaurant_name = restaurant_name.strip().replace("'", "''")
            best_selling_item = best_selling_item.strip().replace("'", "''")
            best_selling_item_dsc = best_selling_item_dsc.strip().replace("'", "''")
            food_bank = food_bank.strip().replace("'", "''")


            cur.execute(
                'update restaurants_restaurant \n' +
                'set restaurant_name=' + "'" + restaurant_name + "' \n" +
                'where restaurant_id=' + "'" + restaurant_id + "'"
            )
            cur.execute(
                'update restaurants_bestsellingitem \n' +
                'set item_name=' + "'" + best_selling_item + "', item_description='" + best_selling_item_dsc + "' \n" +
                'where best_selling_item_id_id=' + "'" + restaurant_id + "'" 
            )
            ### print query to console
            print(
                "\n--------------------------------------------------------------------\n" +
                'update restaurants_restaurant \n' +
                'set restaurant_name=' + "'" + restaurant_name + "' \n" +
                'where restaurant_id=' + "'" + restaurant_id + "'"
                + "\n--------------------------------------------------------------------\n" +
                'update restaurants_bestsellingitem \n' +
                'set item_name=' + "'" + best_selling_item + "', item_description='" + best_selling_item_dsc + "' \n" +
                'where best_selling_item_id_id=' + "'" + restaurant_id + "'" 
                + "\n--------------------------------------------------------------------\n"
            )

            # insert a record to restaurants_foodbankdonation if the restaurant decides to donate to a food bank
            if len(food_bank) != 0:
                cur.execute(
                    'insert into restaurants_foodbankdonation\n' +
                    "values ('" + food_bank.strip() + "', " + "'" + restaurant_id +"')"
                )
                ### print query to console
                print(
                    "\n--------------------------------------------------------------------\n" +
                    'insert into restaurants_foodbankdonation\n' +
                    "values ('" + food_bank.strip() + "', " + "'" + restaurant_id +"')"
                    + "\n--------------------------------------------------------------------\n"
                )

            return redirect("/login/" + username + "/" + password + "/" )


def delete_restaurant(requests, username, password, restaurant_id):

    # Establish cursor to database
    cur = connection.cursor()
    
    cur.execute(
        'select username ' + '\n' +
        'from restaurant_management_manageraccount ' + '\n' +
        'where username=' + "'" + username + "'" +
        " and " + "password=" + "'" + password + "'"
    )
    rows = cur.fetchall()

    # check if there is a matching account in database
    if len(rows) == 0:
        context = {
            'message': '<html><p>There is no account associated with this username and password</p></html>',
        }
        return render(requests, 'failed_login.html', context)
    else:
        cur.execute(
            'delete \n' +
            'from restaurant_management_matchmanagertorestaurant \n' +
            'where manager_id=' + "'" + username + "' and restaurant_id='" + restaurant_id + "'"  
        )
        # print query to console
        print(
            "\n--------------------------------------------------------------------\n" +
            'delete \n' +
            'from restaurant_management_matchmanagertorestaurant \n' +
            'where manager_id=' + "'" + username + "' and restaurant_id='" + restaurant_id + "'"
            + "\n--------------------------------------------------------------------\n"  
        )

        return redirect("/login/" + username + "/" + password + "/" )


def delete_account(requests, username, password):

    # Establish cursor to database
    cur = connection.cursor()
    
    cur.execute(
        'select username ' + '\n' +
        'from restaurant_management_manageraccount ' + '\n' +
        'where username=' + "'" + username + "'" +
        " and " + "password=" + "'" + password + "'"
    )
    rows = cur.fetchall()

    # check if there is a matching account in database
    if len(rows) == 0:
        context = {
            'message': '<html><p>There is no account associated with this username and password</p></html>',
        }
        return render(requests, 'failed_login.html', context)
    else:
        cur.execute(
            'delete\n' +
            'from restaurant_management_manageraccount\n' +
            "where username='" + username + "' and password='" + password + "'" 
        )
        ### print query to the console
        print(
            "\n--------------------------------------------------------------------\n" +
            'delete\n' +
            'from restaurant_management_manageraccount\n' +
            "where username='" + username + "' and password='" + password + "'"
            + "\n--------------------------------------------------------------------\n"
        )

        return redirect("/login/")
