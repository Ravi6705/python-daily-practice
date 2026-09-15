# Write a Python program that takes a year as input and checks whether it is a leap year or not.
year = int(input("Enter a year : ")) 
if year%100==0:
    print("{} is century".format(year))
    if year%400==0:
        print("{} is a leap year".format(year))
    else:
        print("{} is not a leap year".format(year))
else:
    if year%4==0:
        print("{} is a leap year".format(year))
    else:
        print("{} is not a leap year".format(year))