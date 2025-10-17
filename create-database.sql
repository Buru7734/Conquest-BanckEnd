CREATE DATABASE conquest;

CREATE USER conquest_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE conquest TO conquest_admin;
