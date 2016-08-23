def prime(n):
    '''
    >>> prime(25000)
    7927
    '''

    l = []
    for num in range(2, n+1):
        if num>1:
            for i in range(2, num):
                if num%i == 0:
                    break
            else:
                l.append(num)
    print l[1000]

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
