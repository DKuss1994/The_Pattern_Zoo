import unittest
from animals import Animals


class MyTestCase(unittest.TestCase):
    def test_animals(self):
        animal = Animals("Simba", "Lion", 190)
        animal.info()
        self.assertEqual(animal.name, "Simba")
        self.assertEqual(animal.art, "Lion")
        self.assertEqual(animal.weight, 190)


if __name__ == '__main__':
    unittest.main()
