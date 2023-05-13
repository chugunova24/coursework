from random import random


class HashTable:
    def __init__(self, arr=None):
        self.keys = []
        self.hashes = []
        if arr is not None:
            self.appendArray(arr)

    def appendKey(self, item, length=None):
        if length is None:
            length = len(self.keys)

        self.checkKeyExists(item)
        temp = hash(tuple(item)) % length
        # if type(item) == list or type(item) == str:
        #     temp = hash(tuple(item)) % length
        # else:
        #     temp = hash(item) % (length + 1)

        if self.checkCollisions(temp):
            temp = self.simpleRehash(item, length)

        self.hashes.append(temp)
        self.keys.append(item)

    def printHashes(self):
        # for i in range(len(self.keys)):
        #     print(self.hashes[i], self.keys[i])
        # print()
        return [self.hashes, self.keys]

    def appendArray(self, arr):
        for item in arr:
            self.appendKey(item, len(arr))

    def simpleRehash(self, key, length):
        i = 1
        while True:
            temp = hash(tuple(key)) % length + i
            if not self.checkCollisions(temp):
                return temp
            i = i + 1

    def checkCollisions(self, hashValue):
        return hashValue in self.hashes

    def checkKeyExists(self, key):
        if key in self.keys:
            raise Exception("Key '{}' already exists".format(key))
