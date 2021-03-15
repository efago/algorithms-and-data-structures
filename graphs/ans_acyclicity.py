#Uses python3

import sys


def acyclic(adj):

    sinked= []
    current= []
    cycle= 0

    def explore( v):
        nonlocal cycle
        if cycle:
            return
        current.append( v)
        for i in adj[ v]:
            if i in sinked:
                continue
            elif i not in current and not cycle:
                explore( i)
            else:
                cycle= 1
                return
        sinked.append( v)

    for i in range( len( adj)):
        if i in sinked:
            continue
        elif not cycle:
            current= []
            explore( i)
        else:
            return 1

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))