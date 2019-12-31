import sys
import os

from database import Database

import json

def modify_users():
    print('Introdu: 1.{}\n2.{}\n3.{}\n4.{}'.
        format('Adauga un user', 'Sterge un user', 'Afiseaza userii', 'Revenire'))

    opt = int(input())

    if opt == 1:
        print('Introdu: email si parola')
        Database.insert_user(input(), input())
    elif opt == 2:
        print('Introdu: email')
        Database.delete_user(input())
    elif opt == 3:
        print('\n'.join(str(x) for x in Database.get_users()))

def modify_counties():
    print('Introdu: 1.{}\n2.{}\n3.{}\n4.{}\n5.{}'.format(
        'Adauga un judet', 'Modifica raza unui judet', 'Sterge un judet', 'Afiseaza judetele', 'Revenire'))

    opt = int(input())

    if opt == 1:
        print('Introdu: nume, latitudine, longitudine si raza')
        Database.insert_county(input(), float(input()), float(input()), float(input()))
    elif opt == 2:
        print('Introdu: nume si raza')
        Database.update_county_radius(input(), float(input()))
    elif opt == 3:
        print('Introdu: nume')
        Database.delete_county(input())
    elif opt == 4:
        print('\n'.join(str(x) for x in Database.get_counties()))

def modify_cities():
    print('Introdu: 1.{}\n2.{}\n3.{}\n4.{}\n5.{}'.format(
        'Adauga un oras', 'Modifica raza unui oras', 'Sterge un oras', 'Afiseaza orasele', 'Revenire'))

    opt = int(input())

    if opt == 1:
        print('Introdu: nume, latitudine, longitudine, raza si judet')
        Database.insert_city(input(), float(input()), float(input()), float(input()), input())
    elif opt == 2:
        print('Introdu: nume si raza')
        Database.update_city_radius(input(), float(input()))
    elif opt == 3:
        print('Introdu: nume')
        Database.delete_city(input())
    elif opt == 4:
        print('\n'.join(str(x) for x in Database.get_cities()))

def main():
    while True:
        try:
            print('Introdu: 1.{}\n2.{}\n3.{}\n4.{}'.
                format('Modifica userii', 'Modifica judetele',
                    'Modifica orasele', 'Iesi din aplicatie'))

            opt = int(input())

            if opt == 4:
                return 0

            if opt == 1:
                modify_users()
            elif opt == 2:
                modify_counties()
            elif opt == 3:
                modify_cities()

        except Exception as e:
            print('Eroare: {}'.format(e))

        print()

if __name__ == '__main__':
    main()
