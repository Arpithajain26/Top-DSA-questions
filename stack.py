
size=5
stack=[]
top=-1
def push():
    global top
    if top==size-1:
        print("stack is overflow")
    else:
        elm=int(input("enter the elm: "))
        top+=1
        stack.append(elm)
def pop():
    global top
    if top==-1:
        print("stack is underflow")
    else:
        num=stack.pop()
        top=-1
        print("poped element is ",num)
def display():
    global top
    if top==-1:
        print("stack is empty")
    else:
        for i in range(top,-1,-1):
            print(stack[i],end=" ")
            print()
while(1):
    print("1.push 2.pop 3.display 4.quit")
    ch=int(input("enter your choice  "))
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        display()
    else:
        exit()

    
           
        

        
