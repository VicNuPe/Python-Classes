from app_data import AppData
from abstract_demo import Dog, Cat, Fish, LandBird, FlyBird
from heroes import HumanHero, Batman, GodHero, Thor


print(AppData.APP_VERSION)

dog = Dog("Alfie")
cat = Cat("Bianca")
dog1 = Dog("Fido")
fish = Fish("Viros")

brian = LandBird("Brian")
fly_bird = FlyBird("Sky")

print(f"dog {dog.describe()}")
print(f"cat {cat.describe()}")
print(f"bird {brian.describe()}")
print(f"fish {fish.describe()}")
print(f"Brian Jumps {brian.jump()}")
print(f"Sky Jumps {fly_bird.jump()}")
print(f"cat Jumps {cat.jump()}")
print(f"The fish swims {fish.swim()}")

human_hero = HumanHero()
god_hero = GodHero()

batman = Batman()
thor = Thor()

batman.fly()
batman.land()

thor.fly()
thor.thunder()