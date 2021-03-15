class SATInstance:

    def __init__( self):
        self.variables= []
        self.variable_table= dict()
        self.clauses= []
    
    def parse_add_clause( self, clause):
        c= []
        for literal in clause.split():
            neg= 1 if literal.startswith( '-') else 0
            var= literal[ neg: ]
            if var not in self.variables:
                self.variables.append( var)
                self.variable_table[ var]= len( self.variable_table)
            c.append( ( self.variable_table[ var] << 1 ) | neg)
        self.clauses.append( tuple( set( c)))

    @classmethod
    def from_file( cls, file):
        instance= cls()
        for line in file:
            line= line.strip()
            if len( line) > 0 and not line.startswith( '#'):
                instance.parse_add_clause( line)
        return instance

    def literal_to_string( self, literal):
        s= '~' if literal & 1 else ''
        return s + self.variables[ literal >> 1]

    def clause_to_string( self, clause):
        return ' '.join( self.literal_to_string( l) for l in clause)

    def assignment_to_string( self, assignment, brief= False, startswith= ''):
        literals= []
        for neg, v in ( ( a, v) for a, v in zip( assignment, self.variables)):
            if neg and not brief:
                literals.append( '~' + v)
            elif neg:
                literals.append( v)
        return ' '.join( literals)