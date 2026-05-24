name, age = input("What is your name and age? ").split(",")

print(f"Hello {name}, you are {age} years old.")

if int(age) >= 10 and (name[0] == "a" or name[0] == "A"):
    print("You are eligible to watch coco movie.")
else:
    print("Sorry, you cannot watch coco movie.")