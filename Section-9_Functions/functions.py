area = 0 # global variable

def calculate_square_area(side: int = 1) -> int:
    global area
    area = side * side
    print(f"The area is {area}")
    return area

print("")
calculate_square_area(4)
print(f"The area of the square is {area}")




