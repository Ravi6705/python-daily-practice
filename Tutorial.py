## Write a Python Program to check whether a given number is even or odd
num=int(input("Enter the number : "))
if num%2==0:
    print( "Given number is even number")
else:
    print( "Given number is odd number")
    
# Method 2 using %s method 
num=int(input("Enter the number : "))
if num%2==0:
    print( "%s is even number"%(num))
else:
    print( "%s is odd number"%(num))

# Method 3 str>fromating() 
# using .format() method you can any object in the string like we are add there the integer in the string same %s method works
num=int(input("Enter the number : "))
if num%2==0:
    print( "{} is even number".format(num))
else:
    print( "{} is odd number".format(num))

# method 4
# we can also provide the key points or name in the curly braces to improve the readebility
num=int(input("Enter the number : "))
if num%2==0:
    print( "{number} is even number".format(number=num))
else:
    print( "{number} is odd number".format(number=num))

#method 5 using f string 
num=int(input("Enter the number : "))
if num%2==0:
    print( f"{num} is even number")
else:
    print( f"{num} is odd number")


# Method 6 using bitwise and operator 
num=int(input("Enter the number : "))
if num & 1:
    print(num, "is an odd number.")
else:
    print(num, "is an even number.")