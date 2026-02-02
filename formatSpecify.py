price1= 3.14159
price2=-2345.543
price3=23.3253253
print(f"Price 1 is {price1}")
print(f"Price 2 is {price2}")
print(f"Price 3 is {price3}")
#format specify
print(f"price 1 ${price1:.0f}")
print(f"price 2 ${price2:.2f}")
print(f"price 3 ${price3:.5f}")
print(f"price 1 ${price1:010}")
print(f"price 2 ${price2:<10}")
print(f"price 3 ${price3:>10}")
print(f"price 1 ${price1:^10}")
print(f"price 2 ${price2: }")
print(f"price 3 ${price3:,}")
