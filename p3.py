# The prime factors of 13195 are 5, 7, 13 and 29. 
# What is the largest prime factor of the number 600851475143?

import math
target_number = 600851475143

def is_prime(x):
	for i in range(2,int(math.sqrt(x))):
		if(x % i == 0):
			return False
	return True

upper_limit = int(math.sqrt(target_number))
for i in range(2,upper_limit):
	if ((target_number % i == 0) and (is_prime(i))):
		largest_prime = i
print largest_prime
