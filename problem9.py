def pythagorean():
	# a+b+c = 1000        ---- (1)
	# a^2 + b^2 = c^2     ---- (2)

	# a = 1000*(500-b) / (1000 - b) ----> After mathematically solving the equation by squaring the eq. 1

	for b in range(1,500):
		if 1000*(500-b) % (1000-b) == 0:
			a = 1000*(500-b) / (1000-b)
			print b, a

	A = a**2
	B = b**2
	C = A+B

	print C

if __name__ == '__main__':
	pythagorean()