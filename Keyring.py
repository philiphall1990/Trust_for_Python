from RSAAlgorithm import autoGen as genKeyPair

class Keyring:
    def __init__(self):
        self.name = "Me"
        self.publicKey, self.privateKey = genKeyPair(10)#10 bits of entropy is ridiculously weak: for testing purposes only.
        self.keys = [{self.name : self.publicKey}]

    def addKeyValuePair(self, keyValuePair):
        self.keys.append(keyValuePair)

    def deleteKeyPairByKey(self, publicKey):
        self.keys = [x for x in self.keys if list(x.values())[0] != publicKey]

    def deleteKeyPairByName(self, name):
        self.keys = [x for x in self.keys if list(x.keys())[0] != name]

    def importKeyRingFromTrusted(self, trustedKey, keyRing):
        tempList = [x for x in self.keys if x == trustedKey]
        if len(tempList)>0:
            keyRing = [x for x in keyRing if x not in self.keys]
            self.keys.append(keyRing)



