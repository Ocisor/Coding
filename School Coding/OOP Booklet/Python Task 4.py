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
    pass

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