import MySQLdb

from app.config import DBConfig


class Database:
    db = MySQLdb.connect(host=DBConfig.db_server, port=DBConfig.db_port,
                         user=DBConfig.db_user, passwd=DBConfig.db_password, db=DBConfig.db_name)
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    err = 'err'

    @staticmethod
    def set_session_read_commited():
        Database.cursor.execute('SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;')
        Database.db.commit()

    @staticmethod
    def call_no_throw(method, *args, **kwargs):
        try:
            return method(*args, **kwargs)
        except:
            return Database.err

    @staticmethod
    def insert_county(name: str, lat: float, longi: float, radius: float):
        Database.cursor.callproc('insert_county', (name, lat, longi, radius))
        Database.db.commit()

    @staticmethod
    def select_county(name: str):
        Database.cursor.callproc('select_county', (name, ))
        
        result = Database.cursor.fetchall()
        Database.cursor.nextset()
        return result[0] if result else None

    @staticmethod
    def update_county_radius(name: str, radius: float):
        Database.cursor.callproc('update_county_radius', (name, radius))
        Database.db.commit()

    @staticmethod
    def delete_county(name: str):
        Database.cursor.callproc('delete_county', (name, ))
        Database.db.commit()

    @staticmethod
    def get_counties():
        Database.cursor.callproc('get_counties')
        
        result = Database.cursor.fetchall()
        Database.cursor.nextset()
        return result

    @staticmethod
    def insert_city(name: str, lat: float, longi: float, radius: float, county: str):
        Database.cursor.callproc('insert_city', (name, lat, longi, radius, county))
        Database.db.commit()

    @staticmethod
    def select_city(name: str):
        Database.cursor.callproc('select_city', (name, ))
        
        result = Database.cursor.fetchall()
        Database.cursor.nextset()
        return result[0] if result else None

    @staticmethod
    def update_city_radius(name: str, radius: float):
        Database.cursor.callproc('update_city_radius', (name, radius))
        Database.db.commit()

    @staticmethod
    def delete_city(name: str):
        Database.cursor.callproc('delete_city', (name, ))
        Database.db.commit()

    @staticmethod
    def get_cities():
        Database.cursor.callproc('get_cities')
        
        result = Database.cursor.fetchall()
        Database.cursor.nextset()
        return result

    @staticmethod
    def insert_birth(pin: int, surname: str, name: str, date: MySQLdb.Timestamp, city: str):
        Database.cursor.callproc('insert_birth', (pin, surname, name, date, city))
        Database.db.commit()

    @staticmethod
    def select_birth(pin: str):
        Database.cursor.callproc('select_birth', (pin, ))
        
        result = Database.cursor.fetchall()
        Database.cursor.nextset()
        return result[0] if result else None

    @staticmethod
    def get_births_in_county(county: str):
        Database.cursor.callproc('get_births_in_county', (county,))
        
        result = Database.cursor.fetchall()
        Database.cursor.nextset()
        return result

    @staticmethod
    def get_births_in_city(city: str):
        Database.cursor.callproc('get_births_in_city', (city,))
        
        result = Database.cursor.fetchall()
        Database.cursor.nextset()
        return result

    @staticmethod
    def get_births_between(begin_date: MySQLdb.Timestamp, end_date: MySQLdb.Timestamp):
        Database.cursor.callproc('get_births_between', (begin_date, end_date))
        
        result = Database.cursor.fetchall()
        Database.cursor.nextset()
        return result

    @staticmethod
    def insert_death(person: int, date: MySQLdb.Timestamp, city: str):
        Database.cursor.callproc('insert_death', (person, date, city))
        Database.db.commit()

    @staticmethod
    def select_death(person: str):
        Database.cursor.callproc('select_death', (person, ))
        
        result = Database.cursor.fetchall()
        Database.cursor.nextset()
        return result[0] if result else None

    @staticmethod
    def get_deaths_in_county(county: str):
        Database.cursor.callproc('get_deaths_in_county', (county,))
        
        result = Database.cursor.fetchall()
        Database.cursor.nextset()
        return result

    @staticmethod
    def get_deaths_in_city(city: str):
        Database.cursor.callproc('get_deaths_in_city', (city,))
        
        result = Database.cursor.fetchall()
        Database.cursor.nextset()
        return result

    @staticmethod
    def get_deaths_between(begin_date: MySQLdb.Timestamp, end_date: MySQLdb.Timestamp):
        Database.cursor.callproc('get_deaths_between', (begin_date, end_date))
        
        result = Database.cursor.fetchall()
        Database.cursor.nextset()
        return result
