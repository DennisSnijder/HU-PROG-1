from LockerAssignment.repository import locker_repository
from LockerAssignment.controller import unlock_controller, request_controller, cancel_controller, quit_controller


class LockerSystem:
    optionControllers: dict
    locker_repository: locker_repository.LockerRepository

    def __init__(self):
        self.locker_repository = locker_repository.LockerRepository()
        self.optionControllers = {
            1: unlock_controller.unlockController(self.locker_repository),
            2: request_controller.requestController(self.locker_repository),
            3: cancel_controller.cancelController(self.locker_repository),
            0: quit_controller.quitController()
        }

        self.show_menu()

    # Shows the initial menu for the application.
    def show_menu(self):
        print('Welcome, please choose one of the following options')
        print('Option 1. Unlock a locker.')
        print('Option 2. Request a new locker.')
        print('Option 3. Cancel a locker.')
        print('Option 0. Quit the application')

        try:
            selected_option = int(
                input('Please enter the option number.')
            )
        except ValueError:
            return self.handle_invalid_menu_input()

        self.handle_selected_option(selected_option)

    # Handles the users input, calls the right controller for the right option.
    def handle_selected_option(self, selected_option):
        if selected_option in self.optionControllers:
            self.optionControllers[selected_option].handle_request()
        else:
            self.handle_invalid_menu_input()

    # Notifies the user that his input is invalid, recalls the show_menu function.
    def handle_invalid_menu_input(self):
        print('This is not a valid option, please try again.')
        print('=============================================')
        self.show_menu()


LockerSystem()
