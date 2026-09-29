# Python Program to Check if a Number is a Strong Number
def main():
    n=int(input("Enter the number : "))
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n*factorial(n-1)
    temp=n
    sum=0
    while temp>0:
        digit=temp%10
        sum=sum+factorial(digit)
        temp=temp//10

    if sum==n:
        print(f"{n} is strong number")
    else:
        print(f"{n} is not strong number")

    print("Do you want to try again")
    print("1.Yes")
    print("2.NO")
    again=input("Enter the choise : ").upper()
    if again=="1" or again=="YES":
        main()
    else:
        print("Thankyu for using this ")




main()






#we can also use for loop to find the factorial 
def factorial2():
     
 fact=1
 for i in range(1,n+1):
     fact=fact*i
 return fact