#Python Program to Print the Natural Numbers Summation Pattern
n=int(input("Enter the number : "))
sum=0
e=" "
for i in range(1,n+1):
    sum=sum+i
   
    if i ==1:
        e=str( i)
    else:
        e= e +" + "+ str( i)
    
    print(f"{e} = {sum}")




