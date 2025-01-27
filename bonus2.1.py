password = input("Enter a password: ")  # Get the password from the user

correct_password = "pass123"  # Here is the correct password!

# Now check the password!

while password != correct_password:  # While the password you entered is  incorrect, keep asking for password!
    password = input("Enter a password again!: ")

print("Password was correct!")


