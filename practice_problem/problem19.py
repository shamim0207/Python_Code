# Practice Problem: Write a program to check if a user-entered string contains any numeric digits. Use a for loop to examine each character.

user_string=input("Enter your String: ")
find_digit=False

for ch in user_string:
    if(ch.isdigit()):
        find_digit=True
        break
print(f"The string '{user_string}' contains digits: {find_digit}")
    