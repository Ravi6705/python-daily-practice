#Write a Python program that takes in a number and checks whether it is a prime number.
number=int(input("Enter the number : "))
for i in range(2,number):
    if number==2:
        print(f"you are number is 2 which is prime number")
        break
    elif number%i==0:
        print(f"{number} is not prime number")
        break
else: 
    print(f'{number} is prime number')
        
