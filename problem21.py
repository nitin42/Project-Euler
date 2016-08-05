def divisors(n):
    arr = []
    arr.append(1) # 1 is common divisor
    for i in range(2, n): # For all numbers less than the number n
        if n%i == 0:
            arr.append(i) # Add the divisor
            arr.append(n/i) # Add the remainder
    return set(arr) # Each divisor should be unique

sum_div = [] # Store the sum of the divisors from range upto 10000

for j in range(0,10000):
    sum_div.append(sum(divisors(j)))

total = 0

for k in range(0, 10000):
    a = sum_div[k] # store the sum of divisor of number k
    if a<10000:
        b = sum_div[a] # Store the sum of divisor of the previous sum as the number
        if k == b and a!=b:
            print '%s and %s are amicable' % (a, b)
            total += a

print total
