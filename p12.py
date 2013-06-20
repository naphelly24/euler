import math
def num_of_divisor(num):
    if num == 1:
        return 1
    number = 0;
    upper = math.sqrt(num)
    for i in range(2, int(math.ceil(upper))):
        if num%i==0:
            number += 1
    number *= 2
    number += 2
    if upper == math.ceil(upper):
        number -= 1
    return number

i = 28
j = 8
while num_of_divisor(i)<=500:
    i += j
    j += 1
print i




