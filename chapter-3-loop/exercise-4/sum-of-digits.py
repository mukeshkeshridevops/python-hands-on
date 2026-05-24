digits = input("Enter a number: ")
total = 0

for digit in digits:
    total += int(digit)

print(f"The sum of the digits in {digits} is: {total}")
