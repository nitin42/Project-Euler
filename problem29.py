''' 
1. Get the value of a and b from the equation.
2. Get the value of a**b until the maximum b.
3. Store the result in the set and it should be sorted accordingly.
4. Print the result.
'''

def distinct_power():
    l = []
    count = 0
    #a = set()
    for a in range(2, 101):
        for b in range(2, 101):
            l.append(a**b)
    l.sort()

    for i in set(l):
        count += 1

    print count

    '''
    >>> distinct_power()
    9183
    '''

if __name__ == '__main__':
    import doctest
    doctest.testmod()
