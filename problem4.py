def palindrome(n):
	return str(n)[::] == str(n)[::-1]

m = 0
while x>=100:
	while y>=100:
		mul = x*y
		if palindrome(mul) and mul>m:
			m = mul # Maximum product
		y -= 11 # Largest 3 digit number multiple of 11
		x -= 1

print m