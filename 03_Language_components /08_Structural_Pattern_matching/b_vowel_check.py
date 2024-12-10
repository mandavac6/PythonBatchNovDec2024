"""
Purpose: to check wheter the char is vowel or not

"""

char = input("Enter a character: ")
if char.isalpha():  
    if char in 'aeiou':
        print(f"The character '{char}' is a vowel.")
    elif char in "AEIOU":
        print(f"The character '{char}' is a vowel.")
    else:
        print(f"The character '{char}' is a consonant.")
else:
    print("Invalid input! Please enter an alphabetic character.")
# Structural pattern
match char:
    case "a" | "e" | "i" | "o" | "u" | "A" | "E" | "I" | "O" | "U" :
        print(f"The character '{char}' is a vowel.")
    case _:
        print(f"The character '{char}' is a consonant.")