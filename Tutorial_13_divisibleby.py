#This is a Python Program to print all numbers in a range divisible by a given number.
n=int(input("starting of range : "))
m=int(input("ending of the range : "))
divisible=int(input("divisible number : "))
for i in range(n,m+1):
    if (i%divisible==0):
        print(i,end=" ")