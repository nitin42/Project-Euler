# Function for creating a very long decimal fraction which is irrational
# Generate positive integers randomly and append them into a list followed by a '0.'
# Find the positonal value for postions 1, 10, 100, 1000, 10000, 100000, 10000000
# Multiply the results of these positional arguments

# Note - The upper bound I defined for the solution is (1000000*10)

from random import randint

def champernowne_constant():
    l = [0.] # Initial decimal value
    for i in range(1, 10000000):
        l.append(randint(1, 1000000))

    # fraction = ''.join(l) # Our decimal fraction 
    d_one = l[1]
    d_ten = l[10]
    d_hundred = l[100]
    d_one_k = l[1000]
    d_ten_k = l[10000]
    d_one_l = l[100000]
    d_ten_l = l[1000000]

    result = d_one * d_ten * d_hundred * d_one_k * d_ten_k * d_one_l * d_ten_l

    print result

    '''
    >>> champernowne_constant()
    28091920344905555503616130094521501445600
    '''

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
