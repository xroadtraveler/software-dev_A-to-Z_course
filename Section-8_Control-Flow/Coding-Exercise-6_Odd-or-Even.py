#odd or even
number = 3
result = "unknown"

if int(number) % 2 == 0: # Had to add extra "=" to make it work.
    result = "even"
else:
    result = "odd"

print(f"{number} is {result}")