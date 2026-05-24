def greatest_of_two_numbers(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Both numbers are equal"
    
def greatest_of_three(num1, num2, num3):
    greatest = greatest_of_two_numbers(num1, num2)
    return greatest_of_two_numbers(greatest, num3)

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
number3 = float(input("Enter third number: "))

result = greatest_of_three(number1, number2, number3)
print("The greatest of the three numbers is:", result)