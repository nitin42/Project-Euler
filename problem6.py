def sum_square(n):
    '''
    >>> sum_square(145)
    111015480
    '''

    sum_of_sq = 0
    sq_of_sum = 0
    for i in range(1, n+1):
        sum_of_sq += i*i

    for j in range(1, n+1):
        sq_of_sum += j

    square = sq_of_sum*sq_of_sum

    final = square - sum_of_sq

    print final

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
