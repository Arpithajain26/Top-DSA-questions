def common_factor(a,b):
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            print(i)
common_factor(10,20)