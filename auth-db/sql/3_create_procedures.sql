DELIMITER ;;

CREATE PROCEDURE insert_user(
    IN email_a VARCHAR(50),
    IN password_a VARCHAR(128)
)
BEGIN
    INSERT INTO user(email, password)
    VALUES (email_a, password_a);
END;;

CREATE PROCEDURE select_user(
    IN email_a VARCHAR(50)
)
BEGIN
    SELECT * FROM user WHERE email = email_a;
END;;

CREATE PROCEDURE delete_user(
    IN email_a VARCHAR(50)
)
BEGIN
    DELETE FROM user WHERE email=email_a;
END;;

CREATE PROCEDURE get_users()
BEGIN
    SELECT * FROM user;
END;;
