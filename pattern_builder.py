"""This is the Pattern builder"""
import animals


class TierFactory:
    @staticmethod
    def create_tier(art, name, weight):
        if art == "Lion":
            return animals.Lion(name, weight)
        elif art == "Elephant":
            return animals.Elephant(name, weight)
        else:
            print(f"We dont have this animal: {art}, in the database")
            return None
