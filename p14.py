def sequence(num):
    chain_num = 1
    while num != 1:
        if(num%2 == 0):
            num /= 2
        else:
            num = num*3 + 1
        chain_num += 1
    return chain_num
max_chain = [0,0]
for i in range(1, 1000000):
    if sequence(i)>max_chain[1]:
        max_chain[0] = i
        max_chain[1] = sequence(i)
print max_chain[0]

