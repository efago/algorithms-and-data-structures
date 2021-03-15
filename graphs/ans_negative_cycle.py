#Uses python3

import sys


def negative_cycle(adj, cost):
    #write your code here

    dist= [ 0] + [ 1000]*( len( adj) - 1)

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

    if cur_dist != dist:
        return 1

    return 0


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
    print(negative_cycle(adj, cost))
