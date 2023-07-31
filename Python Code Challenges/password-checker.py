# Create a program that asks the user to enter a new password and check:
# 1) the submitted password should contain at least one number,
# 2) at least one uppercase letter,
# 3) at least 5 characters.
# 4) If the conditions are generated, print out "Password is fine"; otherwise, keep prompting the user for a password.
# 5) give the exact reason why the password is not passed
import string

while True:
    password = input('Enter your password here for checking: ')
    passed = True
    if not any(l.isdigit() for l in password):
        print('Password should contain at least one number. Please try again.')
        passed = False
    if not any(l in string.ascii_uppercase for l in password):
        print('Password should contain at least one uppercase letter. Please try again.')
        passed = False
    if len(password) < 5:
        print('Password should contain at least 5 characters. Please try again.')
        passed = False

    if not passed:
        continue

    print('Password successfully passed!')
    break
