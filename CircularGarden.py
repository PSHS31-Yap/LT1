#=======================================================================================================================
#       Programmer  : Brentt Ethann R. Yap
#       Date        : 9/19/26
#       Activity    : LT1 PART II
#       Description : This activity allows for the manipulation of the measurements and formulas of a circular garden using the radius of the circular garden
#=======================================================================================================================

import math

# Input Stage
radius_of_garden = float(input("Enter the radius of the circular garden in meters : ")) # Asks for the input to manipulate formulas of a circle


# Process Stage
area_of_garden = math.pi* math.pow(radius_of_garden,2) # Calculates the area of a circle using math.pow
circumference_of_garden = 2*math.pi*radius_of_garden # Calculates the circumference of a circle using math.pi
square_root_of_area = math.sqrt(area_of_garden) # Calculates the square root of the area using math.sqrt
rounded_down_area = math.floor(area_of_garden) # Calculates the rounded down area of the solved area
rounded_up_area = math.ceil(area_of_garden) # Calculates the rounded up area of the solved area

# Output Stage
print(f"""
The area of the circular garden with a radius of {radius_of_garden} meters is:  {area_of_garden:.2f} square meters. """) # Shows the area
print(f"""
The circumference of the circular garden with a radius of {radius_of_garden} meters is:  {circumference_of_garden:.2f} meters.""") #Shows the circumference
print(f"""
The square root of the area of the circular garden with a radius of {radius_of_garden} is:  {square_root_of_area:.2f} square meters. """) # Shows the square root of the Area
print(f"""
The area rounded down with a radius of {radius_of_garden} meters is:  {rounded_down_area} square meters.""") #Shows the rounded down area of a circle
print(f"""
The area rounded up with a radius of {radius_of_garden} meters is:  {rounded_up_area} square meters.""") # Shows the rounded up area of a circle

