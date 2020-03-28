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

CREATE TABLE "locations_address" ("address_id" serial NOT NULL PRIMARY KEY,
                                                                       "unit_num" varchar(10) NULL,
                                                                                              "street_num" varchar(10) NOT NULL,
                                                                                                                       "street_name" varchar(30) NOT NULL,
                                                                                                                                                 "postcode_id" varchar(10) NOT NULL);


CREATE INDEX "locations_country_country_name_162e2e27_like" ON "locations_country" ("country_name" varchar_pattern_ops);


ALTER TABLE "locations_postcode" ADD CONSTRAINT "locations_postcode_country_id_e1f4da17_fk_locations"
FOREIGN KEY ("country_id") REFERENCES "locations_country" ("country_name") DEFERRABLE INITIALLY DEFERRED;


CREATE INDEX "locations_postcode_postcode_21c425e3_like" ON "locations_postcode" ("postcode" varchar_pattern_ops);


CREATE INDEX "locations_postcode_country_id_e1f4da17" ON "locations_postcode" ("country_id");


CREATE INDEX "locations_postcode_country_id_e1f4da17_like" ON "locations_postcode" ("country_id" varchar_pattern_ops);


ALTER TABLE "locations_address" ADD CONSTRAINT "locations_address_unit_num_street_num_stre_4b135de5_uniq" UNIQUE ("unit_num",
                                                                                                                  "street_num",
                                                                                                                  "street_name",
                                                                                                                  "postcode_id");


ALTER TABLE "locations_address" ADD CONSTRAINT "locations_address_postcode_id_4b30f849_fk_locations"
FOREIGN KEY ("postcode_id") REFERENCES "locations_postcode" ("postcode") DEFERRABLE INITIALLY DEFERRED;


CREATE INDEX "locations_address_postcode_id_4b30f849" ON "locations_address" ("postcode_id");


CREATE INDEX "locations_address_postcode_id_4b30f849_like" ON "locations_address" ("postcode_id" varchar_pattern_ops);

--
-- Create model BestSellingItem
--

CREATE TABLE "restaurants_bestsellingitem" ("item_id" serial NOT NULL PRIMARY KEY,
                                                                              "item_name" varchar(50) NOT NULL,
                                                                                                      "item_description" varchar(200) NOT NULL);

--
-- Create model Cuisine
--

CREATE TABLE "restaurants_cuisine" ("cuisine_id" serial NOT NULL PRIMARY KEY,
                                                                         "nationality" varchar(20) NOT NULL);

--
-- Create model EstablishmentType
--

CREATE TABLE "restaurants_establishmenttype" ("establishment_type_id" serial NOT NULL PRIMARY KEY,
                                                                                              "atmosphere" varchar(20) NOT NULL);

--
-- Create model FoodCategory
--

CREATE TABLE "restaurants_foodcategory" ("food_category_name" varchar(20) NOT NULL PRIMARY KEY,
                                                                                           "disclaimer" varchar(200) NOT NULL);

--
-- Create model RatingStats
--

CREATE TABLE "restaurants_ratingstats" ("rating_stats_id" serial NOT NULL PRIMARY KEY,
                                                                                  "rating" integer NOT NULL,
                                                                                                   "num_of_reviews" integer NOT NULL,
                                                                                                                            "recommended" boolean NOT NULL);

--
-- Create model Restaurant
--

CREATE TABLE "restaurants_restaurant" ("restaurant_id" serial NOT NULL PRIMARY KEY,
                                                                               "restaurant_name" varchar(20) NOT NULL,
                                                                                                             "price_range" varchar(4) NOT NULL,
                                                                                                                                      "address_id_id" integer NOT NULL,
                                                                                                                                                              "best_selling_item_id" integer NULL UNIQUE,
                                                                                                                                                                                                  "cuisine_id" integer NULL,
                                                                                                                                                                                                                       "establishment_type_id" integer NULL,
                                                                                                                                                                                                                                                       "food_category_id" varchar(20) NULL,
                                                                                                                                                                                                                                                                                      "rating_stats_id_id" integer NULL UNIQUE);

--
-- Add field food_category_name to establishmenttype
--

ALTER TABLE "restaurants_establishmenttype" ADD COLUMN "food_category_name_id" varchar(20) NOT NULL CONSTRAINT "restaurants_establis_food_category_name_i_6d8f2ffb_fk_restauran" REFERENCES "restaurants_foodcategory"("food_category_name") DEFERRABLE INITIALLY DEFERRED;


SET CONSTRAINTS "restaurants_establis_food_category_name_i_6d8f2ffb_fk_restauran" IMMEDIATE;

--
-- Add field food_category_name to cuisine
--

ALTER TABLE "restaurants_cuisine" ADD COLUMN "food_category_name_id" varchar(20) NOT NULL CONSTRAINT "restaurants_cuisine_food_category_name_i_a8d0af94_fk_restauran" REFERENCES "restaurants_foodcategory"("food_category_name") DEFERRABLE INITIALLY DEFERRED;


SET CONSTRAINTS "restaurants_cuisine_food_category_name_i_a8d0af94_fk_restauran" IMMEDIATE;

--
-- Alter unique_together for establishmenttype (1 constraint(s))
--

