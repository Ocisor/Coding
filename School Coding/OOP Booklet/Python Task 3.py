class Animal:
    def __init__(self):
        self._coldBlooded = None
        self._skinType = None
        self._tail = None
        self._legs = 0
        self._arms = 0
        self._wings = 0

        self._moveType = ""
        self._diet = ""
        self._birth = ""

    def move(self):
        print(self._moveType)
    def eat(self):
        print(self._diet)
    def birth(self):
        print(self._birth)

    def getInfo(self):
        if self._coldBlooded:
            print("This animal is cold blooded.")
        else:
            print("This animal is warm blooded.")
        if self._skinType != None:
            print(f"This animal is covered in {self._skinType}")
        if self._tail:
            print("This animal has a tail.")
        if self._legs > 0:
            print(f"This animal has {self._legs} legs.")
        if self._arms > 0:
            print(f"This animal has {self._arms} arms.")
        if self._wings > 0:
            print(f"This animal has {self._wings} wings.")
        self.move()
        self.eat()
        self.birth()
        self.hibernate()
        print()


class Reptile(Animal):
    def __init__(self):
        super().__init__()
        self._coldBlooded = True
        self._skinType = "Scales"
        self._tail = True
        self._arms = 0
        self._wings = 0

        self._birth = "This animal lays eggs."
    
    def hibernate(self):
        print("This animal hibernates.")

class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self._coldBlooded = False
        self._skinType = "Fur"
        

        self._birth = "This animal gives birth to live young"

    def hibernate(self):
        pass

class Tortoise(Reptile):
    def __init__(self):
        super().__init__()
        self._legs = 4
        
        self._diet = "This animal is a herbivore."
        self._moveType = "This animal walks."

class Turtle(Reptile):
    def __init__(self):
        super().__init__()
        self._legs = 4

        self._diet = "This animal is an omnivore."
        self._moveType = "This animal crawls and swims."

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self._legs = 0

        self._diet = "This animal is a carnivore"
        self._moveType = "This animal slithers."

class Otter(Mammal):
    def __init__(self):
        super().__init__()
        self._legs = 4
        self._tail = True
        self._arms = 0
        self._wings = 0

        self._moveType = "This animal swims and walks."
        self._diet = "This animal is an omnivore."
    
class Gorilla(Mammal):
    def __init__(self):
        super().__init__()
        self._legs = 2
        self._tail = False
        self._arms = 2
        self._wings = 0

        self._moveType = "This animal walks and climbs"
        self._diet = "This animal is a herbivore"

class Bat(Mammal):
    def __init__(self):
        super().__init__()
        self._legs = 2
        self._tail = True
        self._arms = 0
        self._wings = 2

        self._moveType = "This animal flies."
        self._diet = "This animal is an omnivore."
        


def main():
    tortoise = Tortoise()
    turtle = Turtle()
    snake = Snake()
    otter = Otter()
    gorilla = Gorilla()
    bat = Bat()

    tortoise.getInfo()
    turtle.getInfo()
    snake.getInfo()
    otter.getInfo()
    gorilla.getInfo()
    bat.getInfo()
    input()

if __name__ == '__main__':
    main()