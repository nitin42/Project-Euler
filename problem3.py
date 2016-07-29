from math import sqrt

def max_prime(n):
	if n<0:
		return False
	for i in range(2, sqrt(n)+1):
		if n%i == 0:
			return False

	return True

i = 1 # Initially
number = 600851475143

# After this n must be odd.
while i*i<=number:
	i += 2
	if number%i == 0:
		if max_prime(i)
			print i


if __name__ == '__main__':
	prime(int(raw_input()))