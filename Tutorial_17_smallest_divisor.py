n=int(input("enter the number : "))
for i in range(2,n+1):
    if n%i==0:
        print(f"smallest divisor of {n} is {i}")
        break






#using list meathod 
l=[]
for d in range(2,n+1):
    if n%d==0:
        l.append(d)

print(f"the smallest divisor of {n} is {l[0]}")

# we can also use the min() function to find the smallest divisor of a number
# for maximum divisor we can use max() function