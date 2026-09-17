def HCF_func(a,b):
    HCF=float('-inf')
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            HCF=i
    return HCF
print(HCF_func(10,20))
def HCF_num(a,b):
    hcf=float('-inf')
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            hcf=i
    return hcf
print(HCF_num(10,20))
