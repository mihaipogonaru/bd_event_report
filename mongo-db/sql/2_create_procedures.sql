DELIMITER ;;

CREATE PROCEDURE insert_county(
    IN name_a VARCHAR(50),
    IN lat_a DECIMAL(8,5),
    IN longi_a DECIMAL(8,5),
    IN radius_a DECIMAL(10,5)
)
BEGIN
    INSERT INTO county(name, lat, longi, radius)
    VALUES (name_a, lat_a, longi_a, radius_a);
END;;

CREATE PROCEDURE select_county(
    IN name_a VARCHAR(50)
)
BEGIN
    SELECT * FROM county WHERE name = name_a;
END;;

CREATE PROCEDURE update_county_radius(
    IN name_a VARCHAR(50),
    IN radius_a DECIMAL(10,5)
)
BEGIN
    UPDATE county SET radius=radius_a WHERE name=name_a;
END;;

CREATE PROCEDURE delete_county(
    IN name_a VARCHAR(50)
)
BEGIN
    DELETE FROM county WHERE name=name_a;
END;;

CREATE PROCEDURE get_counties()
BEGIN
    SELECT * FROM county;
END;;

CREATE PROCEDURE insert_city(
    IN name_a VARCHAR(50),
    IN lat_a DECIMAL(8,5),
    IN longi_a DECIMAL(8,5),
    IN radius_a DECIMAL(10,5),
    IN county_a VARCHAR(50)
)
BEGIN
    INSERT INTO city(name, lat, longi, radius, county)
    VALUES (name_a, lat_a, longi_a, radius_a, county_a);
END;;

CREATE PROCEDURE select_city(
    IN name_a VARCHAR(50)
)
BEGIN
    SELECT * FROM city WHERE name = name_a;
END;;

CREATE PROCEDURE update_city_radius(
    IN name_a VARCHAR(50),
    IN radius_a DECIMAL(10,5)
)
BEGIN
    UPDATE city SET radius=radius_a WHERE name=name_a;
END;;

CREATE PROCEDURE delete_city(
    IN name_a VARCHAR(50)
)
BEGIN
    DELETE FROM city WHERE name=name_a;
END;;

CREATE PROCEDURE get_cities()
BEGIN
    SELECT * FROM city;
END;;

CREATE PROCEDURE insert_birth(
    IN pin_a BIGINT UNSIGNED,
    IN surname_a VARCHAR(50),
    IN name_a VARCHAR(50),
    IN date_a DATETIME,
    IN city_a VARCHAR(50)
)
BEGIN
    INSERT INTO birth(pin, surname, name, date, city)
    VALUES (pin_a, surname_a, name_a, date_a, city_a);
END;;

CREATE PROCEDURE select_birth(
    IN pin_a VARCHAR(50)
)
BEGIN
    SELECT * FROM birth WHERE pin = pin_a;
END;;

CREATE PROCEDURE get_births_in_county(
    IN county_name VARCHAR(50)
)
BEGIN
    SELECT * FROM birth
    WHERE
        city IN (SELECT name FROM city WHERE county = county_name);
END;;

CREATE PROCEDURE get_births_in_city(
    IN city_name VARCHAR(50)
)
BEGIN
    SELECT * FROM birth
    WHERE city = city_name;
END;;

CREATE PROCEDURE get_births_between(
    IN begin_date DATETIME,
    IN end_date DATETIME
)
BEGIN
    SELECT * FROM birth
    WHERE begin_date <= date AND end_date >= date;
END;;

CREATE PROCEDURE insert_death(
    IN person_a BIGINT UNSIGNED,
    IN date_a DATETIME,
    IN city_a VARCHAR(50)
)
BEGIN
    INSERT INTO death(person, date, city)
    VALUES (person_a, date_a, city_a);
END;;

CREATE PROCEDURE select_death(
    IN person_a VARCHAR(50)
)
BEGIN
    SELECT * FROM death WHERE person = person_a;
END;;

CREATE PROCEDURE get_deaths_in_county(
    IN county_name VARCHAR(50)
)
BEGIN
    SELECT * FROM death
    WHERE city IN (SELECT name FROM city WHERE county = county_name);
END;;

CREATE PROCEDURE get_deaths_in_city(
    IN city_name VARCHAR(50)
)
BEGIN
    SELECT * FROM death
    WHERE city = city_name;
END;;

CREATE PROCEDURE get_deaths_between(
    IN begin_date DATETIME,
    IN end_date DATETIME
)
BEGIN
    SELECT * FROM death
    WHERE begin_date <= date AND end_date >= date;
END;;
