#write a program to print the multiplication table pattern as shown
# 1
# 2 4
# 3 6 9
# 4 8 12 16 

row=int(input("enter the number of rows: "))
for i in range(1,row+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print("")
    