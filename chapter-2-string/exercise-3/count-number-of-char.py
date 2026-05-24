user_name, char_to_count = input("Enter user name and character to count using comma separated: ").split(",")

print(f"User name length is : {len(user_name)}")
print(f"Number of {char_to_count} in user name is : {user_name.lower().count(char_to_count)}")