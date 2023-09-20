-- Run this script to setup a database environment for eduTech locally

CREATE DATABASE IF NOT EXISTS edutech;
CREATE USER IF NOT EXISTS 'edutech_user'@'localhost' IDENTIFIED BY '@edutech_001';
GRANT ALL PRIVILEGES ON `edutech`.* TO 'edutech_user'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'edutech_user'@'localhost';
FLUSH PRIVILEGES;