import sys
from argparse import ArgumentParser
from argparse import FileType
from satInstance import SATInstance
from watchlist import setup_watchlist
import recursive

def generate_assignmnets(instance, solver, verbose=False):
    watchlist= setup_watchlist( instance)
    if not watchlist:
        return ()
    assignment= [ None] * len( instance.variables)
    return solver.solve( instance, watchlist, assignment, 0, verbose)


def run_solver(input_file, output_file, solver, brief, verbose, output_all,
               starting_with):
    instance= SATInstance.from_file( input_file)
    assignments= generate_assignmnets( instance, solver, verbose)
    count= 0
    for assignment in assignments:
        count+= 1
        if verbose:
            print( f'Found satisfying assignment #{count}')
            assignment_str= instance.assignment_to_string( assignment)
            output_file.write( assignment_str + '\n')
        if not output_all:
            break
    if count == 0:
        print( 'No solution exists', file= sys.stderr)
    else:
        print( f'{count} solutions exists', file= sys.stderr)

def main():
    args= parseArgs()
    with args.input:
        with args.output:
            run_solver( args.input, args.output, args.solver, args.brief,
                        args.verbose, args.all, args.starting_with)

def parseArgs():
    parser= ArgumentParser()
    parser.add_argument( '-v', '--verbose', help= 'verbose output', 
                        action= 'store_true')
    parser.add_argument( '--iterative', help= 'use iterative algorithm', 
                        default= recursive, dest= 'solver', action= 
                        'store_const', const= 'iterative')
    parser.add_argument( '-a', '--all', action= 'store_true', 
                        help= 'output all possible solutions')
    parser.add_argument( '-b', '--brief', help= 'only show true literals',
                        action= 'store_true')
    parser.add_argument( '--starting_with', default= '', 
                        help= 'output literals starting with given str')
    parser.add_argument( '-i', '--input',help='read from file not stdin',
                        type= FileType( 'r'), default= sys.stdin)
    parser.add_argument( '-o', '--output', type= FileType( 'w'), default=
                        sys.stdout, help= 'output to file not stdout')
    return parser.parse_args()

if __name__ == '__main__':
    main()
