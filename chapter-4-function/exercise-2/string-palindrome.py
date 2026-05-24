def is_palindrome(s):
    s = s.replace(" ", "").lower()
    if s == s[::-1]:
        return True

    return False

palindrome = is_palindrome(input("Enter a string: "))
if palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
