def LCM(a,b):
    hcf=float('-inf')
    for i in range(1,a+1):
        if a%i==0:
            hcf=i
    lcm=(a*b)//hcf
    return lcm
print(LCM(10,20))
def LCM(a,b):
    hcf=float('-inf')
    for i in range(1,a+1):
        if a%i==0:
            hcf=i
    return (a*b)//hcf
print(LCM(10,20))