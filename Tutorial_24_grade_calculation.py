def grade_calculation():
 
  total=int(input("Enter the total number of the subject : "))
  total_obtained_marks=[]
  total_out_of_marks=[]
  for i in range(1,total+1):
    obtained=int(input(f"Enter the {i} subject obtained marks : "))
    total_obtained_marks.append(obtained)
  for j in range(1,total+1):
    total_out=int(input(f"Enter the {j} subjects out of marks :"))
    total_out_of_marks.append(total_out)
  sum_of_obtained_marks=sum(total_obtained_marks)
  sum_of_total_marks=sum(total_out_of_marks)

  percentage=(sum_of_obtained_marks/sum_of_total_marks)*100
  if percentage>=90:
    print("You are grade is A")
  elif percentage>=80 and percentage<90:
    print("You are grade is B")
  elif percentage>=70 and percentage<80:
    print("You are grade is C")
  elif percentage>=60 and percentage<70:
    print("You are grade is D")
  else:
    print("You are grade is F")
    print("D o it better next Time")

  print("Do you want to Try again")
  print("1.Yes")
  print("2.No")
  again=input("Enter your choise : ").upper()
  if again== "1" or again== "YES":
    grade_calculation()
  else:
   print("thank you for using this return again ")
grade_calculation()