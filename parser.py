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
        | MAIN LRB RRB block"""#declist MAIN LRB RRB block | MAIN LRB RRB block
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
        | ID LSB exa RSB 
        | ID ASSIGN exa"""        
        print("iddec : ID | ID LSB exa RSB | ID ASSIGN exa")


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


    def p_lvalue(self, p):
        """lvalue : ID
        | ID LSB exa RSB"""
        print("""lvalue : ID
        | ID LSB exa RSB""")


    def p_opertor(self, p):
        """operator : SUM 
        | SUB
        | MUL
        | DIV
        | MOD
        | GT
        | GE
        | LT
        | LE
        | EQ
        | NE
        """
        print("""operator : SUM 
        | SUB
        | MUL
        | DIV
        | MOD
        | GT
        | GE
        | LT
        | LE
        | EQ
        | NE
        """)


    def p_const(self, p):
        """const :  INTEGERNUMBER
        | FLOATNUMBER
        | TRUE
        | FALSE
        """
        print("""const :  INTEGERNUMBER
        | FLOATNUMBER
        | True
        | False
        """)


    def p_ex_assign(self,p):
        """exa : lvalue ASSIGN exa
        | ex
        """
        print("""exa : lvalue ASSIGN exa
        | ex
        """)
        

    def p_ex(self, p):
        """ex : NOT ex 
        | ex1
        """
        print("""ex : NOT ex 
        | ex1
        """)


    def p_ex1(self, p):
        """ex1 : ex1 AND exp
        | ex1 OR exp
        | exp
        """
        print("""ex1 : ex1 AND exp
        | ex1 OR exp
        | exp
        """)


    def p_exp(self, p):
        """exp : exp operator exp1
        | exp1
        """
        print("""exp : exp operator exp1
        | exp1
        """)


    def p_exp1(self, p):
        """exp1 : SUB exp1 
        | exp2
        """
        print("""exp1 : SUB exp1 
        | exp2
        """)


    def p_exp2(self, p):
        """exp2 : LRB exa RRB
        | const
        | ID LRB RRB
        | ID LRB explist RRB
        | lvalue
        """
        print("""exp2 : LRB exa RRB
        | const
        | ID LRB RRB
        | ID LRB explist RRB
        | lvalue
        """)


    def p_explist(self, p):
        """explist : exa
        | explist COMMA exa
        """
        print("""explist : exa
        | explist COMMA exa
        """)
    

    # def p_temp(self, p):
    #     """ex : LSB RSB """




    def p_error(self, p):
        print("Syntax error in input!")

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs, debug=True)
        return self.parser
