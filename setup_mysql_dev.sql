
--create the database if hbnb_dev_db if not EXISTS
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- creates a user if it does not exist and gives a password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
--graants permissions to the user on hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
--grants onlt select permistions to the useron performance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
--flush priviledges for changes to take effect
FLUSH PRIVILEGES;
