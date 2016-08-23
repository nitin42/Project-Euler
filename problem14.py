# Thankx to Charles Leifer

def rule(num):
    if num%2 == 0:
        return num/2
    else:
        return 3*num + 1


def cal():
    '''
    >>> cal()
    837799
    '''
    dic = {1:1}
    n = 0
    m = 0
    for i in range(1, 1000000, 2):
        res = i
        max_terms = 0
        while res!=1:
            if dic.has_key(res):
                max_terms += dic[res] # Add only one term
                break
            else:
                max_terms += 1
                res = rule(res) # Calculate the total terms

        dic[i] = max_terms

        if max_terms>m: # Number of terms
            n = i
            m = max_terms

    print n


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
