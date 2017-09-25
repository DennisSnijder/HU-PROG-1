from LockerAssignment.repository import locker_repository
from LockerAssignment.controller import controller_interface


class unlockController(controller_interface.controllerInterface):
    locker_repository: locker_repository

    def __init__(self, repository: locker_repository.LockerRepository):
        self.locker_repository = repository

    def handle_request(self):
        locker_number = input('Enter your locker number: ')
        locker = self.locker_repository.get_locker_by_number(int(locker_number))

        if locker is None:
            print('This locker does not exists')
            exit(1)

        locker_code = input('Enter your locker code: ')

        if locker[1] == int(locker_code):
            print('Your locker is now open!')
