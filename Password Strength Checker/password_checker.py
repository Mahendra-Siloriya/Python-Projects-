"""
Challenge: Password Strength Checker & Suggestion Tool

Build a Python script that checks the strength of a password based on:
1. Length (at least 8 characters)
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one digit
5. At least one special character (e.g., @, #, $, etc.)

Your program should:
- Ask the user to input a password.
- Tell them what's missing if it's weak.
- If the password is strong, confirm it.
- Suggest a strong random password if the input is weak.

Bonus:
- Hide password input using `getpass` (no echo on screen).
"""
import random
import string
import getpass

def password_cheker(password: str) -> list[str]:

    issue = []
    if len(password) < 8 :
        issue.append('Password must be 8 char...')
    if not any(c.isupper() for c in password):
        issue.append('Password must be atleast one upper case.. ')
    if not any(c.islower() for c in password):
        issue.append('Password must be atleast one lower case.. ')
    if not any(c.isdigit() for c in password):
        issue.append('Password must be atleast one digit  ')
    if not any(c in string.punctuation for c in password):
        issue.append('Password must be atleast one special charch..')

    return issue

def generate_password(number : int = 12 ) -> str:

    strong_pass = string.ascii_letters + string.digits  + string.punctuation        
    return "".join(random.choice(strong_pass) for _ in range(number))

user_pass = getpass.getpass("enter you pass ")
issues = password_cheker(user_pass)

if not issues:
    print("password storng go on ")

else :
    print('you got weak pass')
    for issue in issues:
        print(f"- {issue}")

suggestion = generate_password()
print("suggesting storng pass ")
print(suggestion)    