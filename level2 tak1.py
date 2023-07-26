import random
n=random.randint(1,100)
count=0
while count<10:
    gruss=int(input("enter any number"))
    if gruss == n:
        print("congrats!you gruss the right number")
        break
        

    elif gruss<n:
        print("To Low")
        
    else:
        print("To High")

    
    count += 1
    
    if count>10:
        print(f"the number is {n}")
        print("try again")