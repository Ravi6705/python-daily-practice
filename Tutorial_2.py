#This is a Python Program to find the sum of elements in a list recursively.
#Method 1 
numbers=int(input("Enter the numbers of elements in list : "))
List_numbers = []
for i in range(numbers):
    x=int(input(f"Enter the {i+1} element : "))
    List_numbers.append(x)
print(f"your list is {List_numbers}")
# this above first of the block of the code will give the advantage to take numbers list forme the users 
# because input method only gives the string as result and we cant convers the whole list into int so we have take this code 
# for sun we just have to make another code
sum=0
for r in range(numbers):
    sum=sum+List_numbers[r]

print(f"sum of the list mumner is : {sum}")

#Method 2 
"in method 2 we are just changing the upar which how to get the list input from the input in which we are using split() method which give us the output of list in string and than we are using for loop to convers that string list into intgers "
## this method yo can see in the neso acdemy lecture name input a list using split() method 

#Method 3 
"in this method we are using List comprehension which you can see in the lecture name list comprehension in neso acdemy "


