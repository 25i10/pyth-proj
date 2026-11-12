import heapq as h
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
            p,c,_exp,f = algo(s,g, _map, _mapDict, rows, cols)
    
            #print(c)
    
            if f and c < minC:
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

    OPEN = []
    CLOSED = set()
    pathRec = {s:(None,0)}
    path = []
    cst = 0

    h.heappush(OPEN,(heur(s,goal),s))

    while OPEN:
        hr, cur = h.heappop(OPEN)
        if cur == goal:
            
            cst = pathRec[cur][1]
            while cur in pathRec:
                path.append(cur)
                cur = pathRec[cur][0]
            found = True
            break

        if cur not in CLOSED:
            CLOSED.add(cur)

            for r, c in (nexts):
                next = (cur[0] + r, cur[1] + c)
                
                if 0 <= next[0] < rows and 0 <= next[1] < cols and next not in CLOSED:
                    exploredStates += 1

                    if mapDict[map[next[0]][next[1]]][1] == float('inf'):
                        continue

                    cst = pathRec[cur][1] + mapDict[map[next[0]][next[1]]][1]
                    pathRec[next] = (cur,cst)
                    h.heappush(OPEN,(heur(next,goal),next))


    return path, cst, exploredStates, found



    
