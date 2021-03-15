#Uses python3

import sys
import queue

def bipartite(adj):
    #write your code here

    queue= []
    groups= [0]*len( adj)
    is_bipartite= 1

    def bfs( v, node_group):
        nonlocal is_bipartite, queue
        if not is_bipartite:
            return
        for i in adj[ v]:
            if not groups[ i]:
                queue= [i] + queue
                groups[ i]= node_group*-1
            elif groups[ i] == node_group:
                is_bipartite= 0
                return
        if not queue:
            return
        next= queue.pop()
        bfs( next, groups[ next])

    for i in range( len( adj)):
        if not is_bipartite:
            break
        if not groups[ i]:
            groups[ i] = 1
            bfs( i, 1)

    return is_bipartite

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
