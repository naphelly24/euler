for i in range(1000):
    for j in range(i+1, 1000):
        if 1000-i-j<=j:
            break
        else:
            if i*i+j*j==(1000-i-j)*(1000-i-j):
                print i*j*(1000-i-j)
                quit()
