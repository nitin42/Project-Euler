def smallest(n):
	l = []
	if n<0:
		return False
	for i in range(1,21):
		if n%i == 0:
			l.append(i)

min_num = min(l)
