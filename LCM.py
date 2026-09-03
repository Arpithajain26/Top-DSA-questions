def LCM_func(a,b):
    HCF=0
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            HCF=i
    LCM=(a*b)//HCF
    return LCM
print(LCM_func(10,15))