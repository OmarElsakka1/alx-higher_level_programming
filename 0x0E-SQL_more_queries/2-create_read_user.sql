-- creating a database called hbtn_0d_2 and a user called user_0d_2
-- user_0d_2 has SELECT PRIVILEGE on the hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
    ON hbtn_0d_2.*
    TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
