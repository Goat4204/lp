p = 3
q = 11

n = p * q
phi = (p - 1) * (q - 1)

e = 7
d = 1

while (d * e) % phi != 1:
    d += 1

message = 5

cipher = (message ** e) % n
plain = (cipher ** d) % n

print("Value of p =", p)
print("Value of q =", q)
print("Value of n =", n)
print("Value of phi =", phi)

print("Public Key (e, n) =", e, n)
print("Private Key (d, n) =", d, n)

print("Original Message =", message)
print("Encrypted Message =", cipher)
print("Decrypted Message =", plain)