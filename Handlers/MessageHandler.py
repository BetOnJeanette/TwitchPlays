from abc import ABC, abstractmethod


class MessageHandler(ABC):
    @abstractmethod
    def handleMessage(msg):
        pass
