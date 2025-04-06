p, q = 5, 7 # Two prime numbers
e = 23 # Coprime to (p-1)(q-1)
n = p*q # Product of the two primes
d = [i for i in range(100)] # List of 100 integers

#for i in d:
#    if (i*e) % ((p-1)*(q-1)) == 1 and i != e:
#        print(i)

def encrypt(value, e, n):
    return ((value**e) % n)

def decrypt(value, d, n):
    return ((value**d) % n)

print(encrypt(int(input("To encrypt: ")), e, n))
print(decrypt(int(input("To decrypt: ")), int(input("Decryption Key: ")), n))