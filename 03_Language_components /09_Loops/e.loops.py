"""
Purpose: Loops
    break     - breaks the complete loop
    continue  - skip the current loop
    pass      - will do nothing. it is like a todo
    sys.exit  - will exit the script execution

"""
for i in "Python":
    if i in 'aeiou':
        break
    print(i, end=", ")


print("\n importance of continue")
# print odd numbers from 1 to 100 
for i in range(100):
    if i % 2 == 0 :
        continue 
    print(i, end=", ")
print("\n pass(acts a place holder )")
for i in range(100):
    if i % 2 == 0 :
        pass 
    print(i, end=", ")