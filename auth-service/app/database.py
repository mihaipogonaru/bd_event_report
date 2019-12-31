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
    def insert_user(email: str, password):
        Database.cursor.callproc('insert_user', (email, password))
        Database.db.commit()

    @staticmethod
    def select_user(email: str):
        Database.cursor.callproc('select_user', (email,))

        result = Database.cursor.fetchall()
        Database.cursor.nextset()

        return result[0] if result else None

    @staticmethod
    def delete_user(email: str):
        Database.cursor.callproc('delete_user', (email,))
        Database.db.commit()
    
    @staticmethod
    def get_users():
        Database.cursor.callproc('get_users')
        
        result = Database.cursor.fetchall()
        Database.cursor.nextset()
        return result
