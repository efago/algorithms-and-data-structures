import sys
from watchlist import update_watchlist

def solve(instance, watchlist, assignment, d, verbose):
    if d == len( instance.variable_table):
        yield assignment
        return
    
    for a in [ 0, 1]:
        assignment[ d]= a
        if update_watchlist( instance, watchlist, ( d << 1) | a,
            assignment, verbose):
            yield from solve( instance, watchlist, assignment, d + 1, 
                    verbose)
    assignment[ d]= None