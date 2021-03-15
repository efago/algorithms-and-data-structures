import sys

def reach(adj, x, y):
    #write your code here
    explored.append( x)
    if y in adj[ x]:
        return 1
    else:
        for i in adj[ x]:
            if i not in explored and reach( adj, i, y):
                return 1
    return 0

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    edges= []
    for _ in range( m):
        edges.append( list( map( int, input().split())))
    x, y = list( map( int, input().split()))
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    explored= []
    print(reach(adj, x, y))
