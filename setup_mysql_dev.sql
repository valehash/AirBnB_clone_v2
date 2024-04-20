--create the database if hbnb_dev_db if not EXISTS
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

--create the database performance_schema if it does not exists
CREATE DATABASE IF NOT EXISTS performance_schema;

-- sql code to create a user with a passowrd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grants the user all priviledges
GRANT ALL PRIVILEGES ON hbnb_dev_db to 'hbnb_dev'@'localhost';

-- grant select priviledges to hbnb_dev on performance shcema db
GRANT SELECT PRIVILEGES ON performance_schema to 'hbnb_dev'@'localhost';
