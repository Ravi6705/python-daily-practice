#This is a Python Program to print odd numbers within a given range
start_number=int(input("enter the starting number : "))
end_number=int(input('enter the ending number : '))
for i in range(start_number,end_number+1):
    if i%2!=0:
        print(i)


#method 2 
#This is a Python Program to print odd numbers within a given range
start_number=int(input("enter the starting number : "))
end_number=int(input('enter the ending number : '))
x=[]
for i in range(start_number,end_number+1):
    if i%2!=0:
        x.append(i)

print(x)