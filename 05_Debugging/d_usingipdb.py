"""
Purpose: Debugging with ipdb

TASK - To display all even numbers between 0 & 100

To install ipdb,
    pip install -U ipdb --user

NOTE: TO make ipdb as the default, when using breakpoint(),
    export PYTHONBREAKPOINT='ipdb.set_trace'

"""


numbers = range(0, 100)

import ipdb; ipdb.set_trace()
# breakpoint()


for each_num in numbers:
    if each_num % 2 == 0:  # each_num % 2
        print(each_num, end=", ")

# > /workspaces/PythonBatchNovDec2024/05_Debugging/d_usingipdb.py(21)<module>()
#      20 
# ---> 21 for each_num in numbers:
#      22     if each_num % 2 == 0:  # each_num % 2

# ipdb> n
# > /workspaces/PythonBatchNovDec2024/05_Debugging/d_usingipdb.py(22)<module>()
#      21 for each_num in numbers:
# ---> 22     if each_num % 2 == 0:  # each_num % 2
#      23         print(each_num, end=", ")

# ipdb> n
# > /workspaces/PythonBatchNovDec2024/05_Debugging/d_usingipdb.py(23)<module>()
#      21 for each_num in numbers:
#      22     if each_num % 2 == 0:  # each_num % 2
# ---> 23         print(each_num, end=", ")

# ipdb> n
# 0, > /workspaces/PythonBatchNovDec2024/05_Debugging/d_usingipdb.py(21)<module>()
#      20 
# ---> 21 for each_num in numbers:
#      22     if each_num % 2 == 0:  # each_num % 2

# ipdb> n
# > /workspaces/PythonBatchNovDec2024/05_Debugging/d_usingipdb.py(22)<module>()
#      21 for each_num in numbers:
# ---> 22     if each_num % 2 == 0:  # each_num % 2
#      23         print(each_num, end=", ")

# ipdb> n
# > /workspaces/PythonBatchNovDec2024/05_Debugging/d_usingipdb.py(21)<module>()
#      20 
# ---> 21 for each_num in numbers:
#      22     if each_num % 2 == 0:  # each_num % 2

# ipdb> n
# > /workspaces/PythonBatchNovDec2024/05_Debugging/d_usingipdb.py(22)<module>()
#      21 for each_num in numbers:
# ---> 22     if each_num % 2 == 0:  # each_num % 2
#      23         print(each_num, end=", ")

# ipdb> n
# > /workspaces/PythonBatchNovDec2024/05_Debugging/d_usingipdb.py(23)<module>()
#      21 for each_num in numbers:
#      22     if each_num % 2 == 0:  # each_num % 2
# ---> 23         print(each_num, end=", ")

# ipdb> n
# 2, > /workspaces/PythonBatchNovDec2024/05_Debugging/d_usingipdb.py(21)<module>()
#      20 
# ---> 21 for each_num in numbers:
#      22     if each_num % 2 == 0:  # each_num % 2

# ipdb> each_num
# 2
# ipdb> type(each_num)
# <class 'int'>
# ipdb> each_num.bit_length
# <built-in method bit_length of int object at 0x617b884d67c8>
# ipdb> c


# Assignment: How to clear one specific breakpoint, in ipdb
 
#  when we are creating a break point it is assigning the order of breakpoint creation in a list 
# 
# we can delete the breakpoint by giving clear <num > 

# pdb> b
# ipdb> b 23
# Breakpoint 1 at /workspaces/PythonBatchNovDec2024/05_Debugging/d_usingipdb.py:23
# ipdb> b 22
# Breakpoint 2 at /workspaces/PythonBatchNovDec2024/05_Debugging/d_usingipdb.py:22
# ipdb> b
# Num Type         Disp Enb   Where
# 1   breakpoint   keep yes   at /workspaces/PythonBatchNovDec2024/05_Debugging/d_usingipdb.py:23
# 2   breakpoint   keep yes   at /workspaces/PythonBatchNovDec2024/05_Debugging/d_usingipdb.py:22
# ipdb> cl 2
# Deleted breakpoint 2 at /workspaces/PythonBatchNovDec2024/05_Debugging/d_usingipdb.py:22
# ipdb> b
# Num Type         Disp Enb   Where
# 1   breakpoint   keep yes   at /workspaces/PythonBatchNovDec2024/05_Debugging/d_usingipdb.py:23
# ipdb> cl 1
# Deleted breakpoint 1 at /workspaces/PythonBatchNovDec2024/05_Debugging/d_usingipdb.py:23
# ipdb> 
