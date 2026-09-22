from abc import ABC, abstractmethod


class IFly(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def land(self):
        pass


class ISwim(ABC):
    @abstractmethod
    def swim(self):
        pass


class IJump(ABC):
    @abstractmethod
    def jump(self):
        pass


class IClimb(ABC):
    @abstractmethod
    def climb(self):
        pass

class IThunder(ABC):
    @abstractmethod
    def thunder(self):
        pass
    def land(self):
        pass