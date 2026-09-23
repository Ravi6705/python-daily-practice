n=int(input("Enter the number : "))
temp=n
sum=0
for i in range(1,temp):
    if temp%i==0:
        sum=sum+i
if sum==n:
    print(f"{n} is the perfect number")
else:
    print(f"{n} is not perfect number")
