
front=-1
rear=-1
def Enqueue():
    global front,rear
    if rear==n-1:
        print("Queue Full")
    elif front==-1:
         a=input("Enter the value:")
         front+=1
         rear+=1
         s[rear]=a
    else:
        a=input("Enter the value:")
        rear+=1
        s[rear]=a
def Dequeue():
    global front,rear
    if front==-1:
        print("Queue Empty")

    elif front==rear:
        print(s[front])
        front=-1
        rear=-1
    else:
        print(s[front])
        front+=1
def front_elm():
     if front==-1:
        print("Queue Empty")
     else:
        print(s[front])
def rear_elm():
     if rear==-1:
        print("Queue Empty")
     else:
        print(s[rear])
    
def isempty():
    if(front==-1):
        print("True")
    else:
        print("False")
def isfull():
    if(rear==n-1):
        print("True")
    else:
        print("False")

n=int(input("Enter the size of Queue:"))
s=[None]*n
while(True):
    print("Queue OPERATIONS")
    print("1.Enqueue Element")
    print("2.Dequeue Element")
    print("3.Front Element")
    print("4.Rear Element")
    print("5.Check if queue empty")
    print("6.Check if queue is full")
    print("7.Exit")
    op=int(input("Choose Option:"))
    if op==1:
        Enqueue()
    elif op==2:
        Dequeue()
    elif op==3:
        front_elm()
    elif op==4:
        rear_elm()
    elif op==5:
        isempty()
    elif op==6:
        isfull()
    elif op==7:
        print("Exiting..")
        break
    else:
        print("Invalid Option")

        


