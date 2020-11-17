from lexer import Lexer
from parser import Parser
# from parser import Parser
lexer = Lexer().build()
lexer.input("amin=3*2 :int; main() {}")
# while True:
#     tok = lexer.token()
#     if not tok: break
#     if tok.lineno != line:
#         line = tok.lineno
#         print()
#     print( tok.type , end="\t")

parser = Parser()
parser.build().parse("amin=3*2 :int; main() {}", lexer, False)