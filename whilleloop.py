name = input("Enter your name: ")
while name=="":
    name = input("Please Enter your name: ")

print(f"Your name is {name}")

age=int(input("Enter your age: "))
while not age>0:
    age=int(input("Please Enter your + age: "))

print(f"Your age is {age}")

food=input("Enter your food(press x to exit): ")
while food!="x":
    print(f"Your food is {food}")
    food=input("Please Enter another your food: ")
    print(f"Your food is {food}")

print("bye")


