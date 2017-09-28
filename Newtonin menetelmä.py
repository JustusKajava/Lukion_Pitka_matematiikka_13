#Newtonin menetelmä nollakohdan etsimiseen

def f(x):#f(x) on tutkittava yhtälö, jolle etsitään nollakohtaa
	return x**2
def Df(x):#Df(x) on f'(x), eli f(x):n derivaatta
	return 2*x
#Kysytään ohjelman ajajalta arvausta
x0 = float(input("Anna arvaus nollakohdalle > "))
for i in range(10):
	x0 = x0 - f(x0)/Df(x0)
	print("x"str(i) +" = "+ str(x0))
