from itertools import permutations

def permutation():
	a = list(set(permutations(['0','1','2','3','4','5','6','7','8'])))
	b = a.sort()
	c = [''.join(i) for i in a]
	for i in c:
		print i

if __name__ == "__main__":
	permutation()
	
