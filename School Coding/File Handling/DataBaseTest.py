import tkinter as tk
import math

fPath = "School Coding\\File Handling\\DataFiles\\data.txt"

with open(fPath, "w") as file:
    file.write("YAY")


#gui
root = tk.Tk()
sWidth = root.winfo_screenwidth()
sHeight = root.winfo_screenheight()


root.title("Test Window")
root.geometry(f'{str(math.trunc(sWidth/2))}x{str(math.trunc(sHeight/2))}')


message = tk.Label(root, text="Hello, World!")
message.pack()


root.mainloop()