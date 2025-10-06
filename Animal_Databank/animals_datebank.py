"""We start with the class Animals"""
from Animal_Databank.Enum_animal_datebank import TierArt as TA
class Animals():
    def __init__(self, name, art, weight):
        self.name = name
        self.art = art
        self.weight = weight
        self.big = None

    def info(self):
        print(f"{self.name} is a {self.art} and the weight: {self.weight} kg and {self.big}.")


class Lion(Animals):
    def __init__(self, name, weight):
        super().__init__(name, TierArt.LION, weight)

    def sleep(self):
        print(f"{self.name} sleep!")

    def sound(self):
        print("Rawrrrrr")


class Elephant(Animals):
    def __init__(self, name, weight):
        super().__init__(name, "Elephant", weight)

    def sound(self):
        print("töööörööö")

    def sleep(self):
        print(f"{self.name} sleep!")


