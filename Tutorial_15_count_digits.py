# using string method 
n=int(input("Enter the number : "))
temp=str(n)
print("The digits of the number are : ",len(temp))

# using while loop 
temp1=n
count=0
while temp1>0:
    count=count+1
    temp1=temp1//10
print(f"the digits of the given number are : {count}")


