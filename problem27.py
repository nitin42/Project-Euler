import math

def is_prime(n):
    if n < 0:
        return False
    for j in range(2, n):
        if n%j == 0:
            return False
    return True

def generate_primes(n):
    return [x for x in range(2, n+1) if is_prime(x)]

def f(a, b, n):
    return (n**2 + (a*n) + b)

def sequence_of_primes(a, b):
    n = 0
    t = True
    while t:
        t = is_prime(f(a, b, n))
        n += 1
    return n-1

def gen_prime():

    '''
    >>> gen_prime()
    71 
    59231
    '''

    p = generate_primes(1000)

    maximum = 0
    for i in p:
        for j in p:
            l = sequence_of_primes(i, j)
            if l > maximum:
                maximum = l
                nums = (i, j)
            l = sequence_of_primes(-i, j)
            if l > maximum:
                maximum = l
                nums = (-i, j)

    print(maximum)
    print(abs(nums[0] * nums[1]))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
