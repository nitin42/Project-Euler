def gen_prime(n):
	l = []
	for num in range(2, n+1):
		if num>1:
			for i in range(2, num):
				if num%i == 0 and not is_pandigital(num): 
					break
			else:
				l.append(num)
	print l

def is_pandigital(n):
	a = str(n)
	l = len(a) # Length of the input
	if l>=10: # Only 9 pandigital go through
		return False
	for i in range(1, 10):
		if str(i) not in a: # Check if all the numbers from 1-10 are present in our input
			return False
	return True # The number is pandigital

if __name__ == '__main__':
	gen_prime(120)