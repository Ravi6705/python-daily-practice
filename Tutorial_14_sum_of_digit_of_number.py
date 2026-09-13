# This is a Python Program to find the sum of digits in a number.
n=int(input("Enter the number : "))
temp=n
m=0
if n>0:
   while temp>0:
     digit=temp%10
     m=m+digit
     temp=temp//10

   print(f"sum of the digit of the number {n} is : {m} ")
else:
   print("enter the positive number " )

# second method using recursive function 
l=[]
def sum_digit(b):
   if b==0:
      return l
   last=b%10
   l.append(last)
   sum_digit(b//10)
sum_digit(n)
print(sum(l))

