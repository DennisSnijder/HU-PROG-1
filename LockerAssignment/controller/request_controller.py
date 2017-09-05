from LockerAssignment.repository import locker_repository
from LockerAssignment.controller import controller_interface


class requestController(controller_interface.controllerInterface):
    locker_repository: locker_repository

    def __init__(self, repository: locker_repository.LockerRepository):
        self.locker_repository = repository

    def handle_request(self):
        print('oh shit, lemme request some shit')
