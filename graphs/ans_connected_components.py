#Uses python3

import sys


def number_of_components(adj):
    result = 0
    #write your code here
    explored= []
    
    def explore( v):
        explored.append( v)
        for i in adj[ v]:
            if i not in explored:
                explore( i)

    for i in range( len( adj)):
        if i not in explored:
            explore( i)
            result+= 1

    return result

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
    print( adj)
    print(number_of_components(adj))
