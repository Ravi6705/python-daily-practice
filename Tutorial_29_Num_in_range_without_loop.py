def num_in_range(a, n):

    if a > n:
        return
    else:
        print(a, end=" ")
        num_in_range(a + 1, n)


a = int(input("Enter the starting number : "))
n = int(input("Enter the ending number : "))

if a > n:
    print("Enter the valid range")
else:
    print("Numbers in given Range : ")
    num_in_range(a, n)