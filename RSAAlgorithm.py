import random
import decimal as d
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def egcd(a, b):
    x = 0
    y = 1
    _x = 1
    _y = 0
    oa = a
    ob = b

    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, _x) = ((_x - (q * x)), x)
        (y, _y) = ((_y - (q * y)), y)
    if _x < 0:
        _x += ob
    if _y < 0:
        _y += oa
    return a, _x, _y


def multInverse(a, m):
    (x, y, _) = egcd(a, m)
    if x != 1:
        raise ArithmeticError()
    return y


def isPrime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    n = 3
    sqr = (int(x ** 0.5 + 1))
    while n < sqr:
        if (divmod(x, n)[1] == 0):
            return False
        n += 1
    return True


def generateKeys(p, q):
    if p == q:
        print(p, q, "Equal")
        return "Not prime"
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randint(1, phi)
        g = gcd(e, phi)

    d = multInverse(e, phi)
    return ((e, n), (d, n))


def encrypt(kp, plaintext):
    key, n = kp
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher


def decrypt(kp, ciphertext):
    key, n = kp
    plaintext = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plaintext)


def autoGen(entropy):
    boolPrime = False
    while not boolPrime:
        p = random.getrandbits(int(entropy) // 2)
        tempPrime = isPrime(p)
        if tempPrime:
            q = random.getrandbits(int(entropy) // 2)
            boolPrime = isPrime(q)
    return generateKeys(p, q)
