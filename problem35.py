# Function for taking prime numbers under one million.
# Check whether the number is prime or not.
# Check whether the reverse of the number is prime or not
# Count the total number of prime numbers at the final

def prime(n):
	# l = []
	# count = 0
	for num in range(2, n+1):
		if num>1:
			for i in range(2, num):
				if num%i == 0:
					break
			else:
				return True

def gen_prime(n):
	l = []
	l2 = []
	count = 0
	for num in range(2, n+1):
		if num>1:
			for i in range(2, num):
				if num%i == 0:
					break
			else:
				l.append(num)

	l3 = map(str, l)				

	for i in l3:
		l2.append(i[::-1])

	l4 = map(int, l2)

	for j in l4:
		if prime(j):
			count += 1
	print count


if __name__ == '__main__':
	gen_prime(1000000)
	
