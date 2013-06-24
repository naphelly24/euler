dimension = 20
a = [1]*(dimension+1) 
for i in range(dimension):
    for j in range(1,dimension+1):
        a[j] = a[j]+a[j-1]
        print a
print a[dimension]
