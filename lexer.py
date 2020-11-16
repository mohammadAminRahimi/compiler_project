from ply import lex

class Lexer:

    reserved = {
        'in':'IN' , 'not':'NOT' , 'or':'OR' , 'and':'AND' ,
        'for':'FOR' , 'where':'WHERE' , 'on':'ON', 'while':'WHILE' , 'elseif':'ELSEIF' , 'else':'ELSE' , 'if':'IF' ,
        'main':'MAIN' , 'return':'RETURN' , 'print':'PRINT' , 'function':'FUNCTION' ,
        'False':'FALSE' , 'True':'TRUE',
        'bool':'BOOLEAN' , 'float':'FLOAT' , 'int':'INTEGER'
    }

    tokens = [
        'ERROR',
        'COMMA', 'COLON', 'SEMICOLON',
        'RSB', 'LSB', 'RRB', 'LRB', 'RCB', 'LCB', 
        'NE', 'EQ', 'LE', 'LT', 'GE', 'GT',
        'MOD', 'DIV', 'SUM', 'SUB', 'MUL', 'ASSIGN',
        'FLOATNUMBER', 'INTEGERNUMBER',
        'ID'
    ] + list(reserved.values())


    t_COMMA = r','
    t_COLON = r':'
    t_SEMICOLON = r';'
    t_RSB = r'\]'
    t_LSB = r'\['
    t_RRB = r'\)'
    t_LRB = r'\('
    t_RCB = r'\}'
    t_LCB  = r'\{'
    t_NE = r'!='
    t_EQ = r'==' 
    t_LE = r'<='
    t_LT = r'<'
    t_GE = r'>='
    t_GT = r'>'
    t_MOD = r'%'
    t_DIV = r'\/'
    t_SUM = r'\+'
    t_SUB = r'\-'
    t_MUL = r'\*'
    t_ASSIGN = r'=' 
    t_ignore  = ' \t'


    def t_ID(self, t):
        r'[a-z_][a-zA-Z_0-9]* | True | False'
        t.type = self.reserved.get(t.value,'ID')    # Check for reserved words
        return t


    def t_ERROR(slef, t):
        r"""\d+[a-zA-Z_][a-zA-Z_0-9\.]*  |   \d+\.\d+[a-zA-Z_\.][a-zA-Z_0-9\.]*   |   [\*\/\%\-\+]([\n\t\s]*[\*\/\%\-\+])+ |
            [A-Z][a-zA-Z_0-9]*  | \d{10}\d*\.\d+ | \d{10}\d*"""
        return t


    def t_FLOATNUMBER(self, t):
        r'\d{1,9}\.\d+'
        t.value = float(t.value)
        return t


    def t_INTEGERNUMBER(self, t):
        r'\d{1,9}'
        t.value = int(t.value)
        return t


    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
 

    def t_error(slef, t):
        t.type = 'ERROR'
        t.lexer.skip(1)


    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer