create database if not exists event_reporter;
use event_reporter;

create table if not exists user (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(128) NOT NULL
);
