n=int(input("Enter the number : "))
divisor=[]
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")
        divisor.append(i)
print("")
print(f"all the divisor of {n} are",divisor)




