#Level1 task 5

def palindrome_checker(str):
    if str==str[::-1]:
        print(f"string '{str}' is a Palindrome")
    else:
        print(f"string '{str}' is not a palindrome")


str1="madam"
str2="racecar"
print(palindrome_checker(str1))
print(palindrome_checker(str2))


str=input("Enter a string to check it is palindrome or not")
print(palindrome_checker(str))

