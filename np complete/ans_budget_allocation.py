# python3
import os
from sys import stdin
from itertools import combinations

n, m = list(map(int, stdin.readline().split()))
A = []
for i in range(n):
  A += [list(map(int, stdin.readline().split()))]
b = list(map(int, stdin.readline().split()))

clauses= []

def atleast_one():
    clauses.append( list( range( 1, m + 1)))

def invalids():
    for eq, a in enumerate( A):
        idx= [ i for i in range( m) if a[ i] != 0]
        size= m
        while size:
            for comb in combinations( idx, size):
                addition= 0
                for i in comb:
                    addition+= a[ i]
                if addition > b[ eq]:
                    clauses.append([ -(i+1) if i in comb else (i+1) for i in idx])
            size-= 1

atleast_one()
invalids()

def process_for_solver():
    with open( 'budget.txt', 'w') as f:
        for clause in clauses:
            f.write( ' '.join( str( l) for l in clause) + '\n')

process_for_solver()
os.system( 'python ../../sat.py -i budget.txt')
