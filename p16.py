# method 1:

#import math
#num = int(math.pow(2,1000))
#target = 0
#while num != 0:
    #target += num%10
    #num = int(num/10)

#method 2:
#print sum(int(digit) for digit in str(2**1000))

#method 3:
#reduce(lambda x, y: x + y, [int(i) for i in str(2 ** 1000)])

#method 4:
print sum(map(int, str(2**1000)))
