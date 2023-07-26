#LEVEL 1 TASK 2

print("Pleaase select the option are as follows")
print("a.celsius")
print("b.fahrenheit")

choice=input("please select the option(a/b)")

T=float(input("enter the temperature in celsius or fahrenheit"))

if choice=='a':
    f=T*(9/5)+32
    print(f"the temp {T} is in celsius is converted in fahrenheit:",f)
elif choice=='b':
    c=(T-32)*5/9
    print(f"the temp {T} is in fahrenheit is converted in celsius:",c)
else:
    print("Please select the currect option")