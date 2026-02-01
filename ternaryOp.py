age=float(input("Enter your age: "))
print("eligible to vote" if age>=18 else "you are not born yet"if age<1 else "you are not eligible to vote")
a=5
b=3
max_num=a if a>b else b
min_num=a if a<b else b
print(max_num,min_num)