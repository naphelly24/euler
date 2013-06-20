# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
num = [i for i in xrange(1,21)] 
primes = [2,3,5,7,11,13,17,19]
j = 0
target = 1
def isAll1(num=[]):
    mul = 1
    for i in num:
        mul *= i
    if mul == 1:
        return True
    else:
        return False

while not isAll1(num):
    flag = 0
    for i in range(0,len(num)):
        if not num[i] % primes[j]:
            num[i] = num[i]/primes[j]
            if flag == 0:
                target *= primes[j]
                flag = 1
    if flag == 0: # all numbers in num cannot dividable by primes[j]
        j += 1
    if 1 in num:
        num.remove(1)
print target

