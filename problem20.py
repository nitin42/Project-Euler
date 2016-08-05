def factorial():
	num = int(input("Enter a number: "))
	factorial = 1

	# check if the number is negative, positive or zero
	if num < 0:
		return num
	else:
		for i in range(1,num + 1):
			factorial = factorial*i
		#print(factorial)

	a = (list(str(factorial)))
   	
   	b = map(int, a)

   	c = sum(b)

   	print c


if __name__ == '__main__':
	factorial()