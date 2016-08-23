def divisors(n):
    arr = []
    arr.append(1) # 1 is common divisor
    for i in range(2, n): # For all numbers less than the number n
        if n%i == 0:
            arr.append(i) # Add the divisor
            arr.append(n/i) # Add the remainder
    return set(arr) # Each divisor should be unique

def abundant_sum(n):
    l = []
    for i in range(1, n+1):
        ab_sm = sum(divisors(i))
        if ab_sm>i: # If the sum is greater than the number itself than the number is abundant
            l.append(i) # Store that number
    return l

def cal_abund():
    '''
    >>> cal_abund()
    4179871
    '''
    num = abundant_sum(28124) # Some numbers will be abundant and some will be deficient
    store = set()

    for i in range(len(num)):
        for j in range(i, len(num)): # Because its sum of TWO abundant numbers
            n = num[i] + num[j]
            if n<28124:
                store.add(n) # Store the number that is abundant

    ''' 
    sum of all the positive integers which cannot be written as the sum of two abundant numbers
    '''

    a = sum(set(range(28124)).difference(store))
    print a


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    
