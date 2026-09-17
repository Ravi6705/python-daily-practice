def date_cheacking():
 print("Enter the date in the formate DD/MM/YYYY")
 date=input("Enter the Date : ")
 date_list=date.split("/")
 day=int(date_list[0])
 mm=int(date_list[1])
 year=int(date_list[2])
 if mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12:
    days=31
 elif mm==4 or mm==6 or mm==9 or mm==11:
    days=30
 else:
    if year%4==0 or year%400==0:
        days=29
    else:
        days=28

 if mm>12 or day<1 or day>days:
    print("Date is invalid")
 else :
    day=day+1
    if day>days:
        day=1
        mm=mm+1
        if mm>12:
            mm=1
            year=year+1

    print(f"the next date is {day}/{mm}/{year}")
 print("Do you want to try again")
 print("1.Yes")
 print("2.No")
 again=int(input("Enter your choise : "))
 if again==1:
    date_cheacking()
 elif again==2:
    print("Thank you for using this ")
 else:
    print("enter vailid choise")

date_cheacking()


# we can also use here list method
    

