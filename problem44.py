# Function for calculating the pentagonal numbers and storing it in a list
# Try heat-n-trial for calculating the sum and difference of pentagonal numbers
# Check for sum and difference whether it is pentagonal or not 
# Calculate the D 

def pentagonal(n):
    '''
    >>> pentagonal(10)
    22 92
    35 70
    70 35
    70 92
    92 22
    92 70
    '''

    l = []  
    for i in range(1, n+1):
        pn = ((3*i*i - i)/2)    
        l.append(pn)

    for i in l:
        for j in l:
            an = i+j
            sn = abs(i-j)
            if an and sn in l:
                print i, j

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
