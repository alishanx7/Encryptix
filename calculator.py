print("---------CALCULATOR---------")

num1 = float(input("enter first number:"))
num2 = float(input("enter the second number"))


print("press 1 for addition \npress 2 for subtraction \npress 3 for multiplication \npress 4 for division") 

choice = int(input("enter your choice from 1-4\n"))

if choice == 1:
    print (num1 + num2)

elif choice == 2:
    print (num1 - num2)

elif choice == 3:
    print (num1 * num2)

elif choice == 4:
    print (num1 / num2)

else:

    print("invalid input")