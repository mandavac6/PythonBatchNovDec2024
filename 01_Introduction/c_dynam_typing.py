"""
Purpose: Python is a dynamic Typed Language.
    Progamming Languages
        - Classficiations
            Static-Typed Languages
                - first declare the variables, & then use them
                    int a, float b  # Declaration
                    a = 10          # initialization

            Dynamic Typed Languages (Python, perl, ruby)
                 - create when you need. No declaration needed
                    num = 123

data types in python
    int, float, complex, bool, None
"""

num = 432

print(num)
type(num)

print(type(num))

print('num =', num)
print("num =", num)

print("num =", num, "type(num) =", type(num))   # type function declares the type of integer

# Python is a dynamic-typed language
num1 = 332
print("num1 =", num1, "type(num1) =", type(num1))   # int

num1 = 332.
print("num1 =", num1, "type(num1) =", type(num1))   # Float

num1 = 332.0
print("num1 =", num1, "type(num1) =", type(num1))   # Float

num1 = 332.0,
print("num1 =", num1, "type(num1) =", type(num1))   # tuple
print()


num1 = .332
print("num1 =", num1, "type(num1) =", type(num1))   # Float

num1 = .332j
print("num1 =", num1, "type(num1) =", type(num1))   # complex

num1 = 13 + .332j
print("num1 =", num1, "type(num1) =", type(num1))   # complex
print()

num1 = "13 + .332j"
print("num1 =", num1, "type(num1) =", type(num1))   # complex

# NOTE: Strings need to be declared in quotes

num1 = "3"
print("num1 =", num1, "type(num1) =", type(num1))   # string

num1 = "three"
print("num1 =", num1, "type(num1) =", type(num1))   # string
print()

# NOTE: Boolean value should be typed in case-sensitive  
num1 = True
print("num1 =", num1, "type(num1) =", type(num1))   # boolean

num1 = False
print("num1 =", num1, "type(num1) =", type(num1))   # boolean

# num1 = true
# print("num1 =", num1, "type(num1) =", type(num1))   # boolean
#  num1 = true
# NameError: name 'true' is not defined. Did you mean: 'True'?

num1 = "true"
print("num1 =", num1, "type(num1) =", type(num1))   # string
print()

num1 = None
print("num1 =", num1, "type(num1) =", type(num1))   #None

# num1 = none
# print("num1 =", num1, "type(num1) =", type(num1))   #None
# num1 = none
# NameError: name 'none' is not defined. Did you mean: 'None'?

num1 = "None"
print("num1 =", num1, "type(num1) =", type(num1))   # string
