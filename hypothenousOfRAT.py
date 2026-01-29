import math
base = float(input("enter the base: "))
height = float(input("enter the height: "))
hypotenuse = math.sqrt(pow(base,2)+pow(height,2))
print(f"Hypotenous is {round(hypotenuse,2)}")