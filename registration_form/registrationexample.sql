CREATE DATABASE registrationexample;
USE registrationexample;

CREATE TABLE ticket (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255),
    user_lastname VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(20),
    user_password VARCHAR(255),
    zone_id INT,
    user_comments VARCHAR(255)
);
-- ALTER TABLE ticket CHANGE username user_lastname VARCHAR(255);
CREATE TABLE event_zone (
    id INT AUTO_INCREMENT PRIMARY KEY,
    zone_name VARCHAR(255)
);
-- ALTER TABLE zone RENAME TO event_zone
INSERT INTO event_zone (id, zone_name) VALUES 
					   (DEFAULT, 'Super VIP'),
                       (DEFAULT, 'VIP'),
                       (DEFAULT, 'GENERAL');
SELECT * FROM event_zone;
INSERT INTO ticket (id, user_name, user_lastname, email, phone, user_password, zone_id, user_comments) VALUES 
				   (DEFAULT, 'test', 'test', 'test@test', '999999999', '#########', '1', 'test');
SELECT * FROM ticket;

