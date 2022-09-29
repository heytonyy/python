class Pet:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.energy = 20
    def sleep(self):
        self.energy += 25
    def eat(self):
        self.energy += 5
        self.health += 10
    def play(self):
        self.health += 5

class Cat(Pet):
    def __init__(self, name):
        super().__init__(name)
        self.type = 'Cat'
        self.tricks = 'pounce'
    def sleep(self):
        super().sleep()
        print(f"{self.name} when to sleep")
    def eat(self, food):
        super().eat()
        print(f"{self.name} eats {food}!")
    def play(self):
        super().play()
        print(f"{self.name} just {self.tricks}d!")
    def noise(self):
        print(f"{self.name} says 'Meow'! ")

class Squirrel(Pet):
    def __init__(self, name):
        super().__init__(name)
        self.type = 'Squirrel'
        self.tricks = 'dig'
    def sleep(self):
        super().sleep()
        print(f"{self.name} when to sleep")
    def eat(self, food):
        super().eat()
        print(f"{self.name} eats {food}!")
    def play(self):
        super().play()
        print(f"{self.name} {self.tricks}s up the dirt! Oh no!")
    def noise(self):
        print(f"{self.name} says 'Bark'!")

