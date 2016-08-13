def series():
	d = 1000
	n = 10
	ser = sum([pow(i, i) for i in range(1, d+1)])
	print "Sum of series: %d" % ser
	last_ten = ser%10**10
	print "Last ten digits: %d" % last_ten

if __name__ == '__main__':
	series()