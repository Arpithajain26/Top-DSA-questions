def pattern1(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(j,end=" ")
        print()
    return
# pattern1(5)
def pattern2(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end=" ")
        print()
    return
# pattern2(4)
def pattern3(n):
    for i in range(1,n):
        for j in range(i+1):
            print("*",end=" ")
        print()
# pattern3(4)
def pattern4(n):
    for i in range(n):
        for j in range(2*i+1):
            print("*",end=" ")
        print()
# pattern4(4)

def pattern5(n):
    for i in range(n):
        for j in range(2*i+2):
            print("*",end=" ")
        print()
# pattern5(4)

def pattern6(n):
    for i in range(n):
        for j in range(n,i,-1):
            print("*",end=" ")
        print()
pattern6(4)
def pattern7(n):
    for i in range(n,-1,-1):
        for j in range(2*i-1):
            print("*",end=" ")
        print()
    return
pattern7(4)
def pattern8(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end=" ")
        for j in range(2*i-1):
            print("*",end=" ")
        for j in range(n-i):
            print(" ",end=" ")
        print()

    return
pattern8(4)




