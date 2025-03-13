p, q = 5, 7
e = 23
n = p*q
d = [i for i in range(100)]

for i in d:
    if (i*e) % ((p-1)*(q-1)) == 1 and i != e:
        print(i)