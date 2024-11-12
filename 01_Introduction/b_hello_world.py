#!/usr/bin/python3
"""
 Purpose: Basic PEP-8 guidelines and
       shebang line

    PEP - Python Enhancement Prosopal (https://peps.python.org/pep-0008/)
    PEP 8 - coding style guide

    
"""

print("Hello world!")
# print "hello world"
#   print "hello world"
#     ^^^^^^^^^^^^^^^^^^^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print(True)
print(True, 123, None)


def wishes(name):
    wish = "How are you {0}?".format(name)
    print(wish)

wishes("Naveen")