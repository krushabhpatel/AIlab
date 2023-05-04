import time
global j1
j1=0
j2=0
C1 = int(input("\n Enter caapacity of jug 1 : "))
C2 = int(input("\n Enter caapacity of jug 2 : "))


def gcd(a,b): 
    if(b==0):
        return a
    return gcd(b,a%b)

def fill():
    global j1
    j1 = C1

def transfer():
    global j1 , j2
    diff = (C2-j2)
    j2 = C2
    j1 = j1-diff

def empty():
    global j2
    j2 = 0
    
d = int(input("\n Enter amount need to be measured : "))

start = time.time()
if(d % gcd(C1,C2) != 0 or max(C1,C2) < d) :
    print("No Solution Exists!")
    end = time.time()
    print("Time Taken : ",(end-start))
else:
    if(C1 < C2):
        C1 , C2 = C2 , C1
    print(C1,C2)
    while(1):
        fill()
        print("( ",j1,", ",j2," )")
        transfer()
        print("( ",j1,", ",j2," )")
        empty()
        print("( ",j1,", ",j2," )")
        if(j1>C2):
            transfer()
            empty()
        j1,j2 = j2,j1
        print("( ",j1,", ",j2," )")
        if(j1==d or j2==d):
            break
    end = time.time()
    print("Time Taken : ",(end-start))