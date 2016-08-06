def reciprocate_cycle():
	mx = 0 # For storing the maximum number of the remainders
	for i in range(7, 1000):
		count = 0 # Initially there is no remainder so count is zero
		value = 10 % i # Store the remainder in value variable
		n = 1000 # For tracking the longest value of d under 1000
		while(value != 1 and z > 0):
			value = value * 10
			value = value % 10
			count += 1
			z -= 1 
		if (count>mx and z>1):
			mx = count
			mx2 = i

	print ("The value of d for which 1/d produces the longest recursive cycle is : %d" % i )


if __name__ == '__main__':
	reciprocate_cycle()