ALTER TABLE "restaurants_establishmenttype" ADD CONSTRAINT "restaurants_establishmen_food_category_name_id_at_4102edc5_uniq" UNIQUE ("food_category_name_id",
                                                                                                                                     "atmosphere");

--
-- Create model Discount
--

CREATE TABLE "restaurants_discount" ("id" serial NOT NULL PRIMARY KEY,
                                                                  "discount_code" varchar(10) NOT NULL,
                                                                                              "expiry_date" timestamp with time zone NOT NULL,
                                                                                                                                     "details" varchar(200) NOT NULL,
                                                                                                                                                            "restaurant_id_id" integer NOT NULL);

--
-- Alter unique_together for cuisine (1 constraint(s))
--

ALTER TABLE "restaurants_cuisine" ADD CONSTRAINT "restaurants_cuisine_food_category_name_id_na_6aacf214_uniq" UNIQUE ("food_category_name_id",
                                                                                                                      "nationality");


CREATE INDEX "restaurants_foodcategory_food_category_name_288935da_like" ON "restaurants_foodcategory" ("food_category_name" varchar_pattern_ops);


ALTER TABLE "restaurants_restaurant" ADD CONSTRAINT "restaurants_restaurant_restaurant_name_address__dc7db58a_uniq" UNIQUE ("restaurant_name",
                                                                                                                            "address_id_id");


ALTER TABLE "restaurants_restaurant" ADD CONSTRAINT "restaurants_restaura_address_id_id_4716cd38_fk_locations"
FOREIGN KEY ("address_id_id") REFERENCES "locations_address" ("address_id") DEFERRABLE INITIALLY DEFERRED;


ALTER TABLE "restaurants_restaurant" ADD CONSTRAINT "restaurants_restaura_best_selling_item_id_406a7bbe_fk_restauran"
FOREIGN KEY ("best_selling_item_id") REFERENCES "restaurants_bestsellingitem" ("item_id") DEFERRABLE INITIALLY DEFERRED;


ALTER TABLE "restaurants_restaurant" ADD CONSTRAINT "restaurants_restaura_cuisine_id_889b7f54_fk_restauran"
FOREIGN KEY ("cuisine_id") REFERENCES "restaurants_cuisine" ("cuisine_id") DEFERRABLE INITIALLY DEFERRED;


ALTER TABLE "restaurants_restaurant" ADD CONSTRAINT "restaurants_restaura_establishment_type_i_da363596_fk_restauran"
FOREIGN KEY ("establishment_type_id") REFERENCES "restaurants_establishmenttype" ("establishment_type_id") DEFERRABLE INITIALLY DEFERRED;


ALTER TABLE "restaurants_restaurant" ADD CONSTRAINT "restaurants_restaura_food_category_id_241b51c6_fk_restauran"
FOREIGN KEY ("food_category_id") REFERENCES "restaurants_foodcategory" ("food_category_name") DEFERRABLE INITIALLY DEFERRED;


ALTER TABLE "restaurants_restaurant" ADD CONSTRAINT "restaurants_restaura_rating_stats_id_id_0da29e49_fk_restauran"
FOREIGN KEY ("rating_stats_id_id") REFERENCES "restaurants_ratingstats" ("rating_stats_id") DEFERRABLE INITIALLY DEFERRED;


CREATE INDEX "restaurants_restaurant_address_id_id_4716cd38" ON "restaurants_restaurant" ("address_id_id");


CREATE INDEX "restaurants_restaurant_cuisine_id_889b7f54" ON "restaurants_restaurant" ("cuisine_id");


CREATE INDEX "restaurants_restaurant_establishment_type_id_da363596" ON "restaurants_restaurant" ("establishment_type_id");


CREATE INDEX "restaurants_restaurant_food_category_id_241b51c6" ON "restaurants_restaurant" ("food_category_id");


CREATE INDEX "restaurants_restaurant_food_category_id_241b51c6_like" ON "restaurants_restaurant" ("food_category_id" varchar_pattern_ops);


CREATE INDEX "restaurants_establishmenttype_food_category_name_id_6d8f2ffb" ON "restaurants_establishmenttype" ("food_category_name_id");


CREATE INDEX "restaurants_establishmen_food_category_name_id_6d8f2ffb_like" ON "restaurants_establishmenttype" ("food_category_name_id" varchar_pattern_ops);


CREATE INDEX "restaurants_cuisine_food_category_name_id_a8d0af94" ON "restaurants_cuisine" ("food_category_name_id");


CREATE INDEX "restaurants_cuisine_food_category_name_id_a8d0af94_like" ON "restaurants_cuisine" ("food_category_name_id" varchar_pattern_ops);


ALTER TABLE "restaurants_discount" ADD CONSTRAINT "restaurants_discount_discount_code_restaurant_8a3e7de0_uniq" UNIQUE ("discount_code",
                                                                                                                        "restaurant_id_id");


ALTER TABLE "restaurants_discount" ADD CONSTRAINT "restaurants_discount_restaurant_id_id_07f77fbf_fk_restauran"
FOREIGN KEY ("restaurant_id_id") REFERENCES "restaurants_restaurant" ("restaurant_id") DEFERRABLE INITIALLY DEFERRED;


CREATE INDEX "restaurants_discount_restaurant_id_id_07f77fbf" ON "restaurants_discount" ("restaurant_id_id");