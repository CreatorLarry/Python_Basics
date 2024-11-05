# functions
# import datetime
# import math
# from array import array


# function for triangle area
def calc_area_triangle(b, h):
    area = 0.5 * (b * h)
    area = round(area, 2)
    print("Area of triangle is ", area, "cm^2")

# function for circle area
def calc_area_circle(radius):
    area = 22/7 * radius * radius # math.pi * radius**2
    area = round(area, 2)
    print("Area of circle is ", area, "cm^2")




# arrays
def add(*args):
    total = 0
    for num in args:
        total += num
        print("Total is ", total)



def sayhi(name, age=21): #the age parameter stays original if user doesn't enter their age
    print("Hello", name, ". I am ", age, "years old.")

sayhi("Mary")
sayhi("Larry", 30)
# using a function == calling to calculate area of triangle
calc_area_triangle(5, 10)
calc_area_triangle(70, 20)

# list of triangles I want to calculate area for
triangles = [[65, 70], [50, 50], [60, 50], [72, 77], [70, 99]]

for t in triangles:
    calc_area_triangle(t[0], t[1])


# using a function == calling to calculate area of circle
calc_area_circle(67.75456)
calc_area_circle(30.33333)

# using a function == calling today date
# print_today_date()


# using a function == calling arrays

# array