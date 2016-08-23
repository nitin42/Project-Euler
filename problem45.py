from __future__ import division

def pent_trian_hex(n):
    '''
    >>> pent_trian_hex(500)
    1.0
    210.0
    40755.0
    '''

    p = []
    t = []
    h = []
    n1 = int(n)
    for i in range(1, n1+1):
        pn = (3*i*i - i)/2
        p.append(pn)

    for i in range(1, n1+1):
        tn = (i*i + i)/2
        t.append(tn)

    for i in range(1, n1+1):
        hn = (2*i*i - i)/2
        h.append(hn)

    p1 = map(str, p)
    t1 = map(str, t)
    h1 = map(str, h)

    for i in t1:
        if i in p1 and h1:
            print i

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
