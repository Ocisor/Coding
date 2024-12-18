def pathPrep(path):
    if path[:2] == "C:":
        path = path[2:]
        print(path)
    path = path.split(input("What is the delimeter: "))
    print(path)
    path = input("Enter the double slash: ").join(path)
    print(path[2:])

#C:\Users\Jake\Desktop\Projects\Computing Projects\Python\School\Personal Coding\Websites\TestPHP\process_form.php

fPath = str(input())

pathPrep(fPath)