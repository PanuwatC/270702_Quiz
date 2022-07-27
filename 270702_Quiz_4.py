A = [False,True]
B = [False,True]
x = str.lower(input("Enter Boolean expression (ex. a and not b) : "))
for a in A:
    for b in B:
        print("A =",a,"\t, B =",b,"\tin\t \"",x,"\"\tis\t",eval(x))


