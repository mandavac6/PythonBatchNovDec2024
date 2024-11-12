"""
Purpose: print() function syntax and usage
    Escapes Sequences
        - characters whose presence is felt, but they were not printed
        \t - tab space
        \n - new line
        \b - overwrites previous character

        r'' - raw string

"""
print("hello world python")
print("hello \tworld \tpython")
print("hello \tworld \npython")

print()

# To ignore the escape sequences
print("hello \tworld \\npython")
print(r"hello \tworld \npython")
print()

print("C:\my\newfolder") 
print(r"C:\my\newfolder")
print()


print("hello")  # default end='\n'
print("world")


print("hello", end="\n")
print("world", end="\n")


print("hello", end="___")
print("world")  # default end='\n'


print("hello", end="\t")
print("world")  # default end='\n'


print("hello", "python", 12132, end="\t")  # default sep= ' '
print("world")  # default end='\n'


print("hello", "python", 12132, end="\t", sep=";")
print("world")  # default end='\n'


print(1, 2, 3, 4, 5, sep=";", end="\t")
print("a", "b", "c", "d", sep="-")  # default end='\n'
print()


# \b - overwrites previous character
print("He\bi")
print("12\b34")
print("class\bpython")
print("\bpython")
print("python\b")
print("python\b1")
print()


# \r - overwrites complete existing line like a type-writter
print("He\ri")
print("12\r34")
print("class\rpython")
print("abcdef\r1234")
print("983686\rDOG")
print()

# Unicode characters  \uXXX

print("\u20B4")    # ₴
print("\u018a")    # Ɗ

print("\046")   # & --- Ascii format 

# hexadecimal number \x...

print("\x25")   # %
print("\xa3")   # £
print()


# Ascii Table(0-255) as per american standard (https://www.ascii-code.com/)
# Unicode Table (https://home.unicode.org/)