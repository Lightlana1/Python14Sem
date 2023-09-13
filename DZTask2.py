# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

import unittest

class Fish:
    def __init__(self, name: str, color: str, size: float, max_depth: float):
        self.name = name
        self.color = color
        self.size = size
        self.max_depth = max_depth

    def show_max_depth(self):
        print(self.max_depth)


class Cat:
    def __init__(self, name: str, color: str, size: float, hairy: bool):
        self.name = name
        self.color = color
        self.size = size
        self.hairy = hairy

    def show_hairy(self):
        print(self.hairy)


class Bird:
    def __init__(self, name: str, color: str, size: float, habitat: str):
        self.name = name
        self.color = color
        self.size = size
        self.habitat = habitat

    def show_habitat(self):
        print(self.habitat)

    def get_habitat(self):
        return self.habitat

class TestSample(unittest.TestCase):
    def setUp(self) -> None:
        self.bird = Bird('Chik', 'white', 14,'forest')

    def test_get_habitat(self):
        self.assertEqual(self.bird.get_habitat(), "forest")



if __name__ == '__main__':
    unittest.main(verbosity=2)