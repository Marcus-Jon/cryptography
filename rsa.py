# Initialisation.
import base64
import prime_checker as PC

def key_generator(p, q):
    # Message must be less than n for it to work.
    # Calculate n using product of the two primes.
    n = p * q
    phi_n = (p-1)*(q-1)
    e = 0
    d = 0

    for i in range(1, (phi_n-1)):
        if i > 1 and i < (phi_n-1) and (phi_n % i) != 0:
            e = i
        elif e != 0:
            break
    for i in range(1, (e * phi_n)):
        if (i * e) % phi_n == 1:
            d = i
        elif d != 0:
            break
    if d == 0:
        print "no value of d"
        print "encryption process cannot take place"
        quit()

    # RSA keys.
    public_key = [e, n]
    private_key = [d, n]
    return public_key, private_key

def encryption(message, e, n):
    # Encrypting the message.
    # Encode message with base64 then convert to ascii numerical values.
    message = message.encode('base64')
    message = [ord(c) for c in message]
    ciphertext = [message[c] ** e % n for c in range(0, len(message))]
    ciphertext = 'l'.join(map(str, ciphertext))
    return ciphertext

def decryption(ciphertext, d, n):
    # Decryption process
    ciphertext = ciphertext.split('l')
    original_message = ciphertext
    for c in range(0, len(ciphertext)):
        print '\r', '[', '='*c, ' '*(len(original_message)-c), ']',
        ciphertext[c] = int(ciphertext[c])
        original_message[c] = (ciphertext[c] ** d % n)

    #original_message = [ciphertext[c] ** d % n for c in range(0, len(ciphertext))]
    original_message = [chr(c) for c in original_message]
    original_message = ''.join(map(str, original_message))
    original_message = original_message.decode('base64')
    return original_message

if __name__ == '__main__':

    p = PC.prime_check()
    q = PC.prime_check()
    message = raw_input('Enter a message: ')
    if message == '':
        print 'empty message. Exiting...'
        quit()
    own_public_key, own_private_key = key_generator(p, q)

    mode = raw_input('Mode: ')
    if mode == 'encrypt':
        ciphertext = encryption(message, own_public_key[0], own_public_key[1])
        print ciphertext
    elif mode == 'decrypt':
        original_message = decryption(message, own_private_key[0], own_private_key[1])
        print '\n'
        print '\n', 'Message: '
        print original_message
