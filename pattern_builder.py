"""This is the Pattern builder"""
import animals


class TierFactory:
    @staticmethod
    def create_tier(art, name, weight):
        if art == "Löwe":
            return animals.Lion(name, weight)
        elif art == "Elephant":
            return animals.Elephant(name, weight)
        else:
            print("We dont have this animal in the database")
