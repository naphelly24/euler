# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91*99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import re
def is_palindromic(x):
	x_str = str(x)
	length = len(x_str)
	if length == 5:
	    reg = re.compile(r'(\d)(\d)\d\2\1')
	elif length == 6:
	    reg = re.compile(r'(\d)(\d)(\d)\3\2\1')
	else:
		return False
	match = reg.search(x_str)
	if match is not None:
	    return True
	else:
		return False

max = 0
for i in range (100,999):
	for j in range (100,999):
		if is_palindromic(i*j):
			if i*j > max:
				max = i*j

print max


# 1. is_palindromic function is a bit stupid. We can reverse a string and compre it with the original one to see whether it is palindromic. 
# 2. the palindrmic number must be divisible by 11. So loop with i 100-999 and j 100-999 is clumsy. We just need to loop numbers divisible by 11.
