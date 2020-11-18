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
a4 = 0, a9 = 0, a1 = 0 , d[10]:int;
fun is_sorted_seq(x:int, y:int, z:int):bool
{
	return x <= y <= z or x >= y >= z;
}

fun number_of_even_integers(arr[]:int):int
{
	result = 0:int;
	for(i in arr)
		if(i % 2 == 0)
			result = result + 1;
	return result;
}

fun a_void_sample_use_on_where(x:int)
{
	on(x * x)
	{
		where 1:
		a1 = a1 + 1;
		73;

		where 4:
		a4 = a4 + 1;

		where 9:
		a9 = a9 + 1;

		where 0:
		print(a9);

	};
}

fun a_void_sample_use_if_else(x:int)
{
	long_live_the_queen:bool;

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

main()
{
	x5,y5,x3,x2,x1:float ;
	x5=y5=2+x3=1+x2=2*x1=0.3+0.7;

	a[x5 + x3 + 0.1],i:int;
	for(i=0;i<8;i=i+1)
		a[i] = i + (i % 3 == 2) ;
	long_live_the_king=True:bool;
	result=a_void_sample_use_on_where(a):int;
	if(result<10)
		if(result<1)
			print(long_live_the_king);
		else
			print(result);
}
""", lexer, False)