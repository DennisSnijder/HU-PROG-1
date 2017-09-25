import sqlite3


class LockerRepository:

    connection: sqlite3

    def __init__(self):
        self.connection = sqlite3.connect('lockers.db')
        self.create_sql_structure()

    def create_sql_structure(self):
        self.connection.execute(
            'CREATE TABLE IF NOT EXISTS lockers ('
            'locker_number INTEGER PRIMARY KEY,'
            'pin_code string'
            ');'
        )
        self.connection.commit()

    def get_lockers(self) -> list:
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM lockers')
        return cursor.fetchall()

    def add_locker(self, number: int, pin_code: int):
        self.connection.execute('INSERT INTO lockers (locker_number, pin_code) '
                                'VALUES (' + str(number) + ',  ' + str(pin_code) + ')')
        self.connection.commit()

    def get_locker_by_number(self, number: int) -> tuple:
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM lockers WHERE locker_number = ' + str(number))
        return cursor.fetchone()

    def cancel_locker(self, number: int):
        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM lockers WHERE locker_number = ' + str(number))
        cursor.close()
