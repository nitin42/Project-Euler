
def bin_base(n):
	l = []
	for i in range(1, n+1):
		j = str(i) 
		a = bin(i) # Store the binary for the number
		b = a[2:]
		if b == b[::-1] and j == j[::-1]: # Store the numbers whose base 10 and base 2 are palindrome
			l.append(i)

	print sum(l) # Print the sum of the numbers

if __name__ == '__main__':
	bin_base(1000000) # One million numbers 