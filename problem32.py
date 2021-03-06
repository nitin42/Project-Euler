# Function for checking whether the number is pandigital or not
# Check whether the product of two numbers is of length 9 units and its sum is pandigital.
# Generate the random pandigital numbers

def is_pandigital(n):
    l = len(n) # Length of the input
    if l>=10: # Only 9 pandigital go through
        return False
    for i in range(1, 10):
        if str(i) not in n: # Check if all the numbers from 1-10 are present in our input
            return False
    return True # The number is pandigital

def product_pand(a, b):
    string = str(a) + str(b) + str(a*b)
    if len(string)!=9:
        return False
    return is_pandigital(string)

def cal():
    '''
    >>> cal()
    [6952, 7852, 5796, 5346, 5346, 4396, 7254, 5796, 7632, 5796, 4396, 7632, 7254, 5346, 5346, 5796, 6952, 7852]
    45228
    '''

    result = []

    for a in range(0, 100000):
        for b in range(0, 100000):
            if len(str(a*b) + str(a) + str(b))>9:
                break
            if product_pand(a, b):
                result.append(a*b)

    print result

    print sum(set(result))

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
