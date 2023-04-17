# Name: Yian Ha
# SBUID: 115343173
##################### SCORE ######################
#######  Score:  9/10 - please use python functions and variables
#################################################
# Remove the ellipses (...) when writing your solutions.
# your output:
# (base) D:\CSE 101 Ass1\Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27>D:/anaconda/python.exe "d:/CSE 101 Ass1/Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27/Yian716/Homework_1.py"
# Sweater
# The area of the triangle is : 40.5 , its perimeter is : 34.44016144898765 --> wrong
# The area of the polygon is : 27.527638409423474
# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit): 
    celsius= (5/9) * (fahrenheit - 32)
    return celsius

def what_to_wear(celsius):
    if celsius <= -10:
        print("Puffy jacket")
    elif celsius <= 0:
        print("scarf")
    elif celsius <= 10:
        print("Sweater")
    elif celsius <= 20:
        print("Light jacket")
    else:
        print("T-shirt")
# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    return abs ((((x1*y2)+(x2*y3)+(x3*y1))-((x1*y3)+(x2*y1)+(x3*y2))/2))

def euclidean_distance(x1, y1, x2, y2):
    return ((((x1-x2)**2)+((y1-y2)**2))**0.5)

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    return ((((x1-x2)**2)+((y1-y2)**2))**0.5) + ((((x2-x3)**2)+((y2-y3)**2))**0.5) + ((((x3-x1)**2))**0.5) + ((((x3-x1)**2)+ ((y3-y1)**2))**0.5)


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 

import math
def deg2rad(deg):
    deg2rad = (deg * (math.pi/180))
    return deg2rad

def apothem(number_sides, length_side):
    apothem = (length_side/((2*math.tan(deg2rad(180/number_sides)))))
    return apothem

def polygon_area(number_sides, length_side):
    a = apothem(number_sides, length_side)
    polygon_area = (((number_sides)*(length_side)*(a))/2)
    return polygon_area


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

