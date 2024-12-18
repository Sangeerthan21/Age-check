age = int(input("Enter your age:  "))

if age >= 10:
    if age <= 20:
        print("You are allowed")
    else:
        print("You are not allowed because you are older than 20 years")
else:
    print("You are not allowed because you are younger than 10 years")