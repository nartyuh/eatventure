-- Division queries
--------------------------------------------------------------------
select restaurant_name, longitude, latitude, aggregate_rating, image_url, concat(street_num, ', ', street_name, ', ', city, ', ', state, ' ', postcode)
from restaurants_restaurant
inner join (
select distinct donation.restaurant_id_id from restaurants_foodbankdonation as donation
where not exists (
(select foodbank.food_bank from charities_foodbank as foodbank)
except
(select _donation.food_bank from restaurants_foodbankdonation as _donation where donation.restaurant_id_id=_donation.restaurant_id_id)))
as div_results on div_results.restaurant_id_id=restaurants_restaurant.restaurant_id
inner join restaurants_coordinates on restaurants_restaurant.restaurant_id=coordinates_id_id
inner join restaurants_ratingstats on restaurants_restaurant.restaurant_id=rating_stats_id_id
inner join restaurants_imageurl on restaurants_restaurant.restaurant_id=restaurants_imageurl.restaurant_id_id
inner join locations_address on address_id_id=address_id
inner join locations_postcode on postcode=postcode_id
--------------------------------------------------------------------


-- Select queries
--------------------------------------------------------------------
select restaurant_name, longitude, latitude, aggregate_rating, image_url, concat(street_num, ', ', street_name, ', ', city, ', ', state, ' ', postcode)
from restaurants_restaurant
inner join restaurants_coordinates on restaurant_id=coordinates_id_id
inner join locations_address on address_id_id=address_id
inner join locations_postcode on postcode_id=postcode
inner join restaurants_ratingstats on restaurant_id=rating_stats_id_id
inner join restaurants_imageurl on restaurants_restaurant.restaurant_id=restaurants_imageurl.restaurant_id_id
where upper(restaurant_name)='FATBURGER' or upper(postcode_id)='V6T 1Z1' or upper(street_name)='DAVIE STREET'
--------------------------------------------------------------------


-- Aggregation queries
--------------------------------------------------------------------
select count(*) from restaurants_restaurant
--------------------------------------------------------------------


-- Nested aggregation with group-by queries
--------------------------------------------------------------------
select postcode_id, count(*)
from restaurants_restaurant
inner join locations_address on address_id_id=address_id
group by postcode_id
--------------------------------------------------------------------
--------------------------------------------------------------------
select price_range, count(*)
from restaurants_restaurant
group by price_range
order by length(price_range)
--------------------------------------------------------------------
--------------------------------------------------------------------
select aggregate_rating, count(*)
from restaurants_restaurant
inner join restaurants_ratingstats on restaurant_id=rating_stats_id_id
group by aggregate_rating
order by aggregate_rating desc
--------------------------------------------------------------------


-- Projection queries
--------------------------------------------------------------------
select restaurant_name, concat(street_num, ', ', street_name, ', ', city, ', ', state, ' ', postcode)
from restaurants_restaurant
inner join locations_address on address_id_id=address_id
inner join locations_postcode on postcode_id=postcode
--------------------------------------------------------------------
--------------------------------------------------------------------
select restaurant_name, concat(cast(longitude as varchar), ', ', cast(latitude as varchar))
from restaurants_restaurant
inner join restaurants_coordinates on restaurant_id=coordinates_id_id
--------------------------------------------------------------------
--------------------------------------------------------------------
select restaurant_name, aggregate_rating, review_count
from restaurants_restaurant
inner join restaurants_ratingstats on restaurant_id=rating_stats_id_id
--------------------------------------------------------------------


-- Join Queries
--------------------------------------------------------------------
select postcode_id, count(*)
from restaurants_restaurant
inner join locations_address on address_id_id=address_id
group by postcode_id
--------------------------------------------------------------------
--------------------------------------------------------------------
select price_range, count(*)
from restaurants_restaurant
group by price_range
order by length(price_range)
--------------------------------------------------------------------
--------------------------------------------------------------------
select aggregate_rating, count(*)
from restaurants_restaurant
inner join restaurants_ratingstats on restaurant_id=rating_stats_id_id
group by aggregate_rating
order by aggregate_rating desc
--------------------------------------------------------------------
--------------------------------------------------------------------
select restaurant_name, concat(street_num, ', ', street_name, ', ', city, ', ', state, ' ', postcode)
from restaurants_restaurant
inner join locations_address on address_id_id=address_id
inner join locations_postcode on postcode_id=postcode
--------------------------------------------------------------------
--------------------------------------------------------------------
select restaurant_name, concat(cast(longitude as varchar), ', ', cast(latitude as varchar))
from restaurants_restaurant
inner join restaurants_coordinates on restaurant_id=coordinates_id_id
--------------------------------------------------------------------
--------------------------------------------------------------------
select restaurant_name, aggregate_rating, review_count
from restaurants_restaurant
inner join restaurants_ratingstats on restaurant_id=rating_stats_id_id
--------------------------------------------------------------------



-- Insert queries
--------------------------------------------------------------------
insert into restaurants_foodbankdonation
values ('Blue Sky', 'n1NeUsTJyPn6YfGS9TTDUg')
--------------------------------------------------------------------


-- Delete queries
--------------------------------------------------------------------
delete
from restaurant_management_manageraccount
where username='huytran' and password='12345'
--------------------------------------------------------------------


-- Update queries
--------------------------------------------------------------------
update restaurants_restaurant
set restaurant_name='Prado Cafe'
where restaurant_id='n1NeUsTJyPn6YfGS9TTDUg'
--------------------------------------------------------------------
update restaurants_bestsellingitem
set item_name='Cappuccino', item_description='an espresso-based coffee drink that originated in Italy'
where best_selling_item_id_id='n1NeUsTJyPn6YfGS9TTDUg'
--------------------------------------------------------------------


-- Queries we used that have not been listed
--------------------------------------------------------------------
select username
from restaurant_management_manageraccount
where username='huytran' and password='12345'
--------------------------------------------------------------------
--------------------------------------------------------------------
select restaurants_restaurant.restaurant_id, restaurant_name, concat(street_num, ', ', street_name, ', ', city, ', ', state, ' ', postcode), manager_id
from (select restaurant_id, manager_id from restaurant_management_matchmanagertorestaurant where manager_id='huytran') as manager_restaurants
inner join restaurants_restaurant on restaurants_restaurant.restaurant_id=manager_restaurants.restaurant_id
inner join locations_address on address_id_id=address_id
inner join locations_postcode on postcode=postcode_id
--------------------------------------------------------------------
--------------------------------------------------------------------
select restaurant_name, concat(street_num, ', ', street_name, ', ', city, ', ', state, ' ', postcode),
concat(cast(longitude as varchar), ', ', cast(latitude as varchar)),
price_range, aggregate_rating, review_count, item_name, item_description
from restaurants_restaurant
inner join locations_address on address_id_id=address_id
inner join locations_postcode on postcode=postcode_id
inner join restaurants_coordinates on restaurants_restaurant.restaurant_id=restaurants_coordinates.coordinates_id_id
inner join restaurants_ratingstats on restaurants_restaurant.restaurant_id=restaurants_ratingstats.rating_stats_id_id
inner join restaurants_bestsellingitem on restaurants_restaurant.restaurant_id=restaurants_bestsellingitem.best_selling_item_id_id
where restaurants_restaurant.restaurant_id='n1NeUsTJyPn6YfGS9TTDUg'
--------------------------------------------------------------------
--------------------------------------------------------------------
delete
from restaurant_management_matchmanagertorestaurant
where manager_id='testmanager' and restaurant_id='sLBJg33T9LfeKmq-FKxssg'
--------------------------------------------------------------------
