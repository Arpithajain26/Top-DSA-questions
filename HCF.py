def HCF_func(a,b):
    HCF=float('-inf')
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            HCF=i
    return HCF
print(HCF_func(10,20))
