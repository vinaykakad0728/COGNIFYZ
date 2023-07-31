import re
def password_checker(password):
    not_strong="password is not strong"
    strong=("password is strong")

    if len(password)<8:
       print(not_strong)
    if not re.search(r'\d',password):
        print(not_strong)
    if not re.search(r'[0-9]',password):
        print(not_strong)
    if not re.search(r'[A-Z]',password):
        print(not_strong)
    if not re.search(r'[a-z]',password):
        print(not_strong)
    if not re.search(r'[!@#$%^&*()]',password):
        print(not_strong)

password=input("Enter your password")
print(password_checker(password))