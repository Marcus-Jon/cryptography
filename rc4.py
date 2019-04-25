# ARC4
import os
class ARC4():
    limit = 256 # maximum keylength
    def key_scheduling(self, key):
        self.key = key
        # list used to store all permutations known as the state
        self.State = range(self.limit)
        j = 0
        # first step is to map each byte to itself in the list
        # the key is then mixed into the state
        # the values of State[i] and State[j] are swapped
        # if the key bits run out then wrap around
        for i in range(self.limit):
            j = (j + self.State[i] + ord(self.key[i % len(self.key)])) % self.limit
            self.State[i], self.State[j] = self.State[j], self.State[i]
        self.pseudo_random_generation_algorithm()

    def pseudo_random_generation_algorithm(self):
        self.keystream = []
        i = 0
        j = 0
        # this is used to produce a pseudo random byte based on the state
        # these bytes are used to form the keystream
        # the keystream is then used to XOR with the plaintext or ciphertext
        for i in range(self.limit):
            i = (i + 1) % self.limit
            j = (j + self.State[i]) % self.limit
            self.State[i], self.State[j] = self.State[j], self.State[i]
            self.keystream.append(self.State[(self.State[i] + self.State[j]) % self.limit])
        self.output = "".join(map(chr, self.keystream))

    def encryption(self, key, plaintext):
        self.key_scheduling(key)
        ciphertext = ''.join([chr(ord(x) ^ ord(y)) for (x, y) in zip(self.output, plaintext)])
        return ciphertext
    def decryption(self, key, ciphertext):
        plaintext = self.encryption(key, ciphertext)
        return plaintext

if __name__ == "__main__":
    alg = ARC4()
    test = (os.urandom(16)).encode('base64')
    test_data = {test : 'plaintext'}
    for (key, plaintext) in test_data.iteritems():
        print ""
        print 'Encrypting ' + plaintext + ' with key ' + key
        ciphertext = alg.encryption(key, plaintext)
        print 'ciphertext ' + ciphertext
        print 'decrypting ' + ciphertext + ' with ' + key
        print 'original message is ' + alg.decryption(key, ciphertext)
