#Python Program to Find the Prime Factors of a Number
n=int(input("Enter the number : "))
for i in range(2,n):
    if n%i==0:
        prime=True
        for j in range(2,i):
            if i%j==0:
                prime=False
                break
        
        if prime:
            print("prime factors are : " )
            print(i,end=" ")

        

