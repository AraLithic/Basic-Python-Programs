num=int(input("enter your number between 1 and 10: "))
while num>1 or num>10:
    print(f"{num} not valid ")
    num=int(input("enter your number between 1 and 10: "))

print(num)