#Uses python3

import sys
import queue

def distance(adj, s, t):
    #write your code here

    queue= []
    dist= [0]*len( adj)

    def bfs( v):
        nonlocal queue
        if v== t:
            return
        for i in adj[ v]:
            if not dist[ i] and i != s:
                queue= [i] + queue
                dist[ i]= dist[ v] + 1
        if not queue:
            return
        bfs( queue.pop())

    bfs( s)
    if not dist[ t]:
        return -1
    return dist[ t]

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
