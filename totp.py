###############################################################################
''' HOTP
works by adding a counter to a secret key. These are then passed through
a hash function. Once used the counter is incremented to produce a new
pass code.'''

import os
import base64
import hashlib

key = os.urandom(16)
counter = 0
h = hashlib.sha256()
x = True

while x:
    request = raw_input()
    if request == 'hotp':
        otp = key + str(counter)
        h.update(otp)
        hotp = (h.digest()).encode('base64')
        hotp = hotp[:8]
    counter += 1
    os.system('cls')
    print hotp
