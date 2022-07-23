class Dog:
    species = 'canine'

    def __init__(self, color, name, breed):
        self.color = color
        self.name = name
        self.breed = breed
        self.steps = 0

    def bark(self):
        return f"woof my name is {self.name}"

    def walk(self):
        self.steps += 5000

    def energy(self):
        if self.steps > 10000:
            return "sleepy"
        else:
            return "pumped"

class HighEnergyDog(Dog):
    def __init__(self, color, name):
        super().__init__(color, name)
        self.breed = 'ridgeback'

    def energy(self):
        if self.steps > 10000000:
            return "sleepy"
        else:
            return "pumped"

roofus = HighEnergyDog('brown', 'roofus')

print(roofus.steps)
roofus.walk()
print(roofus.steps)
print(roofus.energy())
roofus.walk()
roofus.walk()
roofus.walk()
roofus.walk()
roofus.walk()
roofus.walk()
print(roofus.steps)
print(roofus.energy())


