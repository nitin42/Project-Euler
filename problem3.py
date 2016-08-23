from math import sqrt

def max_prime(n):
    if n<0:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False

    return True

def check():

    '''
    >>> check()
    6857
    '''

    i = 1 # Initially
    number = 600851475143
    l = []

    # After this n must be odd.
    while i*i<=number:
        i += 2
        if number%i == 0:
            if max_prime(i):
                l.append(i)

    print max(l)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
