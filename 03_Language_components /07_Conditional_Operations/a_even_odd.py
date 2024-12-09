number = 89
print(f"{number             = }")
print(f"{number / 2         = }")
print(f"{number % 2         = }")
print(f"{number % 2 == 0    = }")


if number % 2 == 0:
    print(f"{number} is Even")

if number % 2:
    print(f"{number} is odd")


if number % 2 == 0:
    print(f"{number} is EVEN")
else:
    print(f"{number} is ODD")

# rewriting
if number % 2:
    print(f"{number} is ODD")
else:
    print(f"{number} is EVEN")
