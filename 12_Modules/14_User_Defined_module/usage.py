import  sys

sys.dont_write_bytecode = False


# sys.dont_write_bytecode = True if it is true it donot create bytecode by default it is false 

import os

print(os.listdir())


import myscript

print(dir(myscript))


print(f""" 
    {myscript.Greetings =}

    {myscript.__name__ =}
    {myscript.__doc__ =}
    {myscript.hello_world =}
    {myscript.hello_world.__doc__ =}

""")

print(callable(myscript.Greetings))  
print(callable(myscript.hello_world))
myscript.hello_world()