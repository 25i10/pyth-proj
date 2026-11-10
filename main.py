import heapq as h
import random
import math

rows = 60
cols = 160
map = [['path' for _ in range(cols)] for _ in range(rows)]

mapDict = {'path' : [' ',1], 'ground':['.',1], 'ins':['=',float('inf')], 'wall' : ['■',float('inf')], 'plant':['|',float('inf')]}

for i in range(rows):
    if(i > 0 and i < rows-1):
        map[i][0] = 'wall'
        map[i][cols-1] = 'wall'
    else:
        for j in range(cols):
            map[i][j] = 'wall'


def blockCreate(x1,y1,x2,y2,t='wall',b='0'):
    for i in range(rows):
        for j in range(cols):
            if(t == 'wall'):
                if( (i == y1 and j>=x1 and j <= x2) or (i == y2 and j>=x1 and j <= x2) or (j == x1 and i>=y1 and i <= y2) or (j == x2 and i>=y1 and i <= y2)):
                    map[i][j] = 'wall'
                elif(i > y1 and i<y2 and j>x1 and j<x2):
                    map[i][j] = 'ins_'+b
            else:
                if(i >= y1 and i<=y2 and j>=x1 and j<=x2):
                    map[i][j] = t


def displayMap(path):
    for i in range(rows):
        for j in range(cols):
            if (i, j) in path:
                print('x',end='')

            elif map[i][j].split('_')[0] == 'ins':
                print(map[i][j].split('_')[1],end='')
                #print(mapDict['ins'][0],end='')
            else:
                print(mapDict[map[i][j]][0],end='')
        print()





blockCreate(3,2,30,20,b='L')      #Lab
blockCreate(3,25,30,40,b='A')     #Acads
blockCreate(3,45,30,57,b='N')     #Admin
blockCreate(60,43,100,57,b='M')   #Mess
blockCreate(40,2,59,9,b='C')      #cafeteria

blockCreate(40,43,59,57,'plant')

blockCreate(80,2,120,9,b='R')     #Arjuna
blockCreate(60,2,79,9,'plant')

blockCreate(121,1,158,29,'plant')   #construction on right

#hostels
blockCreate(123,43,140,57,'plant')
blockCreate(105,43,120,57,b='J')  #jasmine
blockCreate(143,30,158,57,b='S')  #ashwatha/ashoka


blockCreate(60,10,120,40,'ground')      #ground
blockCreate(118,30,124,40,b='+')  #medical
blockCreate(125,30,142,35,b='U')


#PEMS
blockCreate(40,11,59,20)
blockCreate(40,25,59,32)
blockCreate(40,33,59,40)












def heur(s, goal):
    return math.sqrt( (goal[0] - s[0])^2 + (goal[1] - s[1])^2)
    #return abs(goal[0] - s[0]) + abs(goal[1] - s[1])




def astar(s, goal):
    nexts = [(-1,0),(1,0),(0,-1),(0,1)]

    OPEN = []
    OPENED = {s}
    parent = {}
    g = {s: 0}
    f = {s: heur(s,goal)}
    h.heappush(OPEN, (0, s))

    while OPEN:
        curr = h.heappop(OPEN)[1]
        OPENED.remove(curr)

        if(curr == goal):
            path = []
            while curr in parent:
                path.append(curr)
                curr = parent[curr]
            path.append(s)
            return path[::-1], g[goal]

        random.shuffle(nexts)

        for r, c in (nexts):
            next = (curr[0] + r, curr[1] + c)

            if 0<= next[0] < rows and 0 <= next[1] < cols:
                if mapDict[map[next[0]][next[1]]][1] == float('inf'):
                    continue

                tent_g = g[curr] + mapDict[map[next[0]][next[1]]][1]

                if tent_g < g.get(next, float('inf')):
                    parent[next] = curr
                    g[next] = tent_g
                    f[next] = tent_g + heur(next, goal)

                    if next not in OPENED:
                        h.heappush(OPEN, (f[next],next))
                        OPENED.add(next)
    return None


# in the format (y,x)
entries = {'Lab1':(10,31)}


path, c = astar(entries['Lab1'],(58,158))

displayMap(path)
print("\nTotal Cost",c)