from math import *

# Calculates the divisors of a number
def divisors(n):
	l = sqrt(n)
	div = []
	for i in range(1, l):
		if n % i == 0:
			div.append(i)
			if i != n/i:  # Add the remaining distinct factors into the list
				div.append(n/i)
	return div


# Check whether the number is triangle number or not
def isTriangleNumber(n):
    a = int(sqrt(2*n)) # Check for the nth digit triangle number

    return 0.5*a*(a+1) == n # If n is the ath triangular number, then n = a*(a+1)/2

def last_term(n):
	if isTriangleNumber(n):
		return int(sqrt(n))
	else:
		None


first_num = 2**4 * 3**4 * 5**4 * 7 * 11

while not isTriangleNumber(first_num):
	first_num += 1 # Calculate another triangle number greater than first_num having more than 5 divisors

last = last_term(first_num)


def final():
	while divisors(first_num) <= 500: # Check for triangle numbers greater than 500 
		# add the next term to first_num to get the next triangle number
		check += (seriesLastTerm + 1)
		seriesLastTerm += 1
	print first_num

	'''
	>>>final()
	62378865
	
	'''

if __name__ == '__main__':
	import doctest
	doctest.testmod()
	
