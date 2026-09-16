# Python Program to Convert Centimeters to Feet and Inches
def cm_to_feet_inches():
    cm_value = float(input("Enter the value in centimeters: "))
    feet_value = cm_value / 30.48
    inches_value = cm_value/2.54
    print(f"{cm_value} cm is equal to {feet_value:.3f}feet")
    print(f"{cm_value}cm is equal to {inches_value:.3f}inch")
    print("Do you want to go through another conversation")
    print("1.Yes")
    print("2.No")
    again = int(input("choose 1 or 2 : "))
    if again == 1 :
        cm_to_feet_inches()
    elif again==2:
        print("Thank you for using this")
    else:
        print("choose valid choise")


cm_to_feet_inches()

