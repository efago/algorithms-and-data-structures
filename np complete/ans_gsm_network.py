# python3
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
clauses= []
import itertools
import os


#convert node+color to number
def numerizer( node):
    a= node*3
    return [ a, a+1, a+2]

#converts literal to cnf
def one_in_node( clause):
    clauses.append( clause)
    for i, j in itertools.permutations( clause, 2):
        clauses.append( [ -i, -j])

def different_in_edge( node_1, node_2):
    for i in range( 3):
        clauses.append( [ -( i + node_1 * 3), -( i + node_2 * 3)])

#one in node
for i in range( 1, n + 1):
    one_in_node( numerizer( i))

#unique in edge
for i, j in edges:
    different_in_edge( i, j)

def process_for_solver():
    with open( 'gsm.txt', 'w') as f:
        for clause in clauses:
            f.write( ' '.join( str( l) for l in clause) + '\n')

process_for_solver()
os.system( 'python ../../sat.py -ai gsm.txt')