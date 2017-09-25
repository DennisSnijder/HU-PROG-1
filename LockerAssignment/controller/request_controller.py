from LockerAssignment.repository import locker_repository
from LockerAssignment.controller import controller_interface
import sqlite3


class requestController(controller_interface.controllerInterface):
    locker_repository: locker_repository

    def __init__(self, repository: locker_repository.LockerRepository):
        self.locker_repository = repository

    def handle_request(self):
        requested_locker = int(input('Enter a number between 1 and 10: '))

        if requested_locker < 1 or requested_locker > 10:
            print('Invalid locker number')
            return

        pass_code = int(input('Please enter a pass code: '))

        try:
            self.locker_repository.add_locker(requested_locker, pass_code)
        except sqlite3.IntegrityError:
            print('This locker is already in use!')
