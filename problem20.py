def factorial_sum(num):

    '''
    >>> factorial_sum(4)
    6
    '''

    fact = 1
    #l = []
    # check if the number is negative, positive or zero
    if num < 0:
        return num
    else:
        for i in range(1,num + 1):
            fact = fact*i

    a = (list(str(fact)))
    
    b = map(int, a)

    c = sum(b)

    print c


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
