def greatest_of_two(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
          return "Both numbers are equal"
    
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

result = greatest_of_two(number1, number2)
print("The greatest of the two numbers is:", result)