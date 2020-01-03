import MySQLdb
from functools import wraps

from app.config import DBConfig


def use_new_connection(static_func):
    @wraps(static_func)
    def decorated_view(*args, **kwargs):
        db, cursor = Database.new_connection()
        kwargs['db'] = db
        kwargs['cursor'] = cursor

        ret = static_func(*args, **kwargs)
        Database.close_connection(db, cursor)

        return ret
    return decorated_view


class Database:
    err = 'err'

    @staticmethod
    def new_connection():
        db = MySQLdb.connect(host=DBConfig.db_server, port=DBConfig.db_port,
                             user=DBConfig.db_user, passwd=DBConfig.db_password, db=DBConfig.db_name)
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        Database.set_session_read_commited(db, cursor)

        return db, cursor

    @staticmethod
    def close_connection(db, cursor):
        cursor.close()
        db.close()

    @staticmethod
    def set_session_read_commited(db, cursor):
        cursor.execute('SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;')
        db.commit()

    @staticmethod
    def call_no_throw(method, *args, **kwargs):
        try:
            return method(*args, **kwargs)
        except:
            return Database.err

    @staticmethod
    @use_new_connection
    # db and cursor will be injected by use_new_connection, hopefully
    def insert_user(email: str, password, db=None, cursor=None):
        cursor.callproc('insert_user', (email, password))
        db.commit()

    @staticmethod
    @use_new_connection
    def select_user(email: str, db=None, cursor=None):
        cursor.callproc('select_user', (email,))
        result = cursor.fetchall()

        return result[0] if result else None

    @staticmethod
    @use_new_connection
    def delete_user(email: str, db=None, cursor=None):
        cursor.callproc('delete_user', (email,))
        db.commit()

    @staticmethod
    @use_new_connection
    def get_users(db=None, cursor=None):
        cursor.callproc('get_users')
        result = cursor.fetchall()

        return result
