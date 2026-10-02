# Python Program to Check If Two Numbers are Amicable Numbers or Not
def factor_sum(n):
    factor=[]
    for i in range(1,n):
        if n%i==0:
            factor.append(i)
    return sum(factor)

n1=int(input("Enter the first number : "))
n2=int(input("Enter the second number : "))

sum1=factor_sum(n1)
sum2=factor_sum(n2)

if sum1==n2 and sum2==n1:
    print(f"{n1} and {n2} are Amicable number ")
else:
    print(f"{n1} and {n2} are not Amicable number")