-- Create a trigger that resets valid_email when email is changed
DELIMITER $$

CREATE TRIGGER before_users_update
BEFORE UPDATE ON users

FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;