#This is a Python Program to find the binary equivalent of a number 
n=int(input("enter the number : "))
print(f"the binary equivalent nuber is {bin(n)}")


# using while and for loop
l=[]
temp=n
while temp>0:
    r=temp%2
    l.append(r)
    temp=temp//2
l.reverse()
print("binary equivalent is : ")
for i in l:
    print(i,end=" ")

