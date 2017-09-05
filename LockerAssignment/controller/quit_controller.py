from LockerAssignment.controller import controller_interface
import sys


class quitController(controller_interface.controllerInterface):
    def handle_request(self):
        print('Quiting....')
        sys.exit()
