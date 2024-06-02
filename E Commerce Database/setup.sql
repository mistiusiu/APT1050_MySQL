-- script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS ecommerce;
CREATE USER IF NOT EXISTS 'misati'@'%' IDENTIFIED BY 'misati_pwd';
GRANT SELECT ON performance_schema.* TO 'misati'@'%';
GRANT ALL PRIVILEGES ON ecommerce.* TO 'misati'@'%';
FLUSH PRIVILEGES;
