"""
Purpose: Importing & using python script
"""
import Package3

print(dir(Package3))


print(Package3.__doc__)
print(Package3.calculator.__doc__)
print(Package3.operations.__doc__)
print()

print(Package3.calculator.addition.__doc__)
print()

from Package3 import calculator
from Package3.calculator import division

print(dir(calculator))

# print(calculator.__builtins__)

print(f"{calculator.addition(10, 20) =}")
print()

print(f"{calculator.__doc__          =}")
print(f"{calculator.addition.__doc__ =}")
print(f"{division.__doc__            =}")


help(calculator)