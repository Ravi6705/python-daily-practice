#This is a Python Program to find those numbers which are divisible by 7 and multiple of 5
#in the given range 

n=int(input("enter the starting number : "))
m=int(input("enter the ending number : "))
for i in range(n,m+1):
    if (i%7==0) and (i%5==0):
        print(i,end=" ")
    