# Loading a module 
import keyword

print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 
# 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', '
# in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
print ()

print(True)  # True
# print(true)
# NameError: name 'true' is not defined. Did you mean: 'True'?

my_value = "something"
print(my_value)  # Identifier


print(keyword.iskeyword("True"))        # True
print(keyword.iskeyword("true"))        # False
print(keyword.iskeyword("my_value"))    # False 


# ------------------------------------------------------
# Identifiers - User-defined variables
#   - Naming Convention
#      1. keywords should not be used as identifiers
#      2. first character: a-z, A-Z, _
#      3. remaining chars: a-z, A-Z, _, 0-9


# ---- Rule 1
# True = 123  # SyntaxError: cannot assign to True
# None = 'Nothing'  # SyntaxError: cannot assign to None

# PEP 8 - Dont create identifiers which are similar as Keywords


true = 123
none = "Nothing"


true_value = 123
none_result = "Nothing"


name = "Naveen"
name_of_student = "Naveen"
first_name = "Naveen"
student_1 = "Naveen"
class_02_a = "Python comment operations"



# PEP 8 recommends to use capitals for constants
PI = 3.1416
DOZEN = 12

# $name = "Naveen"
# name-of-student = "Naveen"
# name of student = "Naveen"
# 1st_name = "Naveen"  SyntaxError: invalid decimal literal


_2nd_student = "someone"    # _variable  -> Protected variable

_job = "software development"   # _variable  -> Protected variable
__role = "Product support"  # __variable -> Private variable
___salary = 1231231232312323233

# OOP -> name mangling
# variable   -> Public variable
# _variable  -> Protected variable
# __variable -> Private variable


# __variable__ ->  Built-in functions
# Ex: __file__, __name__, __doc__, __dict__, __init__
# these are called dunder meathods /magic meathods 

print("__name__ =", __name__)  # __main__
print("__file__ =", __file__) # prints the file path 


# print("__cat__ =", __cat__)
# NameError: name '__cat__' is not defined. Did you mean: '__name__'?