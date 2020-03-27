--
-- Create model Country
--

CREATE TABLE "locations_country" ("country_name" varchar(20) NOT NULL PRIMARY KEY);

--
-- Create model Postcode
--

CREATE TABLE "locations_postcode" ("postcode" varchar(10) NOT NULL PRIMARY KEY,
                                                                           "city" varchar(20) NOT NULL,
                                                                                              "state" varchar(20) NOT NULL,
                                                                                                                  "country_id" varchar(20) NOT NULL);

--
-- Create model Address
--

CREATE TABLE "locations_address" ("id" serial NOT NULL PRIMARY KEY,
                                                               "street_num" varchar(10) NOT NULL,
                                                                                        "street_name" varchar(30) NOT NULL,
                                                                                                                  "postcode_id" varchar(10) NOT NULL);


CREATE INDEX "locations_country_country_name_162e2e27_like" ON "locations_country" ("country_name" varchar_pattern_ops);


ALTER TABLE "locations_postcode" ADD CONSTRAINT "locations_postcode_country_id_e1f4da17_fk_locations"
FOREIGN KEY ("country_id") REFERENCES "locations_country" ("country_name") DEFERRABLE INITIALLY DEFERRED;


CREATE INDEX "locations_postcode_postcode_21c425e3_like" ON "locations_postcode" ("postcode" varchar_pattern_ops);


CREATE INDEX "locations_postcode_country_id_e1f4da17" ON "locations_postcode" ("country_id");


CREATE INDEX "locations_postcode_country_id_e1f4da17_like" ON "locations_postcode" ("country_id" varchar_pattern_ops);


ALTER TABLE "locations_address" ADD CONSTRAINT "locations_address_postcode_id_4b30f849_fk_locations"
FOREIGN KEY ("postcode_id") REFERENCES "locations_postcode" ("postcode") DEFERRABLE INITIALLY DEFERRED;


CREATE INDEX "locations_address_postcode_id_4b30f849" ON "locations_address" ("postcode_id");


CREATE INDEX "locations_address_postcode_id_4b30f849_like" ON "locations_address" ("postcode_id" varchar_pattern_ops);

--
-- Create model BestSellerItem
--

CREATE TABLE "restaurants_bestselleritem" ("item_name" varchar(50) NOT NULL PRIMARY KEY,
                                                                                    "item_type" varchar(20) NOT NULL);

--
-- Create model FoodCategory
--

CREATE TABLE "restaurants_foodcategory" ("food_category_name" varchar(20) NOT NULL PRIMARY KEY,
                                                                                           "disclaimer" varchar(200) NOT NULL);

--
-- Create model RecommendationBenchmark
--

CREATE TABLE "restaurants_recommendationbenchmark" ("id" serial NOT NULL PRIMARY KEY,
                                                                                 "rating" integer NOT NULL,
                                                                                                  "num_of_reviews" integer NOT NULL,
                                                                                                                           "recommended" varchar(3) NOT NULL);

--
-- Create model EstablishmentType
--

CREATE TABLE "restaurants_establishmenttype" ("id" serial NOT NULL PRIMARY KEY,
                                                                           "atmosphere" varchar(20) NOT NULL,
                                                                                                    "food_category_name_id" varchar(20) NOT NULL UNIQUE);

--
-- Create model Cuisine
--

CREATE TABLE "restaurants_cuisine" ("id" serial NOT NULL PRIMARY KEY,
                                                                 "nationality" varchar(20) NOT NULL,
                                                                                           "food_category_name_id" varchar(20) NOT NULL UNIQUE);


CREATE INDEX "restaurants_bestselleritem_item_name_104e03ee_like" ON "restaurants_bestselleritem" ("item_name" varchar_pattern_ops);


CREATE INDEX "restaurants_foodcategory_food_category_name_288935da_like" ON "restaurants_foodcategory" ("food_category_name" varchar_pattern_ops);


ALTER TABLE "restaurants_establishmenttype" ADD CONSTRAINT "restaurants_establis_food_category_name_i_6d8f2ffb_fk_restauran"
FOREIGN KEY ("food_category_name_id") REFERENCES "restaurants_foodcategory" ("food_category_name") DEFERRABLE INITIALLY DEFERRED;


CREATE INDEX "restaurants_establishmen_food_category_name_id_6d8f2ffb_like" ON "restaurants_establishmenttype" ("food_category_name_id" varchar_pattern_ops);


ALTER TABLE "restaurants_cuisine" ADD CONSTRAINT "restaurants_cuisine_food_category_name_i_a8d0af94_fk_restauran"
FOREIGN KEY ("food_category_name_id") REFERENCES "restaurants_foodcategory" ("food_category_name") DEFERRABLE INITIALLY DEFERRED;


CREATE INDEX "restaurants_cuisine_food_category_name_id_a8d0af94_like" ON "restaurants_cuisine" ("food_category_name_id" varchar_pattern_ops);