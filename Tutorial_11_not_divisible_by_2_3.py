#This is a Python Program to print all integers that aren’t divisible by either 2 or 3 in given range
n=int(input("enter the starting number of range :"))
m=int(input("enter the ending number of the range :"))
not_divisible=[]
divisible=[]
for i in range(n,m+1):
    if (i%2!=0) and (i%3!=0):
        print(i,end=" ")
        not_divisible.append(i)
    else:
        divisible.append(i)
print("")
print("divisible numbers are : ",divisible)