def reciprocate_cycle():
    '''
    >>> reciprocate_cycle()
    999
    '''
    mx = 0 # For storing the maximum number of the remainders
    for i in range(7, 1000):
        count = 0 # Initially there is no remainder so count is zero
        value = 10 % i # Store the remainder in value variable
        n = 1000 # For tracking the longest value of d under 1000
        z = 0
        while(value != 1 and z >= 0):
            value = value * 10
            value = value % 10
            count += 1
            z -= 1 
        if (count>mx and z>1):
            mx = count
            mx2 = i

    print  i
 

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
