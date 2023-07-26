import re
def checking(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+",email):
        return True
    return False

email="vinay@email.com"
if checking(email):
    print("valid email address")
else:
    print("invalid email address")