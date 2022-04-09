"""
Written by WENG XINN CHOW on 07.04.2022
Quick RSA Decription for RSA noob CTFlearn
"""

# Given
e = 1
c = 9327565722767258308650643213344542404592011161659991421
n = 245841236512478852752909734912575581815967630033049838269083

# Factorise n to 2 primes,  p and q  (http://factordb.com/)
p = 416064700201658306196320137931
q = 590872612825179551336102196593

# Find Euler's totient
phi = (p-1) * (q-1)

# Find private key, d - inverse of e (mod  n)
# pow function take base e, inverse exp (for inverse) and modulo
d = pow(e, -1, phi)

# Decrypt message - c ** d mod n
m = (c ** d) % n
print(m)






