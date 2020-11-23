from lexer import Lexer
from parser import Parser
# from parser import Parser
lexer = Lexer().build()
line=0
lexer.input("""
main()
{
	if(result<10)
		if(result<1)
			print(long_live_the_king);
		else
			print(result);
}""")
while True:
    tok = lexer.token()
    if not tok: break
    if tok.lineno != line:
        line = tok.lineno
        print()
    print( tok.type , end="\t")
	
print("\n")

parser = Parser()
parser.build().parse("""
main()
{
	if(x * x == 0)
		print(a9);
	elseif(x * x == 1)
		a1 = a1 + 1;
	elseif(x * x == 4)
		a4 = a4 + 1;
	else
	{
		a9 = a9 + 1;
		long_live_the_queen;
	}
}
""", lexer, False)