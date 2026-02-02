print("Hello welcome")
print("Enter principle, rate and time")
principle=0.0
rate=0.0
time=0.0
while principle<=0:
    principle = float(input("enter principle: "))
    if principle<=0:
        print("enter valid principle")

while rate<=0:
    rate = float(input("enter rate: "))
    if rate<=0:
        print("enter valid rate")

while time<=0:
    time = float(input("enter time in years: "))
    if time<=0:
        print("enter valid time")

amount=principle* pow((1+(rate/100)),time)
print(f"Your final amount is ${amount:.2f} for Principle ${principle} and rate {rate} and time {time}")


