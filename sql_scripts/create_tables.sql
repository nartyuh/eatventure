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
ALTER TABLE "locations_postcode" ADD CONSTRAINT "locations_postcode_country_id_e1f4da17_fk_locations" FOREIGN KEY ("country_id") REFERENCES "locations_country" ("country_name") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "locations_postcode_postcode_21c425e3_like" ON "locations_postcode" ("postcode" varchar_pattern_ops);
CREATE INDEX "locations_postcode_country_id_e1f4da17" ON "locations_postcode" ("country_id");
CREATE INDEX "locations_postcode_country_id_e1f4da17_like" ON "locations_postcode" ("country_id" varchar_pattern_ops);
ALTER TABLE "locations_address" ADD CONSTRAINT "locations_address_street_num_street_name_p_58f60c48_uniq" UNIQUE ("street_num", "street_name", "postcode_id");
ALTER TABLE "locations_address" ADD CONSTRAINT "locations_address_postcode_id_4b30f849_fk_locations" FOREIGN KEY ("postcode_id") REFERENCES "locations_postcode" ("postcode") DEFERRABLE INITIALLY DEFERRED;
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
ALTER TABLE "restaurants_restaurant" ADD CONSTRAINT "restaurants_restaura_address_id_id_4716cd38_fk_locations" FOREIGN KEY ("address_id_id") REFERENCES "locations_address" ("address_id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "restaurants_restaurant_restaurant_id_8ddcf24b_like" ON "restaurants_restaurant" ("restaurant_id" varchar_pattern_ops);
CREATE INDEX "restaurants_restaurant_address_id_id_4716cd38" ON "restaurants_restaurant" ("address_id_id");
CREATE INDEX "restaurants_restaurant_address_id_id_4716cd38_like" ON "restaurants_restaurant" ("address_id_id" varchar_pattern_ops);
ALTER TABLE "restaurants_bestsellingitem" ADD CONSTRAINT "restaurants_bestsell_best_selling_item_id_9a3d9604_fk_restauran" FOREIGN KEY ("best_selling_item_id_id") REFERENCES "restaurants_restaurant" ("restaurant_id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "restaurants_bestsellingi_best_selling_item_id_id_9a3d9604_like" ON "restaurants_bestsellingitem" ("best_selling_item_id_id" varchar_pattern_ops);
ALTER TABLE "restaurants_coordinates" ADD CONSTRAINT "restaurants_coordina_coordinates_id_id_5c1c3ad5_fk_restauran" FOREIGN KEY ("coordinates_id_id") REFERENCES "restaurants_restaurant" ("restaurant_id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "restaurants_coordinates_coordinates_id_id_5c1c3ad5_like" ON "restaurants_coordinates" ("coordinates_id_id" varchar_pattern_ops);
ALTER TABLE "restaurants_ratingstats" ADD CONSTRAINT "restaurants_ratingst_rating_stats_id_id_4b2566be_fk_restauran" FOREIGN KEY ("rating_stats_id_id") REFERENCES "restaurants_restaurant" ("restaurant_id") DEFERRABLE INITIALLY DEFERRED;
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
ALTER TABLE "locations_address" ADD CONSTRAINT "locations_address_postcode_id_4b30f849_fk" FOREIGN KEY ("postcode_id") REFERENCES "locations_postcode" ("postcode") DEFERRABLE INITIALLY DEFERRED;
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