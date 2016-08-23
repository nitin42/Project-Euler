import fractions

def root_convergents(limit):
    d = fractions.Fraction(1/2) 
    for i in range(limit):
        d = fractions.Fraction(1/(2+d)) # This grows until the iterations end.
        yield 1 + d 

def main():
    '''
    >>> main()
    153
    '''

    print(len([f for f in root_convergents(1000) if len(str(f.numerator))>
                    len(str(f.denominator))]))

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
