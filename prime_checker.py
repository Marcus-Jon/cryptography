# prime checker
# import in other programs to make use of this function
# place in same directory as the file calling it
def prime_check():

    x = 2
    is_prime = False

    prime = input('Enter a prime number: ')
    while is_prime != True and x < prime:
        print '\r', prime % x, x,
        if prime % x != 0 and x == (prime - 1):
            is_prime = True
        elif prime % x == 0:
            print '\n'
            prime = input('Not Prime. Enter a prime number: ')
            x = 1
        x += 1
    print '\n', 'Prime found'
    print '\n'
    return prime
