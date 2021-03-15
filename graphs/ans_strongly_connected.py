#Uses python3

import sys

sys.setrecursionlimit(200000)


def number_of_strongly_connected_components(adj):
    result = 0
    #write your code here

    explored= []
    order= []
    result= 0

    def compute_post( v):
        if v not in explored:
            explored.append( v)
        for i in adj[ v]:
            if i not in order and i not in explored:
                compute_post( i)
                
        order.append( v)

    def explore( v):
        for i in adj[ v]:
            if i not in explored:
                explored.append( i)
                explore( i)

    for i in range( len( adj)):
        if i not in order:
            compute_post( i)

    explored= []
    for i in order:
        if i not in explored:
            explored.append( i)
            result+= 1
            explore( i)
    
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
    print(number_of_strongly_connected_components(adj))
    #a= number_of_strongly_connected_components( adj)
    #for i in a:
       # print( i + 1, a[ i] + 1)
