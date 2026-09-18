#This is a Python Program to read a number n and compute n+nn+nnn.
print("This is a Python Program to read a number n and compute n+nn+nnn.")

def n_nn_nnn():
 n=int(input("enter the number : "))
 temp=str(n)
 nn=int(temp*2)
 nnn=int(temp*3)
 Ans=n+nn+nnn
 print(f"the wanted computed answer : {Ans}")

 print("Do you want to Try again")
 print("1.Yes")
 print("2.No")
 again=input("Enter your choise : ").upper()
 if again== "1" or again== "YES":
  n_nn_nnn()
 else:
  print("thank you for using this return again ")



 

 



n_nn_nnn()


 