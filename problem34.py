def fact(n):
    "Return n!."
    if n < 2:
        return 1
    else:
        result = 1
        for i in xrange (2, n + 1):
            result = result * i
        return result

def curious_number():
    '''
    >>> curious_number()
    40730
    '''

    #s = 0
    r = 0
    '''
    upper bound is on 9!*7 = 2540160 which is a seven digit number

    '''
    for i in range(10, 2540161):
        n = i
        s = 0
        while(n>0):
            d = n%10
            n /= 10
            s += fact(d)

        if (s == i):
            r += i

    print r

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
