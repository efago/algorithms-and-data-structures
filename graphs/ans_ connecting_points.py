#Uses python3
import sys
import math

def minimum_distance(x, y):
    result = 0.
    #write your code here

    edges= []
    for i in range( len( x)):
        for j in range( len( x)):
            if j > i:
                dist= math.sqrt( (x[ i] - x[ j])**2 + ( y[ i] - y[ j])**2)
                edges.append([ dist, i, j])

    forest= [ {i} for i in range( len( x))]
    while edges:
        dist, a, b= edges.pop( edges.index( min( edges)))
        set_a= -1
        set_b= -1

        for i in forest:
            if a in i:
                set_a= i
                if type( set_b) is set:
                    break
            if b in i:
                set_b= i
                if type( set_a) is set:
                    break
        if set_a == set_b:
            continue
        else:
            forest.pop( forest.index( set_a))
            forest.pop( forest.index( set_b))
            forest.append( set_a.union( set_b))
            result+= dist
        if len( forest) == 1:
            print( 'single')
            break

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
