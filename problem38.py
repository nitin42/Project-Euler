def is_pandigital(n):
	l = len(n) # Length of the input
	if l>=10: # Only 9 pandigital go through
		return False
	for i in range(1, 10):
		if str(i) not in n: # Check if all the numbers from 1-10 are present in our input
			return False
	return True # The number is pandigital

def pan_mul():
	m = []
	# Just a normal heat-n-trial by multiplying the numbers with 1 and 2
	for i in range(9487, 9213, -1): # Move backwards till 9213
		res = str(i*1) + str(i*2)
		if is_pandigital(res):
			m.append(res)		
	print max(m) # Print the maximum or largest pandigital number from the list 	


if __name__ == '__main__':
	pan_mul()

