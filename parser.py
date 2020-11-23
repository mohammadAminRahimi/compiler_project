from ply import yacc
from lexer import Lexer

class Parser:

    tokens = Lexer().tokens
    precedence = (
    ('left', 'UNMATCHED', 'MATCHED'),
    ('left', 'ELSEIF', 'ELSE'),
    ('right', 'low3'),
    ('left', 'or'),
    ('left', 'and'),
    ('left', 'not'), 
    ('left', 'ne', 'eq', 'NE', 'EQ'),
    ('left', 'gt', 'ge', 'GE', 'GT'),
    ('left', 'le', 'lt','LT', 'LE'),
    ('left', 'SUM', 'SUB','sum','sub'),
    ('left', 'MUL', 'DIV', 'MOD', 'div', 'mod', 'mul'),
    ('left', 'ASSIGN'),
    ('left', 'high'),
    ('left', 'vhigh'),
    )


    def __init__(self):
        pass


    # initial point
    def p_program(self, p):
        """program : declist MAIN LRB RRB block 
        | MAIN LRB RRB block"""
        print("program : declist MAIN LRB RRB block")


    # empty production
    def p_empty(slef, p):
        'empty : '
        print("empty : ")


    # declaration related products
    def p_declist_to_dec(slef, p):
        """
        declist : dec 
        | declist dec 
        """
        if len(p)==2:
            print("declist : dec")
        if len(p)==3:
            print("declist : declist dec ")


    def p_dec_to_var_or_func(self, p):
        """dec : vardec 
        | funcdec """
        print("dec : vardec | funcdec")


    def p_type_to_type(self, p):
        """type : INTEGER 
        | FLOAT 
        | BOOLEAN"""
        if p[1]=='int':
            print("type : INTEGER")
        if p[1]=="float":
            print("type : FLOAT ")
        if p[1]== 'bool':
            print("type : BOOLEAN")


    def p_iddec_to_id(self, p):
        """iddec : ID 
        | ID LSB exp RSB 
        | ID ASSIGN exp"""        
        if len(p)==2:
            print("iddec : ID")
        if len(p)==4:
            print("iddec : ID ASSIGN exp ")
        if len(p)==5:
            print('iddec : ID LSB exp RSB')


    def p_idlist_to_iddec(self, p):
        """idlist : iddec 
        | idlist COMMA iddec"""
        if len(p)==2:
            print("idlist : iddec")
        if len(p)==4:
            print("idlist : idlist COMMA iddec ")


    def p_vardec_to_idlist_and_tyep(self, p):
        """vardec : idlist COLON type SEMICOLON"""
        print("vardec : idlist COLON type SEMICOLON")


    def p_funcdec_to_dec(self, p):
        """funcdec : FUNCTION ID LRB paramdecs RRB COLON type block 
        | FUNCTION ID  LRB paramdecs RRB block"""
        if len(p)==9:
            print("funcdec : FUNCTION ID LRB paramdecs RRB COLON type block ")
        if len(p)==7:
            print("FUNCTION ID  LRB paramdecs RRB block")     # Error rule for syntax errors


    def p_paramdecs_to_paramdecslist(self, p):
        """paramdecs : paramdecslist 
        | empty"""
        print("paramdecs → paramdecslist | 𝜖")


    def p_paramdecslist_to_paramdec(self, p):
        """paramdecslist : paramdec
        | paramdecslist COMMA paramdec"""
        if len(p)==2:
            print("paramdecslist : paramdec")
        if len(p)==4:
            print("paramdecslist : paramdecslist COMMA paramdec") 


    def p_paramdec_to_id(self, p):
        """paramdec : ID COLON type
        | ID LSB RSB COLON type"""
        if len(p)==4:
            print('paramdec : ID COLON type')
        if len(p)==6:
            print('ID LSB RSB COLON type')


    def p_lvalue(self, p):
        """lvalue : ID LSB exp RSB"""
        print("""lvalue : ID LSB exa RSB""")


    def p_const(self, p):
        """const :  INTEGERNUMBER
        | FLOATNUMBER
        | TRUE
        | FALSE
        """
        print(p[0],p[1])
        if p[1]=='True':
            print("const : TRUE")
        elif p[1]=='False':
            print("const : FALSE")
        else:
            print("const : INTEGERNUMBER | FLOATNUMBER")


    def p_exp(self, p):
        """exp : lvalue ASSIGN exp %prec low3
        | ID ASSIGN exp %prec low3
        | ID %prec vhigh
        | LRB exp RRB %prec vhigh
        | const %prec vhigh
        | ID LRB RRB %prec vhigh
        | ID LRB explist RRB %prec vhigh
        | lvalue %prec vhigh 
        | SUB exp %prec high
        | exp SUM exp %prec sum
        | exp SUB exp %prec sub
        | exp MUL exp %prec mul
        | exp DIV exp %prec div
        | exp MOD exp %prec mod
        | exp GE exp %prec ge
        | exp GT exp %prec gt
        | exp LE exp %prec le
        | exp LT exp %prec lt
        | exp EQ exp %prec eq
        | exp NE exp %prec ne
        | exp OR exp %prec or
        | exp AND exp %prec and
        | NOT exp %prec not
        """
        if len(p)==5:
            print("exp : ID LRB explist RRB")
        if len(p)==4:
            if p[1]=="(":
                print("exp : LRB exp RRB")
            if p[2]=='(':
                print("exp : ID LRB RRB")
            if p[2] == '+':
                print('exp : exp SUM exp')
            if p[2] == '-':
                print('exp : exp SUB exp')
            if p[2] == '*':
                print('exp : exp MUL exp')
            if p[2] == '%':
                print('exp : exp MOD exp')
            if p[2] == '/':
                print('exp : exp DIV exp')
            if p[2] == '>=':
                print('exp : exp GE exp')
            if p[2] == '>':
                print('exp : exp GT exp')
            if p[2] == '<=':
                print('exp : exp LE exp')
            if p[2] == '<':
                print('exp : exp LT exp')
            if p[2] == '==':
                print('exp : exp EQ exp')
            if p[2] == '!=':
                print('exp : exp NE exp')
            if p[2] == 'and':
                print('exp : exp AND exp')
            if p[2] == 'or':
                print('exp : exp OR exp')
            if  p[2]=='=':
                print('exp : ID ASSIGN exp')
        if len(p)==3:
            if p[1]=='-':
                print('exp : SUB exp')
            if p[1]=='not':
                print('exp : NOT exp')
            if p[2]=='=':
                print('exp : lvalue ASSIGN')
        if len(p)==2:
                print('exp : lvalue | const | ID')


    def p_explist(self, p):
        """explist : exp
        | explist COMMA exp
        """
        if len(p)==4:
            print("explist :explist COMMA exp")
        else:
            print("explist : exp")
    

    ### functions for parsing statements part of grammar
    def p_block_to_statement(self, p):
        """block : LCB stmtlist RCB
        | LCB RCB
        """ #stmtlist
        if len(p)==4:
            print("block : LCB stmtlist RCB")
        else:        
            print("block : LCB RCB")


    def p_stmtlist(self, p): 
        """stmtlist : stmt 
        | stmtlist stmt 
        """
        if len(p)==2:
            print( "stmtlist : stmt") 
        else:
            print("stmtlist : stmtlist stmt")
        

    def p_cases(self, p):
        """cases : case 
        | cases case 
        """
        if len(p)==3:
            print("cases : cases case")
        if len(p)==2:
            print("cases : case")


    def p_case(self, p):
        """case : WHERE const COLON stmtlist"""
        print("case : where const : stmtlist")


    def p_s_to_matched(self, p):
        """stmt : matched %prec MATCHED
        | unmatched """
        print("stmt : matched | unmatched" )


    def p_unmatched(self, p):
        """unmatched : IF LRB exp RRB stmt elseiflist %prec UNMATCHED
        | IF LRB exp RRB matched elseiflist ELSE unmatched %prec ELSE
        | IF LRB exp RRB matched ELSE unmatched %prec ELSE
        | IF LRB exp RRB stmt %prec UNMATCHED"""
        if len(p)==9:
            print('stmt : IF LRB exp RRB stmt elseiflist ELSE stmt')
        if len(p)==7:
            if p[1]=='if':
                print('stmt : IF LRB exp RRB stmt elseiflist')
        if len(p)==6:
            print("stmt : IF LRB exp RRB stmt %prec stmt")
        if len(p)==8:
            print("stmt : IF LRB exp RRB stmt ELSE stmt ")


    def p_stmt(self, p):
        """
        matched : RETURN exp SEMICOLON
        | exp SEMICOLON
        | block
        | WHILE LRB exp RRB stmt
        | ON LRB exp RRB LCB cases RCB SEMICOLON
        | ON LRB exp RRB LCB RCB SEMICOLON
        | FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt
        | FOR LRB ID IN ID RRB stmt 
        | PRINT LRB ID RRB SEMICOLON 
        | IF LRB exp RRB matched elseiflist ELSE matched  
        | IF LRB exp RRB matched ELSE matched  
        | vardec
        """
        if len(p)==10:
            if p[1]=='for':
                print("stmt : FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt")
        if len(p)==9:
            if p[1]=="if":
                print("stmt : IF LRB exp RRB stmt elseiflist ELSE stmt")
            if p[1]=='on':
                print('stmt : ON LRB exp RRB LCB cases RCB SEMICOLON')
        if len(p)==8:
            if p[1]=='on':
                print('stm : ON LRB exp RRB LCB RCB SEMICOLON')
            if p[1]=='for':
                print('stmt : FOR LRB ID IN ID RRB stmt')
            if p[1]=='if':
                print('stmt : IF LRB exp RRB stmt ELSE stmt')
        if len(p)==6:
            if p[1]=='print':
                print("stmt : PRINT LRB ID RRB SEMICOLON")
            if p[1]=="while":
                print("stmt : WHILE LRB exp RRB stmt")
        if len(p)==5:
            pass
        if len(p)==4:
            if p[1]=='RETURN':
                print('stmt : RETURN exp SEMICOLON')
        if len(p)==3:
            if p[2]=='SEMICOLON':
                print('stmt : exp SEMICOLON')
        if len(p)==1:
            print("stmt : block | vardec")


    def p_elseiflist(self, p):
        """
        elseiflist : ELSEIF LRB exp RRB matched  
        | elseiflist ELSEIF LRB exp RRB matched    
        """
        if len(p)==7:
            print("elseiflist : elseiflist ELSEIF LRB exp RRB stmt")
        else:
            print("elseiflist : ELSEIF LRB exp RRB stmt  | empty")


    def p_error(self, p):
        print("there is some Error")


    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs, debug=True)
        return self.parser
