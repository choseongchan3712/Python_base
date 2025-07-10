# 상수
PI = 3.14

def calculate_area(r):
    return PI * r * r

radius = 4
print(f"반지름이 {radius}면, 넓이는 {calculate_area(radius): .2f}")
radius = 6
print(f"반지름이 {radius}면, 넓이는 {calculate_area(radius): .2f}")
radius = 7
print(f"반지름이 {radius}면, 넓이는 {calculate_area(radius): .2f}")