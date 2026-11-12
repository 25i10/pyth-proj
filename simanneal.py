import math
import random

def search(s_list, goal_list, _map, _mapDict, rows, cols):
    minPath = []
    minC = float('inf')
    st = tuple()
    go = tuple()
    exp = 0
    
    for s in s_list:
        for g in goal_list:
            p,c,_exp, _f = algo(s,g, _map, _mapDict, rows, cols)
    
            #print(c)
    
            if c < minC:
                minC = c
                minPath = p
                st = s
                go = g
                exp = _exp
    
    
    return minPath, minC, st, go, exp


def algo(s, goal, map, mapDict, rows, cols):
    nexts = [(-1,0),(1,0),(0,-1),(0,1)]
    exploredStates = 0
    found = False

    def heur(_s, _g):
        return math.sqrt( (_g[0] - _s[0])**2 + (_g[1] - _s[1])**2)
    
    curr = s
    h = heur(s,goal)
    T = 10.0
    path = set()
    cost = 0
    path.add(curr)

    while(h>0 and T>0.001):
        nxt = tuple()

        while True:
            n = nexts[random.randint(0,3)]
            nxt = (curr[0] + n[0], curr[1] + n[1])
            if 0 <= nxt[0] < rows and 0 <= nxt[1] < cols:
                if mapDict[map[nxt[0]][nxt[1]]][1] != float('inf'):
                    break

        exploredStates += 1
        _h = heur(nxt,goal)
        dl = h - _h

        if(dl > 0):
            curr = nxt
            h = _h
            path.add(nxt)
            cost += mapDict[map[nxt[0]][nxt[1]]][1]
        elif dl == 0:
            found = True
            pass
        elif -(dl/T) > 709:
            continue
        elif random.random() <= 1/(1+math.exp(-(dl/T))):
            curr = nxt
            h = _h
            path.add(nxt)
            cost += mapDict[map[nxt[0]][nxt[1]]][1]

        T *= 0.9999


    return path, cost, exploredStates, found
