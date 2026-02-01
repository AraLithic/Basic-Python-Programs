temp = float(input("Enter temperature in Celsius: "))
is_raining=input("Do you want the raining? (Y/N): ")

if is_raining=="Y":
    print("Event off")
elif is_raining == "N":
    if temp>15 and temp<30:
        print("Event On")
    elif temp>30 or temp<15:
        print("Event Off")
    else:
        print("Event off")
else:
    print("Invalid")

is_sunny=input("Do you want the sunny? (Y/N): ")
if is_sunny=="Y":
    is_sunny=True
else:
    is_sunny=False

if not is_sunny:
    print("Bring raincoat")
else:
    print("Wear Bikini")






