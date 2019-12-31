create database if not exists event_reporter;
use event_reporter;

create table if not exists county (
    name VARCHAR(50) PRIMARY KEY,
    lat DECIMAL(8,5) NOT NULL,
    longi DECIMAL(8,5) NOT NULL,
    radius DECIMAL(10,5) NOT NULL,
    UNIQUE KEY(lat, longi)
);

create table if not exists city (
    name VARCHAR(50) PRIMARY KEY,
    lat DECIMAL(8,5) NOT NULL,
    longi DECIMAL(8,5) NOT NULL,
    radius DECIMAL(10,5) NOT NULL,
    county VARCHAR(50) NOT NULL,
    UNIQUE KEY(lat, longi),
    FOREIGN KEY(county) REFERENCES county(name)
);

create table if not exists birth (
    pin BIGINT UNSIGNED PRIMARY KEY,
    surname VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    date DATETIME NOT NULL,
    city VARCHAR(50) NOT NULL,
    FOREIGN KEY(city) REFERENCES city(name)
);

create table if not exists death (
    person BIGINT UNSIGNED PRIMARY KEY,
    date DATETIME NOT NULL,
    city VARCHAR(50) NOT NULL,
    FOREIGN KEY(person) REFERENCES birth(pin),
    FOREIGN KEY(city) REFERENCES city(name)
);
