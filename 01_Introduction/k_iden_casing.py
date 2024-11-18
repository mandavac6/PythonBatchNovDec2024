#!/usr/bin/python3
"""
Purpose: Identifier Casing
    PEP (python Enhancement Proposal) 8 - coding style guide
        - class names should be in CamelCase
        - identifier names should be in snake( or Underscore) case .

    Article: https://ieeexplore.ieee.org/document/5521745?tp=&arnumber=5521745

"""

# Python is case-sensitive language
animal = "Cat"
print(animal)

# print(Animal)
# NameError: name 'Animal' is not defined. Did you mean: 'animal'?

ANIMAL = "PIG"
print(ANIMAL)


Animal = "Camel"
print(Animal)


# ------------------------
# variable casing
# 1.snake casing or underscore casing

student = "arjun"
employee_salary = 322344.23
cost_of_mango = 14
selling_price_of_apples = 44

output_of_thermal_sensor = 35
no_of_current_processes = 7



# 2. Camel casing
Student = "Arjun"
EmployeeSalary = 322344.23
CostOfMango = 14
SellingPriceOfApples = 44

OutputOfThermalSensor = 35
NoOfCurrentProcesses = 7