#Python Program to Check Armstrong Number
n=int(input("Enter the number : "))

temp=str(n)
l=len(temp)
temp1=n
sum=0
while temp1>0:
    digit=temp1%10
    sum=sum+digit**l
    temp1=temp1//10

if sum==n:
    print(f"{n} is armstrong number")

else:
    print(f"{n} is not armstrong number")