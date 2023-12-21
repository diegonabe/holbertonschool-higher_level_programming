-- write a script that makes a database and a tablle
-- make the database first
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- make a table and let it have default and unique constants
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL);
