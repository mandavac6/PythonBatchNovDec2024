"""
Purpose: Getting Command-line arguments
"""
import sys

print("__file__", __file__) 
print("sys.argv", sys.argv[0])

"""

$ python b_commandline_args.py 
__file__ /workspaces/PythonBatchNovDec2024/12_Modules/02_Sys/b_commandline_args.py
sys.argv b_commandline_args.py

$ python ../02_Sys/b_commandline_args.py 
__file__ /workspaces/PythonBatchNovDec2024/12_Modules/02_Sys/../02_Sys/b_commandline_args.py
sys.argv ../02_Sys/b_commandline_args.py

$ cd ..
$ python 02_Sys/b_commandline_args.py 
__file__ /workspaces/PythonBatchNovDec2024/12_Modules/02_Sys/b_commandline_args.py
sys.argv 02_Sys/b_commandline_args.py

"""


print("__file__", __file__.replace("\\", "/"))
assert __file__ != sys.argv[0]

print()

print("Number of arguments:", len(sys.argv), "arguments")
print("Arguments List:", list(sys.argv))

'''
$ python b_commandline_args.py 5655 fibroo 898 ghoilkjho
__file__ /workspaces/PythonBatchNovDec2024/12_Modules/02_Sys/b_commandline_args.py
sys.argv b_commandline_args.py
__file__ /workspaces/PythonBatchNovDec2024/12_Modules/02_Sys/b_commandline_args.py

Number of arguments: 5 arguments
Arguments List: ['b_commandline_args.py', '5655', 'fibroo', '898', 'ghoilkjho']

'''