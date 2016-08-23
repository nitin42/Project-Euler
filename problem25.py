def fibo(n):
    '''
    >>> fibo(int('1%s'%('0'*999)))
    4782
    '''
    a, b = 1, 0
    count = 0
    while a<n:
        a, b = a+b, a
        count += 1
    return count+1


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)    
