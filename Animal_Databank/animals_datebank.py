"""We start with the class Animals"""
from Animal_Databank.Enum_animal_datebank import TierArt as TA


class Animals():
    def __init__(self, name, art, weight, sex):
        self.name = name
        self.art = art
        self.weight = weight
        self.big = None
        self.sex = sex

    def sexuale(self):
        if self.sex == "m":
            self.sex = "male"
        elif self.sex == "f":
            self.sex = "female"

    def info(self):
        print(f"{self.name} is a {self.art} and the weight: {self.weight} kg and {self.big}.{self.name} is {self.sex}")


class Lion(Animals):
    def __init__(self, name, weight, sex=None):
        super().__init__(name, TA.LION.value, weight, sex)

    def sleep(self):
        print(f"{self.name} sleep!")

    def sound(self):
        print("Rawrrrrr")


class Elephant(Animals):
    def __init__(self, name, weight, sex=None):
        super().__init__(name, TA.ELEPHANT.value, weight, sex)

    def sound(self):
        print("töööörööö")

    def sleep(self):
        print(f"{self.name} sleep!")


class Giraffe(Animals):
    def __init__(self, name, weight, sex=None):
        super().__init__(name, TA.GIRAFFE.value, weight, sex)

    def sound(self):
        print("   ")

    def sleep(self):
        print(f"{self.name} sleep!")
