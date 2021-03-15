# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table):
    # find parent and compress path
    pointing_to= parent[ table]
    if ( pointing_to != table) and ( parent[ pointing_to] != pointing_to):
        parent[ table]= getParent( parent[ pointing_to])
    return parent[table]

def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)
    if realDestination == realSource:
        return False

    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size

    lines[ realDestination]+= lines[ realSource]
    lines[ realSource]= 0
    parent[ source]= destination
    ans = max(lines)
    
    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)
    
