import Keyring

if __name__ == '__main__':
    keyring = Keyring.Keyring()
    bobsKeyring = [{"Bob": (67,29)},
{"Jane": (53,10)}, {"Janice": (68,39)}]

    keyring.addKeyValuePair({"Bob": (67,29)})
    keyring.addKeyValuePair({"Alice": (53,10)})
    keyring.deleteKeyPairByName("Bob")
    keyring.deleteKeyPairByKey((53,10))
    keyring.importKeyRingFromTrusted(keyring.keys[0], bobsKeyring)
    entropy = input("Please select the encryption strength in bits\n")
'''
    boolPrime = False
    while not boolPrime:
        p = random.getrandbits(int(entropy)//2)
        tempPrime = isPrime(p)
        if tempPrime:
            q = random.getrandbits(int(entropy)//2)
            boolPrime = isPrime(q)

    (publicKey,privateKey) = generateKeys(p,q)
   rint("Success! Public Key: {0}, modulo: {1}; Private Key: {2}, modulo: {3}".format(publicKey[0],publicKey[1],privateKey[0],privateKey[1]))
    cipher = encrypt(publicKey, "This is a secret Message")
    print("This is a secret Message. Cipher is; ", cipher)
    plaintext = decrypt(privateKey, cipher)
    print("Decoded: {0}".format(plaintext))
   # print(crack(cipher, "This"))'''




