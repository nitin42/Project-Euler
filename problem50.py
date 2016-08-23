def prime(n):
	l = []
	l2 = []
	for num in range(2, n+1):
		if num>1:
			for i in range(2, num):
				if num%i == 0:
					break
			else:
				l.append(num)
	
	for i in l:
		for j in l[1:]:
			a = i+j
			if is_prime(a):
				l2.append(a) 

	print l2			
	

def is_prime(n):
	if n>1:
		for i in range(2, n):
			if n%i == 0:
				return False
		else:
			return True
	else:
		return False

if __name__ == '__main__':
	prime(1000000)
	
