# Write a script that takes two numbers as input and prints whether 
# the first number is greater than, less than, or equal to the second 
# number
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


if num1 > num2:
    print("The first number is greater than the second")
elif num1 < num2:
    print("The first number is less than the second")
else:
    print("Both numbers are equal")
