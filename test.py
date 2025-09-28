import unittest
from animals import Animals, Lion


class MyTestCase(unittest.TestCase):
    def test_animals(self):
        animal = Animals("Simba", "Lion", 190)
        animal.info()
        self.assertEqual(animal.name, "Simba")
        self.assertEqual(animal.art, "Lion")
        self.assertEqual(animal.weight, 190)
    def test_lion(self):
        lion = Lion("Frank",  150)
        lion.info()
        lion.sound()
        lion.sleep()
        self.assertEqual(lion.name, "Frank")
        self.assertEqual(lion.art, "Lion")
        self.assertEqual(lion.weight, 150)


if __name__ == '__main__':
    unittest.main()
