#write a python program to reverse the number
n=int(input("enter the number: "))
temp=n
rev=0
while temp>0:
    last=temp%10
    rev=rev*10+last
    temp=temp//10

print(f"reverse of the {n} number is :{rev}")

