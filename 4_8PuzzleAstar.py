import sys, time

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

def printM(m):
    for i in m: 
        print(i)
    print('')

def swap(xc,yc,x1,y1,m):
    temp = m[xc][yc]
    m[xc][yc] = m[x1][y1]
    m[x1][y1] = temp

def findCost(curr, goal):
    cost=0
    for i in range(3):
        for j in range(3):
            if curr[j][i]==goal[j][i]:
                cost+=1
    return cost
q=[]
visited=[]
inital = []
goal = []
# inital = [[8,7,4],[3,2,5],[1,6,'b']]
# goal = [[1,2,3],[4,5,6],[7,8,'b']]

print("Give the input for START node: ")
for i in range(3):
    ele = []
    for j in range(3):
        num = input("Enter value"+str(i)+str(j)+": ")
        ele.append(num)
    inital.append(ele)

print("Give the input for END node: ")
for i in range(3):
    ele = []
    for j in range(3):
        num = input("Enter value"+str(i)+str(j)+": ")
        ele.append(num)
    goal.append(ele)


m = inital
xc, yc = index_2d(m,'b')
q.append([xc,yc,m, 0])
r=[1,-1,0,0]
c=[0,0,1,-1]

def fourthele(ele):
    return ele[3]

s = time.time()
while len(q) > 0:
    q.sort(key=fourthele, reverse=True)
    xc, yc, m, cost = q.pop(0)

    if m in visited:
        continue
    visited.append(m)
    for i in range(0,4):
        x1 = xc + r[i]
        y1 = yc + c[i]
        if x1 < 0 or x1 > 2 or y1 < 0 or y1 > 2:
            continue
        m_copy = [row[:] for row in m]
        swap(xc, yc, x1, y1, m_copy)
        if m_copy in visited:
            continue
        q.append([x1, y1, m_copy, findCost(m_copy, goal)])
        print(findCost(m_copy, goal))
        printM(m_copy)
        if m_copy == goal:
            print('Done')
            e = time.time()
            print(e-s)
            sys.exit()