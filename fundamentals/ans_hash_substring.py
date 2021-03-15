# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    pattern_hash= polyhash( pattern)
    text_hash= precompute( len( pattern), text)
    return [
        i 
        for i in range( len(text) - len(pattern) + 1) 
        if ( text_hash[ i] == pattern_hash) and \
             (are_equal( pattern, text[ i: i + len( pattern)]))
    ]

def precompute( len_pattern, text):
    H= np.zeros( len( text) - len_pattern + 1)
    H[ -1]= polyhash( text[ -len_pattern: ])
    y= 1
    for i in range( len_pattern):
        y= ( y * x)%p
    for i in range( len( text) - len_pattern - 1, -1, -1):
        H[ i]= ( x * H[ i + 1] + ord( text[ i]) - y*ord(text[ i + len_pattern])) % p
    return H

def polyhash( phrase):
    hash= 0
    for i in reversed( phrase):
        hash= ( hash * x + ord( i))%p
    return hash

def are_equal( pattern1, pattern2):
    if pattern1 == pattern2:
        return True
    return False

if __name__ == '__main__':
    import numpy as np
    p= 1000000007
    x= 263
    print_occurrences(get_occurrences(*read_input()))

