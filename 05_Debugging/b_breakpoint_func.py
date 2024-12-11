"""
Purpose: Breakpoint()

        - builtin function, introducted in python 3.6
        - same as import pdb; pdb.set_trace()
"""


num1 =int(input("enter num1     : "))
num2 =int(input("enter num2     : "))


# import pdb
# pdb.set_trace()

# import pdb; pdb.set_trace()
breakpoint()

result =  num1 * num2 # num1 + num2
print(f"Multiplication   :{result}")

# enter num1     : 40
# enter num2     : 10
# > /workspaces/PythonBatchNovDec2024/05_Debugging/b_breakpoint_func.py(19)<module>()
# -> result =  num1 * num2 # num1 + num2
# (Pdb) ll
#   1     """
#   2     Purpose: Breakpoint()
#   3  
#   4             - builtin function, introducted in python 3.6
#   5             - same as import pdb; pdb.set_trace()
#   6     """
#   7  
#   8  
#   9     num1 =int(input("enter num1     : "))
#  10     num2 =int(input("enter num2     : "))
#  11  
#  12  
#  13     # import pdb
#  14     # pdb.set_trace()
#  15  
#  16     # import pdb; pdb.set_trace()
#  17     breakpoint()
#  18  
#  19  -> result =  num1 * num2 # num1 + num2
#  20     print(f"Multiplication   :{result}")
# (Pdb) next
# > /workspaces/PythonBatchNovDec2024/05_Debugging/b_breakpoint_func.py(20)<module>()
# -> print(f"Multiplication   :{result}")
# (Pdb) next
# Multiplication   :400