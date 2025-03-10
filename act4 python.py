
def ageggs():
    age = int(input("Enter your age: "))
    if age <=12:
        print("You are",age, " and you are still a child")
    elif age <=19:
        print("You are", age, "and you are still a teen.")
    elif age <=64:
        print("You are ", age," and you are an adult.")
    elif age >=65:
        print("You are", age, " and you are already senior")

ageggs()

while True: 
    a = input("again? y/n: ")
    if a == "y":
        age()
    else:
        b = print("OKE BYE")
        break