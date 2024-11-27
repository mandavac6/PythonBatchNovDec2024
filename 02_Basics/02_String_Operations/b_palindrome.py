"""
Purpose: Demonstration of Palindrome check

Algorithms:
-----------
Step 1: Take the string in run-time and store in a variable
Step 2: create a reverse string , from the given string, using string reversal
Step 3: compare both with a condition and decide

"""

test_string = input("Enter any string:")
print("test_string    :", test_string)

# reverse string
reverse_string = test_string[::-1]
print("reverse_string :", reverse_string)
print("test_string == reverse_string:", test_string == reverse_string)

if test_string == reverse_string:
    print(test_string, "is palindrome")
else:
    print(test_string, "is NOT a palindrome")    
