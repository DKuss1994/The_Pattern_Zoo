"""We start with the class Animals"""
class Animals():
    def __init__(self, name , art, weight):
        self.name = name
        self.art = art
        self.weight = weight
    def info(self):
        print(f"{self.name} is a {self.art} and the weight: {self.weight}")
class Lion (Animals):
    def __init__(self, name, weight):
        super().__init__ ( name, "Lion",weight)
        def sleep(self):
            print(f"{self.name}")

