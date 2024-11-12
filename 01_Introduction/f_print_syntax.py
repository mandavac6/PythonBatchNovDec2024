
name = "Marvel"  # str

print(name)
print("name")   # prints name as string

# print(name1)
# NameError: name 'name1' is not defined. Did you mean: 'name'?

print("name1")  # prints name as string


print("name =", name)
print()

print("Name of kid is name")

# concate with the name string 
print("Name of kid is" + name)
print("Name of kid is " + name)
print()

print("Name of kid is", name)

#using different sep by default space is added 
print("Name of kid is", name, sep=" ")
print("Name of kid is", name, sep="-")
print("Name of kid is", name, sep="")
print()


print(1, 2, 3, 4, 5, 6)  # default sep=' '
print(1, 2, 3, 4, 5, 6, sep=" ")
print()

print(1, 2, 3, 4, 5, 6, sep="*")
print(1, 2, 3, 4, 5, 6, sep="+")
print(1, 2, 3, 4, 5, 6, sep="_")
print()

# NOTE: Python is dynamic typed language
name = 445
print("Name of kid is", name)

# print('Name of kid is'+ name)
# TypeError: can only concatenate str (not "int") to str

# NOTE: Python is a strictly typed language
print("13 + 32        =",  13 + 32)     # addition
print("'13' + '32'    =", "13" + "32")  # string concatenation
print()

# 13 + '32' # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# type converters - str(), int(), float()

print("1 + int('2') =", 1 + int("2"))
print("str(1) + '2' =", str(1) + "2")

print()
print("int('234')   =", int("234"))

# print("int('23.4')  =", int('23.4')) # ValueError: invalid literal for int() with base 10: '23.4'
# print("int('two')  =", int('two')) # ValueError: invalid literal for int() with base 10: 'two'


print("Name of kid is" + str(name))
print("Name of kid is" + " " + str(name))