#Uses python3

import sys
import queue


def shortest_paths(adj, cost, s, distance, reachable, shortest):
    #write your code here

    dist= distance
    dist[ s]= 0

    def bfs( node):
        for i, v in enumerate( adj[ node]):
            sum= cost[ node][ i] + dist[ node]
            if dist[ v] > sum:
                dist[ v]= sum

    for i in range( len( adj)):
        if i == len( adj) - 1:
            cur_dist= dist.copy()
        for v in range( len( adj)):
            bfs( v)

    checked_neg= []
    q= queue.Queue()

    for i, v in enumerate( dist):
        if cur_dist[ i] != v:
            q.put( i)
        if v < 10**19:
            reachable[ i]= 1

    def neg_cycle_check( node):
        for v in adj[ node]:
            if v not in checked_neg:
                q.put( v)
    
    while not q.empty():
        neg= q.get()
        checked_neg.append( neg)
        shortest[ neg]= 0
        neg_cycle_check( neg)


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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortest_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

