###########################################################################

import random

mode = raw_input('mode: ')
message = raw_input('message: ')
message_len = range(len(message))

if mode == 'encrypt':
    print 'message first then key'
    key = ''.join(chr(65 + random.randint(0, 25)) for x in message_len)
    ciphertext = key + "\n"+''.join(chr((ord(message[x])+ord(key[x]))%26 + 65) for x in message_len)
elif mode == 'decrypt':
    key = raw_input('Key: ')
    ciphertext = ''.join(chr((ord(key[x])-ord(message[x]))%26 + 65) for x in message_len)
print ciphertext
