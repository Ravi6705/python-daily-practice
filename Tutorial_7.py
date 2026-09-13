n=int(input("enter the starting number of list: "))
m=int(input("enter the ending number of the list: "))
main_list=list(range(n,m+1))
even_numbers=[]
odd_numbers=[]
for i in main_list:
    if i%2==0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print("main list is: ",main_list)
print("even numbers list : ",even_numbers)
print("odd numbers list : ",odd_numbers)
