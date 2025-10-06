"""This is the Pattern builder"""
# Mit dem builder können wir schrittweise neue verschiede Typen erstellen
import animals_datebank

"""We have a animal_builder"""
#Hier erstellen wir neue Tiere die in den Zoo kommen.
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

# Hier werden die Gehge für die Tiere erstellt
class Vivarium_builder:
    def create_vivarium(self ,art,in_or_out):
        pass

