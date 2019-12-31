DELIMITER ;;

CREATE FUNCTION number_of_users ( 
    starting_value INT
)
RETURNS INT
READS SQL DATA
BEGIN

   DECLARE nr INT;

   SELECT COUNT(*) INTO nr FROM user;

   RETURN nr;

END;;
