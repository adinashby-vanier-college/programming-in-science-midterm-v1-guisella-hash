import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    area = round(math.pi * radius**2, 2)
    return area 

print(area_of_circle(5))

    # return 0.0

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    result = ""

    for i in range(n):
        if n <= 3:
            result += ("The triangle height should be at least 4.") 

        for j in range(n):
            if i == j or i == n - 1 or j == 0:
                result += "*"
            else:
                result += " "
        result += "\n"

    return result.rstrip()



print(hollow_right_triangle(5))
print(hollow_right_triangle(4))
print(hollow_right_triangle(3))
print(hollow_right_triangle(1))
    # return ""

# Q3: Inverted Pyramid
def inverted_pyramid(n):
    result = ""

    for i in range(n):
        for j in range(n * 2 - i * 2 - 1):
            result += "*"
        for k in range(i):
            result += " "
        result += "\n"
    return result.rstrip()

print(inverted_pyramid(5))
# print(inverted_pyramid(3))
    # return ""

# ----------------------------------------------------------------
# print(area_of_circle(5))
# print()

# print(hollow_right_triangle(3))
# print()

# print(hollow_right_triangle(4))
# print()

# print(hollow_right_triangle(5))
# print()

# print(inverted_pyramid(3))
# print()

# print(inverted_pyramid(4))
# print()

# print(inverted_pyramid(5))
# print()
