from abc import ABC, abstractmethod


class StreamConnection(ABC):
    @abstractmethod
    def connect():
        pass

    @abstractmethod
    def receiveMessages():
        pass
