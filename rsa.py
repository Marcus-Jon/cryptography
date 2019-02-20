# Initialisation.
import base64
p_prime = False
q_prime = False
x = 2
y = 2

# User inputs, which checks if prime.
p = input('Enter a prime number: ')
while p_prime != True and x < p:
    print '\r', p % x, x,
    if p % x != 0 and x == (p - 1):
        p_prime = True
    elif p % x == 0:
        print '\n'
        p = input('Not prime. Enter a prime number: ')
        x = 1
    x = x + 1
print '\n'
q = input('Enter a prime number: ')
while q_prime != True and y < q:
    print '\r', q % y, y,
    if q % y != 0 and y == (q - 1):
        q_prime = True
    elif q % y == 0:
        print '\n'
        q = input('Not prime. Enter a prime number: ')
        y = 1
    y = y + 1
print '\n'
message = raw_input('Enter a message: ')

# Encode message with base64 then convert to ascii numerical values.
message = message.encode('base64')
message = [ord(c) for c in message]

# Message must be less than n for it to work.
# Calculate n using product of the two primes.
n = p * q

T = (p-1)*(q-1)
e = 0
d = 0
for i in range(1, (T-1)):
    if i > 1 and i < (T-1) and (T % i) != 0:
        e = i
    elif e != 0:
        break
print '\n'
print "P= ", p
print "Q= ", q
print "N= ", n
print "T= ", T
print "E= ", e

for i in range(1, (e * T)):
    if (i * e) % T == 1:
        d = i
    elif d != 0:
        break

if d == 0:
    print "no value of d"
    print "cannot encrypt or decrypt data"
else:
    print "D= ", d
    # RSA keys.
    public_key = [e, n]
    private_key = [d, n]
    print public_key
    print private_key
    print '\n'
    # Encrypting the message, then decrypting it.
    ciphertext = [message[c] ** e % n for c in range(0, len(message))]
    print ciphertext
    original_message = []
    for c in range(0, len(ciphertext)):
        original_message.append(ciphertext[c] ** d % n)
        print '\r', original_message[c],
    #original_message = [ciphertext[c] ** d % n for c in range(0, len(ciphertext))]
    print '\n'
    original_message = [chr(c) for c in original_message]
    original_message = ''.join(map(str, original_message))
    original_message = original_message.decode('base64')
    print original_message
