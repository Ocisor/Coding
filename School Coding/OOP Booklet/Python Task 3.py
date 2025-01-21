class Animal:
    def __init__(self):
        self._coldBlooded = None
        self._skinType = ""
        self._tail = None
        self._legs = None
        self._arms = None
        self._wings = None

        self._moveType = ""
        self._diet = ""
        self._birth = ""



class Reptile(Animal):
    def __init__(self):
        super.__init__()
        self._coldBlooded = True
        self._skinType = "Scales"

        self._birth = "This animal lays eggs."
    

class Mammal(Animal):
    def __init__(self):
        super.__init__()
        self._birth = "This animal gives birth to live young"
        self._skinType = "Fur"

        self._coldBlooded = False

class Tortoise(Reptile):
    def __init(self):
        super.__init__()
        self._tail = True





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