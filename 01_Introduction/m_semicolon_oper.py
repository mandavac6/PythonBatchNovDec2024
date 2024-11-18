"""
Purpose : Multiple statements in sameline 
    , logic seperator
    ; statement completion seperator 
"""
print("hello" "world")
print("hello", "world")

print("hello", 3344)
# print("hello" 3344)
# SyntaxError: invalid syntax. Perhaps you forgot a comma?

print("hello", 3344, 765, 213 + 34)

# meathod 1
num1 = 23
num2 = 34
sum_of_num = num1 + num2
print("sum :", sum_of_num)

# meathod 2 using operator

num1 = 23; num2 = 34; sum_of_num = num1 + num2; print("sum :", sum_of_num)