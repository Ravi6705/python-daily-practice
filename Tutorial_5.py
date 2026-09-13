# This is a Python Program to read a number n and compute f(x)=n+nn+nnn.
n=int(input("Enter a number : "))
temp=str(n)
temp1=temp+temp
temp2=temp+temp+temp
f=n+int(temp1)+int(temp2)
print(f"the value of the f(x) is : {f} ")
print("the value of the f(x) is : %d"%(f))