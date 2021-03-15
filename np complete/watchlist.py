import sys
from collections import deque

def dump_watchlist( instance, watchlist):
    print( 'Current watchlist: ', file= sys.stderr)
    for l, w in enumerate( watchlist):
        literal= instance.literal_to_string( l)
        clauses= ', '.join( instance.clause_to_string( c) for c in w)
        print( '{} {}'.format( literal, clauses), file= sys.stderr)
    
def setup_watchlist( instance):
    watchlist= [ deque() for _ in range( 2 * len( instance.variables))]
    for clause in instance.clauses:
        watchlist[ clause[ 0]].append( clause)
    return watchlist

def update_watchlist( instance, watchlist, false_literal, assignment, verbose):
    while watchlist[ false_literal]:
        clause= watchlist[ false_literal][ 0]
        found_alternative= False
        for literal in clause:
            v= literal >> 1
            neg= literal & 1
            if assignment[ v] is None or assignment[ v]== neg ^ 1:
                found_alternative= True
                del watchlist[ false_literal][ 0]
                watchlist[ literal].append( clause)
                break
            
        if not found_alternative:
            if verbose:
                dump_watchlist( instance, watchlist)
                print( 'Current assignment {}'.format( 
                    instance.assignment_to_string( assignment)), 
                    file= sys.stderr)
                print( 'Clause {} contradicted'.format( 
                    instance.clause_to_string( clause)), file= sys.stderr)
            return False

    return True


