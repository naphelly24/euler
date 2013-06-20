# What is the 10 001st prime number?
import math
fp = open("test.txt", 'w')
primes = [2,3]
def is_prime(x):
	for i in range(2,int(math.sqrt(x))+1):
		if(x % i == 0):
			return False
	return True
while len(primes) != 10001:
    start = primes[len(primes)-1] + 2
    while not is_prime(start):
        start += 2
    primes.append(start)
for item in primes:
    fp.write("%d " % item)
print primes.pop()


