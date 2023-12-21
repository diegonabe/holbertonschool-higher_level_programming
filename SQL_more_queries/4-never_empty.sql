-- Write a script that creates the table id_not_nul
-- table done with attributes id and name.
CREATE TABLE IF NOT EXISTS id_not_null (id INT NOT NULL DEFAULT 1,
name VARCHAR(256));
