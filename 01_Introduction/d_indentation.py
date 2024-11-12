"""
Purpose: Importance of indentataion
"""

print("hello world1!")

#  print("hello world2!")  
# IndentationError: unexpected indent
print("hello world3!")

# if 13 > 7:
# print('13 is greater than 7')
# IndentationError: expected an indented block after

# If Statement
if 13 > 7:
    print('13 is greater than 7')

# If-else Statement
if 12 > 34:
    print("greater")
else:
    print("It is lesser")

# If-elseif-else Statement
if 1 < 2:
    print("case 1")
elif 2 > 1:
    print("case 2")
else:
    print("case 3")

# Nested if Statement
if 1 < 2:
    if 2 < 3:
        if 3 < 4:
            if 4 < 5:
                print("LESS")
            else:
                print("!something")
        else:
            print("!something")
    else:
        print("!something")

# for loop printing numbers from 0-6
for i in range(7):
    print(i)

# while loop printing values from 0-15 increment by 3 each time 
i = 0
while i < 15:
    print(i)
    i += 3

i = 0
while i < 5:
    j = 0
    while j < 10:
        print(i, "+", j, "=", i + j)
        j += 1
    print()
    i += 1


# tabs vs white-space
# Prefer white-spaces for indentation 
# to standardize python implements tabs; four white-spaces(to made it more clear than single space)