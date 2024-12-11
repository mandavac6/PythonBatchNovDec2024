"""
Purpose: Debugging
"""


num1 =int(input("enter num1     : "))
num2 =int(input("enter num2     : "))


# import pdb
# pdb.set_trace()
import pdb; pdb.set_trace()

result =  num1 * num2 # num1 + num2
print(f"Multiplication   :{result}")



# @mandavac6 ➜ /workspaces/PythonBatchNovDec2024/05_Debugging (class13) $ python a_using_pdb.py 
# enter num1     : 25
# enter num2     : 5
# > /workspaces/PythonBatchNovDec2024/05_Debugging/a_using_pdb.py(11)<module>()
# -> result =  num1 + num2
# (Pdb) help

# Documented commands (type help <topic>):
# ========================================
# EOF    c          d        h         list      q        rv       undisplay
# a      cl         debug    help      ll        quit     s        unt      
# alias  clear      disable  ignore    longlist  r        source   until    
# args   commands   display  interact  n         restart  step     up       
# b      condition  down     j         next      return   tbreak   w        
# break  cont       enable   jump      p         retval   u        whatis   
# bt     continue   exit     l         pp        run      unalias  where    

# Miscellaneous help topics:
# ==========================
# exec  pdb

# (Pdb) l
#   6     num1 =int(input("enter num1     : "))
#   7     num2 =int(input("enter num2     : "))
#   8     import pdb
#   9     pdb.set_trace()
#  10  
#  11  -> result =  num1 + num2
#  12     print(f"Multiplication   :{result}")
# [EOF]
# (Pdb) ll
#   1     """
#   2     Purpose: Debugging
#   3     """
#   4  
#   5  
#   6     num1 =int(input("enter num1     : "))
#   7     num2 =int(input("enter num2     : "))
#   8     import pdb
#   9     pdb.set_trace()
#  10  
#  11  -> result =  num1 + num2
#  12     print(f"Multiplication   :{result}")
# (Pdb) next
# > /workspaces/PythonBatchNovDec2024/05_Debugging/a_using_pdb.py(12)<module>()
# -> print(f"Multiplication   :{result}")
# (Pdb) ll
#   1     """
#   2     Purpose: Debugging
#   3     """
#   4  
#   5  
#   6     num1 =int(input("enter num1     : "))
#   7     num2 =int(input("enter num2     : "))
#   8     import pdb
#   9     pdb.set_trace()
#  10  
#  11     result =  num1 + num2
#  12  -> print(f"Multiplication   :{result}")
# (Pdb) num1
# 25
# (Pdb) num2
# 5
# (Pdb) 25*5
# 125
# (Pdb) next
# Multiplication   :30
# --Return--
# > /workspaces/PythonBatchNovDec2024/05_Debugging/a_using_pdb.py(12)<module>()->None
# -> print(f"Multiplication   :{result}")
# (Pdb) q
# Traceback (most recent call last):
#   File "/workspaces/PythonBatchNovDec2024/05_Debugging/a_using_pdb.py", line 12, in <module>
#     import pdb; pdb.set_trace()
#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/usr/local/python/3.12.1/lib/python3.12/bdb.py", line 94, in trace_dispatch
#     return self.dispatch_return(frame, arg)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/usr/local/python/3.12.1/lib/python3.12/bdb.py", line 156, in dispatch_return
#     if self.quitting: raise BdbQuit
#                       ^^^^^^^^^^^^^
# bdb.BdbQuit