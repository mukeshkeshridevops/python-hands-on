name = input("Enter a name: ")
number_of_characters = len(name)

if number_of_characters > 0:
    print(f"The name {name} has {number_of_characters} characters.")
else:
    print("You did not enter a name.")

temp_var = ""
for character in name:
    if character not in temp_var:
        count = name.count(character)
        print(f"The character '{character}' appears {count} times in the name {name}.")
        temp_var += character