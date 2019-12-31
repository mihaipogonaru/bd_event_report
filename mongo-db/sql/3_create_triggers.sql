DELIMITER ;;

CREATE TRIGGER monitor_city_insert
BEFORE INSERT ON city FOR EACH ROW
BEGIN
    DECLARE county_name VARCHAR(50);
    DECLARE county_lat DECIMAL(8,5);
    DECLARE county_longi DECIMAL(8,5);
    DECLARE county_radius DECIMAL(10,5);
    DECLARE error VARCHAR(255);

    SELECT name, lat, longi, radius INTO county_name, county_lat, county_longi, county_radius
    FROM county WHERE name = new.county;
    
    IF SQRT(POW((county_lat - new.lat), 2) + POW((county_longi - new.longi), 2)) > county_radius
    THEN
        SET error = CONCAT("Orasul ", new.name, " trebuie sa fie in raza judetului ", county_name);
        SIGNAL SQLSTATE "45000" SET MESSAGE_TEXT = error;
    END IF;
END;;

CREATE TRIGGER monitor_city_update
BEFORE UPDATE ON city FOR EACH ROW
BEGIN
    DECLARE county_name VARCHAR(50);
    DECLARE county_lat DECIMAL(8,5);
    DECLARE county_longi DECIMAL(8,5);
    DECLARE county_radius DECIMAL(10,5);
    DECLARE error VARCHAR(255);

    SELECT name, lat, longi, radius INTO county_name, county_lat, county_longi, county_radius
    FROM county WHERE name = new.county;
    
    IF SQRT(POW((county_lat - new.lat), 2) + POW((county_longi - new.longi), 2)) > county_radius
    THEN
        SET error = CONCAT("Orasul ", new.name, " trebuie sa fie in raza judetului ", county_name);
        SIGNAL SQLSTATE "45000" SET MESSAGE_TEXT = error;
    END IF;
END;;

CREATE TRIGGER monitor_county_update
BEFORE UPDATE ON county FOR EACH ROW
BEGIN
    DECLARE city_name VARCHAR(50);
    DECLARE city_lat DECIMAL(8,5);
    DECLARE city_longi DECIMAL(8,5);
    DECLARE error VARCHAR(255);

    DECLARE done BOOLEAN DEFAULT FALSE;
    DECLARE city_cur CURSOR FOR SELECT name, lat, longi FROM city WHERE county = new.name;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN city_cur;

    city_loop:
    LOOP
        FETCH city_cur INTO city_name, city_lat, city_longi;

        IF done THEN
        LEAVE city_loop;
        END IF;

        IF SQRT(POW((city_lat - new.lat), 2) + POW((city_longi - new.longi), 2)) > new.radius
        THEN
            SET error = CONCAT("Judetul ", new.name, " trebuie sa cuprinda orasul ", city_name);
            SIGNAL SQLSTATE "45000" SET MESSAGE_TEXT = error;
        END IF;
    END LOOP;

    CLOSE city_cur;
END;;
