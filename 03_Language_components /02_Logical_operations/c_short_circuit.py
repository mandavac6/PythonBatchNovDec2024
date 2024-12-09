"""
Purpose: short-circuit logic

"""

expr3 = 0 and 1 
print("expr3=", expr3)

expr4 = 3 and 9  
print("expr4=", expr4)

expr4 = 3 and 9 and 13 
print("expr4=", expr4)

expr4 = 3 and 13 and 9  
print("expr4=", expr4) 

 # If it has non-zeros, results last element


expr5 = 0 or 1  
print("expr5=", expr5)

expr6 = 3 or 9 
print("expr6=", expr6)

expr6 = 3 or 9 or 13  
print("expr6=", expr6)

expr6 = 13 or 9 or 3  
print("expr6=", expr6)  

expr6 = 0 or 0 or 9 or 13
print("expr6=", expr6)  
int()

# or is resulting first element(non-zero value)