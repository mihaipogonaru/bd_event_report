import sys
import os

from app.database import Database

counties = {
    'Alba': ('Alba Iulia', 46.0718, 23.5730, 6.2),
    'Bucuresti': ('Bucuresti', 44.267, 26.610, 0.2),
    'Cluj': ('Cluj-Napoca', 46.46, 23.35, 6.6),
    'Timis': ('Timisoara', 45.4758, 21.1738, 8.7),
    'Iasi': ('Iasi', 47.944, 27.352, 5.5),
    'Constanta': ('Constanta', 44.1024, 28.3818, 7.1),
    'Dolj': ('Craiova', 44.20, 27.35, 7.4),
    'Brasov': ('Brasov', 45.39, 25.36, 5.3),
    'Galati': ('Galati', 45.26, 28.24, 4.5),
    'Arges': ('Pitesti', 44.5624, 26.148, 6.8),
    'Bihor': ('Oradea', 47.0420, 21.5516, 7.6),
    'Braila': ('Braila', 45.169, 27.5727, 4.7),
    'Arad': ('Arad', 46.1036, 21.184, 7.7),
    'Prahova': ('Ploiesti', 44.5138, 24.524, 4.7),
    'Sibiu': ('Sibiu', 45.4745, 24.98, 5.4),
    'Bacau': ('Bacau', 46.35, 26.55, 6.6)
}

def insert_test_counties():
    for county, (city, lat, longi, rad) in counties.items():
        try:
            Database.insert_county(county, lat, longi, rad)
            Database.insert_city(city, lat, longi, rad / 10, county)
        except Exception as e:
            print(e)
            continue

if __name__ == '__main__':
    print("Adding counties")
    insert_test_counties()
    print("Done adding counties")
