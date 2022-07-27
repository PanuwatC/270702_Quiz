x = [0,1]
n = int(input("Enter number to list fibonacci numbers : "))
while(n<=0):
    print("Please input number more than 0!!!")
    n = int(input("Enter number to list fibonacci numbers : "))
if(n == 1):
    print("Fibonacci numbers : ",x[0])
else:
    print("Fibonacci numbers : ",end="")
    for i in range (0,n-1):
        print(x[i],end=", ")
        x.append(x[-2] + x[-1])
    print("and",x[n-1],end=".")

