import os
import sys

print(os.getcwd())

print(os.listdir())


# paths it will check for imports
for each_path in sys.path:
    print(each_path)

# adding the path
sys.path.insert(0, "Package")



'''
added custom paths
    /package

current dir
/workspaces/PythonBatchNovDec2024/12_Modules/15_User_defined_Packages

Built in modules 
/usr/local/python/3.12.1/lib/python312.zip
/usr/local/python/3.12.1/lib/python3.12
/usr/local/python/3.12.1/lib/python3.12/lib-dynload

installed modules
/workspaces/PythonBatchNovDec2024/.venv/lib/python3.12/site-packages
'''

# importing a single script --- module
import module1


# importing entire folder of scripts -- package
import Package
print(Package)
print(dir(Package))


print(dir(Package.module1 ))

Package.module1.hello_world()
Package.module2.hello_world()