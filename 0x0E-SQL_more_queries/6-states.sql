-- creates 'hbtn_0d_usa' database and table 'states' in the database
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
id INT UNIQUE NOT NULL AUTO_INCREMENT,
name VARCHAR(256),
PRIMARY KEY (id)
);
