def pathPrep(path):
    if path[:2] == "C:":
        path = path[2:]
        print(path)

#C:\Users\Jake\Desktop\Projects\Computing Projects\Python\School\Personal Coding\Websites\TestPHP\process_form.php

fPath = str(input())

pathPrep(fPath)