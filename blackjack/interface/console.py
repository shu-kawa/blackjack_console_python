from abc import ABC, abstractmethod

class IOutput(ABC):
    @abstractmethod
    def write(self, message: str):
        pass

class ConsoleOutput(IOutput):
    def write(self, message: str):
        print(message)

class LogOutput(IOutput):
    def __init__(self, logfile: str = "blackjack.log"):
        self.logfile = logfile

    def write(self, message: str):
        with open(self.logfile, "a", encoding="utf-8") as f:
            f.write(message + "\n")