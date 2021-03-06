# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            bracket= Bracket( next, i)
            opening_brackets_stack.append( bracket)

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if ( len( opening_brackets_stack) == 0):
                opening_brackets_stack.append( i + 1)
                break
            elif opening_brackets_stack.pop().Match( next) != True:
                opening_brackets_stack.append( i + 1)
                break

    # Printing answer, write your code here
    if len( opening_brackets_stack) > 0:
        print( opening_brackets_stack[ -1])
    else:
        print( 'Success')
