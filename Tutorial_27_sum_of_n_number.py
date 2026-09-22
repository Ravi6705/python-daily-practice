#Python Program to Find Sum of First N Natural Numbers
def sum_Natural():
 n=int(input("Enter the last number : "))
 temp=n
 sum=0
 while temp>0:
    sum=sum+temp
    temp=temp-1

 print(f"sum of the {n} natural number is {sum}")
 print("Do you want to Try again ")
 print("1.Yes".upper())
 print("2.No".upper())
 AGAIN=input("Enter you are choise : ").upper()

 if AGAIN=="1" or AGAIN== "YES":
   sum_Natural()
 elif AGAIN=="2" or AGAIN=="NO":
   print("thank  you for using ")
 else:
   print("Enter valid choise")


sum_Natural()