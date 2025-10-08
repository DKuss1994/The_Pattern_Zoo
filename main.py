from Animal_Databank.animals_datebank import Lion
from pattern_builder import TierFactory
from Animal_Databank.Enum_animal_datebank import TierArt as TA

lion_1 = TierFactory.create_tier(TA.LION.value,"David",1000,"m")
lion_1.sexuale()
lion_1.info()
