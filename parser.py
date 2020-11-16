from ply import yacc
from lexer import Lexer

class Parser:

    tokens = Lexer().tokens


    # precedence = (
    #     ('left', 'FUNCTION', 'ID')
    # )

    def __init__(self):
        pass


    # initial point
    def p_program(self, p):
        """program : declist MAIN LRB RRB block 
        | MAIN LRB RRB block"""
        print("program : declist main ( ) block")


    # empty production
    def p_empty(slef, p):
        'empty : '
        print("empty : ")
        pass
        


    # declaration related products
    def p_declist_to_dec(slef, p):
        """
        declist : dec 
        | declist dec 
        """
        print("declist : dec | declist dec | empty")


    def p_dec_to_var_or_func(self, p):
        """dec : vardec 
        | funcdec """
        print("dec : vardec | funcdec ")


    def p_type_to_type(self, p):
        """type : INTEGER 
        | FLOAT 
        | BOOLEAN"""
        print("type : INTEGER | FLOAT | BOOLEAN")


    def p_iddec_to_id(self, p):
        """iddec : ID 
        | ID LSB exp RSB 
        | ID ASSIGN exp"""        
        print("iddec : ID | ID LSB exp RSB | ID ASSIGN exp")


    def p_idlist_to_iddec(self, p):
        """idlist : iddec 
        | idlist COMMA iddec"""
        print("idlist : iddec | idlist COMMA iddec")


    def p_vardec_to_idlist_and_tyep(self, p):
        """vardec : idlist COLON type SEMICOLON"""
        print("vardec : idlist COLON type SEMICOLON")


    def p_funcdec_to_dec(self, p):
        """funcdec : FUNCTION ID LRB paramdecs RRB COLON type block 
        | FUNCTION ID  LRB paramdecs RRB block"""
        print("funcdec → fun id (paramdecs): type block | fun id (paramdecs) block")
     # Error rule for syntax errors


    def p_paramdecs_to_paramdecslist(self, p):
        """paramdecs : paramdecslist 
        | empty"""
        print("paramdecs → paramdecslist | 𝜖")


    def p_paramdecslist_to_paramdec(self, p):
        """paramdecslist : paramdec
        | paramdecslist COMMA paramdec"""


    def p_paramdec_to_id(self, p):
        """paramdec : ID COLON type
        | ID LSB RSB COLON type"""

    def p_block_to_statement(self, p):
        """block : LCB RCB""" #stmtlist
        print("{ stmtlist }")


    def p_temp(self, p):
        """exp : LSB RSB """


    # def p_error(self, p):
    #     print("Syntax error in input!")

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
