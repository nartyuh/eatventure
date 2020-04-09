# EatVenture

## Project Beta Run

To see the beta run: http://eatventure.tranquanghuy.me/

## Project Description

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RestaurantAdvisor is the "google map" for restaurants. It is built to help travellers find the best nearby restaurants and get the necessary knowledge about the restaurant that they are looking into.
<br />
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This includes things like sorting the star ratings of the restaurants in the local city (1-5 stars), filtering out the restaurants by types of meals (vegetarian, vegan, etc.), cuisines (Italian, Chinese, Japanese, etc), atmosphere (fine dining, bistro, cafe, etc.), as well as seeing the price range ($-$$$$).
<br />
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;These types of information will let the customers choose what their next actions will be, such as making a reservation, looking through the menus, ordering a takeout, etc. As a result, all of these features should allow our customers to choose which restaurant that is a good fit for them, as well as leaving a review of a restaurant by giving a star rating and comments once they’re finished eating at the restaurant.
<br />
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;And finally, the customer should not be able to change the restaurants’ data within the DB. Only accounts with certain granted admin privilege may change/update the restaurants’ data, as well as adding/removing restaurants to the DB.
<br />
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As a result, there will be two types of users in this app: the restaurant managers (those who are going to put their restaurants on the app and will have the ability to set prices, menus, etc), and the customers who are looking for restaurants to eat.

## App Screenshots

#### Main Page
![alt text](https://raw.githubusercontent.com/dekutran99/Eatventure/master/readmepics/main.PNG)
#### Search results
![alt text](https://raw.githubusercontent.com/dekutran99/Eatventure/master/readmepics/search.PNG)
#### Details and Stats
![alt text](https://raw.githubusercontent.com/dekutran99/Eatventure/master/readmepics/details.PNG)
#### Login Page
![alt text](https://raw.githubusercontent.com/dekutran99/Eatventure/master/readmepics/login.PNG)
#### Manager View
![alt text](https://raw.githubusercontent.com/dekutran99/Eatventure/master/readmepics/managerview.PNG)
#### Restaurant View
![alt text](https://raw.githubusercontent.com/dekutran99/Eatventure/master/readmepics/restaurantview.PNG)

## Schema and Sample SQL Queries

#### Schema

```sql
--
-- Create model Country
--
CREATE TABLE "locations_country" ("country_name" varchar(20) NOT NULL PRIMARY KEY);
--
-- Create model Postcode
--
CREATE TABLE "locations_postcode" ("postcode" varchar(10) NOT NULL PRIMARY KEY, "city" varchar(20) NOT NULL, "state" varchar(20) NOT NULL, "country_id" varchar(20) NOT NULL);
--
-- Create model Address
--
CREATE TABLE "locations_address" ("address_id" varchar(50) NOT NULL PRIMARY KEY, "street_num" varchar(10) NOT NULL, "street_name" varchar(30) NOT NULL, "postcode_id" varchar(10) NOT NULL);
CREATE INDEX "locations_country_country_name_162e2e27_like" ON "locations_country" ("country_name" varchar_pattern_ops);
ALTER TABLE "locations_postcode" ADD CONSTRAINT "locations_postcode_city_state_country_id_ef0ab36c_uniq" UNIQUE ("city", "state", "country_id");
ALTER TABLE "locations_postcode" ADD CONSTRAINT "locations_postcode_country_id_e1f4da17_fk_locations" FOREIGN KEY ("country_id") REFERENCES "locations_country" ("country_name") ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "locations_postcode_postcode_21c425e3_like" ON "locations_postcode" ("postcode" varchar_pattern_ops);
CREATE INDEX "locations_postcode_country_id_e1f4da17" ON "locations_postcode" ("country_id");
CREATE INDEX "locations_postcode_country_id_e1f4da17_like" ON "locations_postcode" ("country_id" varchar_pattern_ops);
ALTER TABLE "locations_address" ADD CONSTRAINT "locations_address_street_num_street_name_p_58f60c48_uniq" UNIQUE ("street_num", "street_name", "postcode_id");
ALTER TABLE "locations_address" ADD CONSTRAINT "locations_address_postcode_id_4b30f849_fk_locations" FOREIGN KEY ("postcode_id") REFERENCES "locations_postcode" ("postcode") ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "locations_address_address_id_bbbc9b69_like" ON "locations_address" ("address_id" varchar_pattern_ops);
CREATE INDEX "locations_address_postcode_id_4b30f849" ON "locations_address" ("postcode_id");
CREATE INDEX "locations_address_postcode_id_4b30f849_like" ON "locations_address" ("postcode_id" varchar_pattern_ops);
--
-- Create model Restaurant
--
CREATE TABLE "restaurants_restaurant" ("restaurant_id" varchar(50) NOT NULL PRIMARY KEY, "restaurant_name" varchar(50) NOT NULL, "price_range" varchar(4) NOT NULL, "address_id_id" varchar(50) NOT NULL);
--
-- Create model BestSellingItem
--
CREATE TABLE "restaurants_bestsellingitem" ("best_selling_item_id_id" varchar(50) NOT NULL PRIMARY KEY, "item_name" varchar(50) NOT NULL, "item_description" varchar(200) NOT NULL);
--
-- Create model Coordinates
--
CREATE TABLE "restaurants_coordinates" ("coordinates_id_id" varchar(50) NOT NULL PRIMARY KEY, "longitude" numeric(16, 12) NOT NULL, "latitude" numeric(16, 12) NOT NULL);
--
-- Create model RatingStats
--
CREATE TABLE "restaurants_ratingstats" ("rating_stats_id_id" varchar(50) NOT NULL PRIMARY KEY, "aggregate_rating" double precision NOT NULL, "review_count" integer NOT NULL, "recommended" boolean NOT NULL);
ALTER TABLE "restaurants_restaurant" ADD CONSTRAINT "restaurants_restaurant_restaurant_name_address__dc7db58a_uniq" UNIQUE ("restaurant_name", "address_id_id");
ALTER TABLE "restaurants_restaurant" ADD CONSTRAINT "restaurants_restaura_address_id_id_4716cd38_fk_locations" FOREIGN KEY ("address_id_id") REFERENCES "locations_address" ("address_id") ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "restaurants_restaurant_restaurant_id_8ddcf24b_like" ON "restaurants_restaurant" ("restaurant_id" varchar_pattern_ops);
CREATE INDEX "restaurants_restaurant_address_id_id_4716cd38" ON "restaurants_restaurant" ("address_id_id");
CREATE INDEX "restaurants_restaurant_address_id_id_4716cd38_like" ON "restaurants_restaurant" ("address_id_id" varchar_pattern_ops);
ALTER TABLE "restaurants_bestsellingitem" ADD CONSTRAINT "restaurants_bestsell_best_selling_item_id_9a3d9604_fk_restauran" FOREIGN KEY ("best_selling_item_id_id") REFERENCES "restaurants_restaurant" ("restaurant_id") ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "restaurants_bestsellingi_best_selling_item_id_id_9a3d9604_like" ON "restaurants_bestsellingitem" ("best_selling_item_id_id" varchar_pattern_ops);
ALTER TABLE "restaurants_coordinates" ADD CONSTRAINT "restaurants_coordina_coordinates_id_id_5c1c3ad5_fk_restauran" FOREIGN KEY ("coordinates_id_id") REFERENCES "restaurants_restaurant" ("restaurant_id") ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "restaurants_coordinates_coordinates_id_id_5c1c3ad5_like" ON "restaurants_coordinates" ("coordinates_id_id" varchar_pattern_ops);
ALTER TABLE "restaurants_ratingstats" ADD CONSTRAINT "restaurants_ratingst_rating_stats_id_id_4b2566be_fk_restauran" FOREIGN KEY ("rating_stats_id_id") REFERENCES "restaurants_restaurant" ("restaurant_id") ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "restaurants_ratingstats_rating_stats_id_id_4b2566be_like" ON "restaurants_ratingstats" ("rating_stats_id_id" varchar_pattern_ops);
--
-- Alter field city on postcode
--
ALTER TABLE "locations_postcode" ALTER COLUMN "city" TYPE varchar(50);
--
-- Alter field state on postcode
--
ALTER TABLE "locations_postcode" ALTER COLUMN "state" TYPE varchar(50);
--
-- Alter field city on postcode
--
ALTER TABLE "locations_postcode" ALTER COLUMN "city" TYPE varchar(100);
--
-- Alter field state on postcode
--
ALTER TABLE "locations_postcode" ALTER COLUMN "state" TYPE varchar(100);
--
-- Alter unique_together for postcode (0 constraint(s))
--
ALTER TABLE "locations_postcode" DROP CONSTRAINT "locations_postcode_city_state_country_id_ef0ab36c_uniq";
--
-- Alter field address_id on address
--
ALTER TABLE "locations_address" ALTER COLUMN "address_id" TYPE varchar(100);
--
-- Alter field street_name on address
--
ALTER TABLE "locations_address" ALTER COLUMN "street_name" TYPE varchar(100);
--
-- Alter field street_num on address
--
ALTER TABLE "locations_address" ALTER COLUMN "street_num" TYPE varchar(100);
--
-- Alter field postcode on postcode
--
SET CONSTRAINTS "locations_address_postcode_id_4b30f849_fk_locations" IMMEDIATE; ALTER TABLE "locations_address" DROP CONSTRAINT "locations_address_postcode_id_4b30f849_fk_locations";
ALTER TABLE "locations_postcode" ALTER COLUMN "postcode" TYPE varchar(100);
ALTER TABLE "locations_address" ALTER COLUMN "postcode_id" TYPE varchar(100) USING "postcode_id"::varchar(100);
ALTER TABLE "locations_address" ADD CONSTRAINT "locations_address_postcode_id_4b30f849_fk_locations" FOREIGN KEY ("postcode_id") REFERENCES "locations_postcode" ("postcode") ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED;
--
-- Alter field item_name on bestsellingitem
--
ALTER TABLE "restaurants_bestsellingitem" ALTER COLUMN "item_name" TYPE varchar(100);
--
-- Alter field restaurant_name on restaurant
--
ALTER TABLE "restaurants_restaurant" ALTER COLUMN "restaurant_name" TYPE varchar(100);
--
-- Alter field price_range on restaurant
--
ALTER TABLE "restaurants_restaurant" ALTER COLUMN "price_range" TYPE varchar(10);
--
-- Create model ManagerAccount
--
CREATE TABLE "restaurant_management_manageraccount" ("username" varchar(20) NOT NULL PRIMARY KEY, "password" varchar(100) NOT NULL);
--
-- Create model MatchManagerToRestaurant
--
CREATE TABLE "restaurant_management_matchmanagertorestaurant" ("restaurant_id" varchar(50) NOT NULL PRIMARY KEY, "manager_id" varchar(20) NOT NULL);
CREATE INDEX "restaurant_management_manageraccount_username_6102326e_like" ON "restaurant_management_manageraccount" ("username" varchar_pattern_ops);
ALTER TABLE "restaurant_management_matchmanagertorestaurant" ADD CONSTRAINT "restaurant_managemen_restaurant_id_350b6f37_fk_restauran" FOREIGN KEY ("restaurant_id") REFERENCES "restaurants_restaurant" ("restaurant_id") ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "restaurant_management_matchmanagertorestaurant" ADD CONSTRAINT "restaurant_managemen_manager_id_bdff5ada_fk_restauran" FOREIGN KEY ("manager_id") REFERENCES "restaurant_management_manageraccount" ("username") ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "restaurant_management_ma_restaurant_id_350b6f37_like" ON "restaurant_management_matchmanagertorestaurant" ("restaurant_id" varchar_pattern_ops);
CREATE INDEX "restaurant_management_matc_manager_id_bdff5ada" ON "restaurant_management_matchmanagertorestaurant" ("manager_id");
CREATE INDEX "restaurant_management_ma_manager_id_bdff5ada_like" ON "restaurant_management_matchmanagertorestaurant" ("manager_id" varchar_pattern_ops);
--
-- Create model FoodBank
--
CREATE TABLE "charities_foodbank" ("food_bank" varchar(100) PRIMARY KEY);
CREATE INDEX "charities_foodbank_food_bank_idx" ON "charities_foodbank" ("food_bank" varchar_pattern_ops);
--
-- Create model FoodBankDonation
--
CREATE TABLE "restaurants_foodbankdonation" ("food_bank" varchar(100) NOT NULL, "restaurant_id_id" varchar(50) NOT NULL);
ALTER TABLE "restaurants_foodbankdonation" ADD CONSTRAINT "restaurants_foodbankdonation_pk" PRIMARY KEY ("food_bank", "restaurant_id_id");
ALTER TABLE "restaurants_foodbankdonation" ADD CONSTRAINT "restaurants_foodbankdonation_restaurant_id_id_fk_restaurant" FOREIGN KEY ("restaurant_id_id") REFERENCES "restaurants_restaurant" ("restaurant_id") ON DELETE CASCADE;
ALTER TABLE "restaurants_foodbankdonation" ADD CONSTRAINT "restaurants_foodbankdonation_food_bank_fk_foodbank" FOREIGN KEY ("food_bank") REFERENCES "charities_foodbank" ("food_bank") ON DELETE CASCADE;
CREATE INDEX "restaurants_foodbankdonation_food_bank_idx" ON "restaurants_foodbankdonation" ("food_bank" varchar_pattern_ops);
CREATE INDEX "restaurants_foodbankdonation_restaurant_id_id_idx" ON "restaurants_foodbankdonation" ("restaurant_id_id" varchar_pattern_ops);
--
-- Create model ImageURL
--
CREATE TABLE "restaurants_imageurl" ("restaurant_id_id" varchar(50) PRIMARY KEY, "image_url" varchar(500) NOT NULL);
ALTER TABLE "restaurants_imageurl" ADD CONSTRAINT "restaurants_imageurl_fk_restaurant" FOREIGN KEY ("restaurant_id_id") REFERENCES "restaurants_restaurant" ("restaurant_id") ON DELETE CASCADE;
CREATE INDEX "restaurants_imageurl_restaurant_id_idx" ON "restaurants_imageurl" ("restaurant_id_id" varchar_pattern_ops);
CREATE INDEX "restaurants_imageurl_image_url_idx" ON "restaurants_imageurl" ("image_url" varchar_pattern_ops);
```

#### Sample SQL Queries

```sql
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
```
