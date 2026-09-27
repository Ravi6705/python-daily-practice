def cheack_prime(num,d):
    if d==1:
         return True
    elif num%d==0:
        return False
    
    return cheack_prime(num,d-1)
num=int(input("Enter the number : "))
if num<=1:
    print(f"{num} is not  prime number ")
elif cheack_prime(num,num-1):
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")


