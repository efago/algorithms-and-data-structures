#Uses python3

import sys
import queue


def distance(adj, cost, s, t):
    #write your code here

    if s== t:
        return 0

    cur_dist= [ 1000]*len( adj)
    cur_dist[ s]= 0
    q = queue.PriorityQueue()

    q.put(( 0, s))
    prev= [ -1]*len( adj)
    
    while not q.empty():
        node_cost, node= q.get()
        if node== t:
            break
        for i, v in enumerate( adj[ node]):
            add_cost= cost[ node][ i] + node_cost
            if add_cost < cur_dist[ v]:
                cur_dist[ v]= add_cost 
                prev[ v]= node
                q.put( ( cur_dist[ v], v))

    def chain( parent, child):
        nonlocal dist
        idx= cost[ parent].index( child)
        dist+= cost[ parent][ idx]
        
        if parent != s:
            chain( prev[ parent], parent)

    if cur_dist[ t] != 1000:
        dist= 0
        chain( prev[ t], t)
    else:
        dist= -1
    
    return dist


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
