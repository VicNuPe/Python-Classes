from abc import ABC
from interfaces import IFly, IThunder


class Being(ABC):
    pass


class SuperHero(Being):
    pass

class GodHero(SuperHero):
    pass

class HumanHero(SuperHero):
    pass


class Batman(HumanHero, IFly):
    def fly(self):
        print("I am flying with my bat wings")

    def land(self):
        print("I am landing with my bat wings")

class Thor(GodHero, IThunder, IFly):
    def fly(self):
        print("I fly with my hammer!")
    def land(self):
        print("I land with my mighty hammer.")
    def thunder(self):
        pass