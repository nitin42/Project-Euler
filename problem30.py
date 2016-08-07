'''

Breakdown Analysis - The largest 4-digit number of fifth power is 236196. But we need to traverse upto
highest sum of fifth power of digits i.e 295245. For 6-digit number sum of fifth power of their digits
is 354294. So we can find all the narcissistic numbers till 354294.

Note - 1 is ignored as its sum

'''

def narcissistic_number():
	l = []
	final = 0 # Storing the sum of highest power
	for i in range(2, 354295):
		total = 0
		for j in str(i):
			total += int(j)**5

		if total == i: # If the sum is equal to the number
			l.append(i)

	for i in l:
		final += i

	print 'Sum of fifth power is : %d' %(final)

	print 'List of all the numbers: ' 
	print l

if __name__ == '__main__':
	narcissistic_number()
