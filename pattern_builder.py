from Animal_Databank.Enum_animal_datebank import TierArt as TA
from Animal_Databank.animals_datebank import  Lion, Elephant
"""This is the Pattern builder"""
# Mit dem builder können wir schrittweise neue verschiede Typen erstellen

"""We have a animal_builder"""
#Hier erstellen wir neue Tiere die in den Zoo kommen.
class TierFactory:
    @staticmethod
    def create_tier(art, name, weight):
        if art == TA.LION.value:
            return Lion(name, weight)
        elif art == "Elephant":
            return Elephant(name, weight)
        else:
            print(f"We dont have this animal: {art}, in the database")
            return None

# Hier werden die Gehge für die Tiere erstellt
class Vivarium_builder:
    def create_vivarium(self ,art,in_or_out):
        pass

