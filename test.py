import unittest
from animals import Animals, Lion, Elephant
from pattern_builder import TierFactory


class MyTestCase(unittest.TestCase):
    def test_animals(self):
        animal = Animals("Simba", "Lion", 190)
        animal.info()
        self.assertEqual(animal.name, "Simba")
        self.assertEqual(animal.art, "Lion")
        self.assertEqual(animal.weight, 190)

    def test_lion(self):
        lion = Lion("Frank", 150)
        lion.info()
        lion.sound()
        lion.sleep()
        self.assertEqual(lion.name, "Frank")
        self.assertEqual(lion.art, "Lion")
        self.assertEqual(lion.weight, 150)

    def test_elefant(self):
        elephant = Elephant("Dumbo", 450)
        elephant.info()
        elephant.sound()
        elephant.sleep()
        self.assertEqual(elephant.name, "Dumbo")
        self.assertEqual(elephant.art, "Elephant")
        self.assertEqual(elephant.weight, 450)

    def test_tierfactory(self):
        tier = TierFactory.create_tier("Elephant", "Hans", 1000)
        tier.info()
        tier.sound()
        tier.sleep()
        self.assertEqual(tier.name, "Hans")
        self.assertEqual(tier.art, "Elephant")
        self.assertEqual(tier.weight, 1000)
    def test_tierfactory2(self):
        tier = TierFactory.create_tier("Pinguin", "Hans", 1000)



if __name__ == '__main__':
    unittest.main()
