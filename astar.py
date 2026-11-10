import math
import random
import heapq as h

def heur(s, goal):
    return math.sqrt( (goal[0] - s[0])**2 + (goal[1] - s[1])**2)
    #return abs(goal[0] - s[0]) + abs(goal[1] - s[1])


def algo(s, goal, _map, _mapDict, rows, cols):
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
            return path[::-1], g[goal],s, goal

        random.shuffle(nexts)

        for r, c in (nexts):
            next = (curr[0] + r, curr[1] + c)

            if 0 <= next[0] < rows and 0 <= next[1] < cols:
                if _mapDict[_map[next[0]][next[1]]][1] == float('inf'):
                    continue

                tent_g = g[curr] + _mapDict[_map[next[0]][next[1]]][1]

                if tent_g < g.get(next, float('inf')):
                    parent[next] = curr
                    g[next] = tent_g
                    f[next] = tent_g + heur(next, goal)

                    if next not in OPENED:
                        h.heappush(OPEN, (f[next],next))
                        OPENED.add(next)
    return None


def search(s_list, goal_list, _map, _mapDict, rows, cols):
    minPath = []
    minC = float('inf')
    st = tuple()
    go = tuple()

    for s in s_list:
        for g in goal_list:
            p,c,_s,_g = algo(s,g, _map, _mapDict, rows, cols)

            print(c)

            if c < minC:
                minC = c
                minPath = p
                st = _s
                go = _g


    return minPath, minC, st, go