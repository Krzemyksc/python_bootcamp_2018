class Dog:

    def __init__(self):
        self.energy = 10

    def get_energy(self):
        return self.energy

    def bark(self):
        self.energy -= 1

    def sleep(self):
        self.energy += 2

def test_dog():
    dog = Dog()

    assert dog.get_energy() == 10
    dog.bark()
    dog.bark()
    assert dog.get_energy() == 8
    dog.sleep()
    assert dog.get_energy() == 10