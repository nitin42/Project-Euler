def power(num):
	a = 2**num
	b = list(str(a))
	res = [int(i) for i in b]
	print sum(res)

power(1000)