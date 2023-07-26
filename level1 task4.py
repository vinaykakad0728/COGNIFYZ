print("Please select the operation to perfrom on the number")
print("a.add")
print("b.subtract")
print("c.multiply")
print("d.div")
print("e.module")

choice=input("please enter the choice (a/b/c/d/e) ")

num_1=int(input("enter first number to perfrom the operation"))
num_2=int(input("enter second number to perfrom the operation"))

if choice=='a':
    print("The addition of two number is:",num_1+num_2)
elif choice=='b':
    print("The subtration of two number is:",num_1-num_2)
elif choice=='c':
    print("The multiplication of two number is:",num_1*num_2)
elif choice=='d':
    print("The division of two number is:",num_1/num_2)
elif choice=='e':
    print("The module of two number is:",num_1%num_2)
else:
    print("The choose the valid option")
    