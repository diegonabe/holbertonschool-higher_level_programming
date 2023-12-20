-- Creates the user user_0d_1 with all privileges.
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grants all privileges on all databases to user_0d_1.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Flushes privileges to apply the changes.
FLUSH PRIVILEGES;
