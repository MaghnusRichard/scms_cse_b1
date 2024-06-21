#Stack functions push,pop,peek,isempty,isfull
top=-1

def push():
    global top
    if top==n-1:
        print("Stack Full")
    else:
        a=input("Enter the value:")
        top+=1
        s[top]=a
def pop():
    global top
    if top==-1:
        print("Stack Empty")
    else:
        print(s[top])
        top=top-1
def peek():
     if top==-1:
        print("Stack Empty")
     else:
        print(s[top])
    
def isempty():
    if(top==-1):
        print("True")
    else:
        print("False")
def isfull():
    if(top==n-1):
        print("True")
    else:
        print("False")
def mid_elm():
    if top==-1:
        print("Stack Empty")
    else:
        print(s[top//2])

n=int(input("Enter the size of stack:"))
s=[None]*n
while(True):
    print("STACK OPERATIONS")
    print("1.Push Element")
    print("2.Pop Element")
    print("3.Peek Element")
    print("4.Check if stack empty")
    print("5.Check if stack is full")
    print("6.Display Middle Element")
    print("7.Exit")
    op=int(input("Choose Option:"))
    if op==1:
        push()
    elif op==2:
        pop()
    elif op==3:
        peek()
    elif op==4:
        isempty()
    elif op==5:
        isfull()
    elif op==6:
        mid_elm()
    elif op==7:
        print("Exiting..")
        break
    else:
        print("Invalid Option")

        


