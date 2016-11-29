import random
import decimal as d
import math


#def crack(cipher, textFragment):
 #   plaintext = ""
  #  for x in range(3,999999):
   #     (x,y) = (x,3)
    #    plaintext = decrypt((x,y),cipher)
     #   if plaintext.__contains__(textFragment):
      #      return (x,y)

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def egcd(a,b):
    x = 0
    y = 1
    _x = 1
    _y = 0
    oa = a
    ob = b

    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x,_x) = ((_x - (q * x)), x)
        (y, _y) = ((_y - (q * y)), y)
    if _x < 0:
        _x += ob
    if _y < 0:
        _y += oa
    return a, _x, _y



def multInverse(a, m):
    (x,y, _) = egcd(a,m)
    if x != 1:
        raise ArithmeticError()
    return y

def isPrime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    n = 3
    sqr = (int(x**0.5+1))
    while n < sqr:
        if (divmod(x,n)[1] == 0):
            return False
        n += 1
    return True

def generateKeys(p,q):
    if p == q:
        print(p,q, "Equal")
        return "Not prime"
    n = p*q
    phi = (p-1) * (q-1)
    e = random.randint(1,phi)
    g = gcd(e,phi)
    while g != 1:
        e = random.randint(1,phi)
        g = gcd(e,phi)

    d = multInverse(e, phi)
    return ((e,n), (d,n))

def encrypt(kp, plaintext):
    key, n = kp
    cipher = [pow(ord(char),key,n) for char in plaintext]
    return cipher

def decrypt(kp, ciphertext):
    key, n = kp
    plaintext = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plaintext)

if __name__ == '__main__':
    entropy = input("Please select the encryption strength in bits\n")

    boolPrime = False
    while not boolPrime:
        p = random.getrandbits(int(entropy)//2)
        tempPrime = isPrime(p)
        if tempPrime:
            q = random.getrandbits(int(entropy)//2)
            boolPrime = isPrime(q)

    (publicKey,privateKey) = generateKeys(p,q)
    print("Success! Public Key: {0}, modulo: {1}; Private Key: {2}, modulo: {3}".format(publicKey[0],publicKey[1],privateKey[0],privateKey[1]))
    cipher = encrypt(publicKey, "This is a secret Message")
    print("This is a secret Message. Cipher is; ", cipher)
    plaintext = decrypt(privateKey, cipher)
    print("Decoded: {0}".format(plaintext))
   # print(crack(cipher, "This"))




