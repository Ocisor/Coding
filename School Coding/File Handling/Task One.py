l = ["Josh", "Joe", "John"]
path = "names1.txt"
f = open(path, "w")
for entry in l:
    f.write(entry + "\n")
f.close()
print(0%2)