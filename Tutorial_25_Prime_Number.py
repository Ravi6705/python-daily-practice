#this is the python program code to print the prime number in given range
# this is little difficult one for me as beginer we can also do this with recursion but it is other thing 
# we are not using recurstion to start again without running becuse at earlyer code if you se it i don't have the idea about the recursion 
# now after watching the lecture i know what is recursion so we wiil  rectureion take recursion program as other tutorial 
start=int(input("Enter the starting of the range : "))
end=int(input("Enter the Ending  ot the range : "))
prime_number=[]
for i in range(start,end+1):
    if i<2:
        continue
    for j in range(2,i):
        if i%j==0:
            break
    else:
        prime_number.append(i)
print(prime_number)

      

    

