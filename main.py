import astar

rows = 60
cols = 160
map = [['path' for _ in range(cols)] for _ in range(rows)]


#■
mapDict = {'path' : [' ',1], 'ground':['_',1], 'ins':['=',float('inf')], 'wall' : ['■',float('inf')], 'plant':['|',float('inf')],'trace':'□'}

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


def displayMap(path,s,g):
    for i in range(rows):
        for j in range(cols):
            if(i ,j) == s or (i,j) == g:
                print('×',end='')
                continue
            elif (i, j) in path:
                print(mapDict['trace'],end='')
                continue

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

blockCreate(80,2,119,9,b='R')     #Arjuna
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
blockCreate(40,11,59,20,b='P')
blockCreate(40,25,59,32,b='P')
blockCreate(40,33,59,40,b='P')


# in the format (y,x)
entries = {'lab':[(10,31),(21,15)], 'acad':[(24,15),(41,15)], 'test':[(58,158)], 'admin':[(58,15)], 'bhost':[(45,142)],
    'mess' : [(58,80)], 'jhost':[(50,104)], 'anhost':[(42,115)],
    'pems1' : [(15,39),(21,50)], 'pems2':[(28,39),(24,50)], 'pems3':[(36,39)],
    'cafe' : [(5,39)], 'arj':[(1,100)], 'med':[(35,117)], 'ulti':[(36,133)]
}
inpKey = {'A':'acad','L':'lab','N':'admin','P1':'pems1','P2':'pems2','P3':'pems3','J':'jhost','S':'bhost','+':'med','C':'cafe','R':'arj','U':'ulti','M':'mess','JA':'anhost'}

print("Key :\nA - Academics\tL - Laboratory\tN - Admin\nP1, P2, P3 - Pems Blocks\nJ - Jasmine Hostel\tJA - Jasmine Annex\tS - Ashwatha/Ashoka\nM - Mess\n+ - Medical Center\nR - Sports Complex\nU - Ultimate Store\tC - Cafeteria")

while(True):
    a = input("\nEnter starting place : ").upper()
    if a not in inpKey.keys():
        print("Not valid, enter from key")
        continue
    break

while(True):
    b = input("\nEnter destination place : ").upper()
    if b not in inpKey.keys():
        print("Not valid, enter from key")
        continue
    break

#path, c = astar.algo(entries['admin'][0],entries['bhost'][0],map,mapDict,rows,cols)
path, c, st, goal = astar.search(entries[inpKey[a]],entries[inpKey[b]],map,mapDict,rows,cols)

displayMap(path, st, goal)
print("\nTotal Cost",c)