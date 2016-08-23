def palindrome(n):
    return str(n)[::] == str(n)[::-1]

def cal_pal():
    '''
    >>> cal_pal()
    2332
    '''
    m = 0
    for i in range(1, 101):
        for j in range(1, 101):
            mul = i*j
            if palindrome(mul) and mul>m:
                m = mul
            j -= 11
            i -= 1
    print m

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
