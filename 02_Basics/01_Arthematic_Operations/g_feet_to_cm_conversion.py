"""
Purpose: Feet to centimetres conversion

    1 foot = 12 inches
    1 inch = 2.54 centimetres

Algorithm:
--------------
Step 1: Get feet values in runtime
Step 2: compute  from feet to cms
            feet to inches, then
            inches to centimeters conversion
Step 3: Display the results
"""

# declaring constants 
FEET_TO_INCHES = 12
INCHES_TO_CENTIMETERS = 2.54

# feet run time 
feet = float(input("enter feet to convert:"))

# feet to inches
inches_conv= feet * FEET_TO_INCHES
print("inches converted:", inches_conv)

# inches to cms
cms_conv = inches_conv * INCHES_TO_CENTIMETERS
print("cms converted:", cms_conv)