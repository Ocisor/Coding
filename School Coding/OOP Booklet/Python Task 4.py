import math

def convert(self, string):
    match string:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9
        case _:
            return string

class Shape:
    def __init__(self, x, y=-1, z=-1):
        self.x = convert(x)
        self.y = convert(y)
        self.z = convert(z)
        self.initCircle()
        self.initRectangle()
        self.initTriangle()

    def initCircle(self):
        if self.y == -1:
            self.perimeterValue = 2 * math.pi * self.x
            self.areaValue = math.pi * (self.x ** 2)
    def initRectangle(self):
        if self.y != -1 and self.z == -1:
            self.perimeterValue = (2* self.x) + (2 * self.y)
            self.areaValue = self.x * self.y
    def initTriangle(self):
        if self.y != -1 and self.z != -1:
            self.perimeterValue = self.x + self.y + self.z
            self.areaValue = math.sqrt( (self.perimeterValue/2) * self.perimeterValue/2-self.x * self.perimeterValue/2-self.y * self.perimeterValue/2-self.z)

    def perimeter(self):
        print(f"This has a perimeter of {self.perimeterValue}")
    def area(self):
        print(f"This has a area of {self.areaValue}")


def main():
    #Circles have one value: radius
    circle1 = Shape(2)
    circle2 = Shape("three")

    #Rectangles have two values: width and height
    rectangle1 = Shape(5, 3)
    rectangle2 = Shape("seven", "two")

    #Triangles have three values: the lengths of each side of the triangle
    triangle1 = Shape("four", "six", "nine")
    triangle2 = Shape(3, 6, 5)

    #You can assume that shapes are either given only integer values or only strings
    
    #math.pi returns a value of pi
    #value ** 2 squares a value

    circle1.perimeter()
    circle1.area()

    circle2.perimeter()
    circle2.area()

    rectangle1.perimeter()
    rectangle1.area()

    rectangle2.perimeter()
    rectangle2.area()

    triangle1.perimeter()
    triangle1.area()

    triangle2.perimeter()
    triangle2.area()

    input()

if __name__ == '__main__':
    main()