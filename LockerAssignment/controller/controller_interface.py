from abc import abstractmethod


class controllerInterface:
    @abstractmethod
    def handle_request(self): raise NotImplementedError
