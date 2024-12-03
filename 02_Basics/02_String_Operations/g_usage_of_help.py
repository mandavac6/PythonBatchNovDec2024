"""
Purpose: Demonstration of usage of help() on python objects
"""
dozen =12
dozen = 12.3

dozen = None
dozen = True

print(f"{type(dozen) =}")
print(f"{id(dozen)  =}")
print(f"{dozen      =}")

print(f"{dir(dozen) =}")

help(dozen)

# for strings the help usage differs if we give the help of the variable name it gives nothing then we have to do help(str)
mountain = "Himalayas"
print(f"{type(mountain) =}")
print(f"{id(mountain)   =}")
print(f"{mountain       =}")

print(f"{dir(mountain) =}")

help(mountain)
help(str)