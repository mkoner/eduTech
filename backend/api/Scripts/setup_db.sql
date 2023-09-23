-- Run this script to setup a database environment for eduTech locally
-- This script works for postgresql
-- To run => cat setup_db.sql | psql

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS edutech;

-- Create the user if it doesn't exist and set the password
CREATE USER IF NOT EXISTS edutech_user WITH PASSWORD '@edutech_001';

-- Grant all privileges on the "edutech" database to the user
GRANT ALL PRIVILEGES ON DATABASE edutech TO edutech_user;

-- Grant SELECT privilege on the "performance_schema" schema to the user
GRANT SELECT ON SCHEMA performance_schema TO edutech_user;