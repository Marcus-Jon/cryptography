import os
import base64
import hashlib

message = 'test'

key = os.urandom(16)
key = ''.join(format(ord(x)) for x in key)
print key

inner_pad = ''.join(chr(ord(k) ^ 0x5C) for k in key)
print inner_pad

outer_pad = ''.join(chr(ord(k) ^ 0x36) for k in key)
print outer_pad

h = hashlib.sha256()
h.update(inner_pad + message)
first_pass = (h.digest()).encode('base64')
print first_pass
g = hashlib.sha256()
g.update(outer_pad + first_pass)
second_pass = (g.digest()).encode('base64')
print second_pass
