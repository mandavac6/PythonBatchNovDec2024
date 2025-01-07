"""
Purpose: Reading(Parsing) csv, using unstructure file ops
"""
# Method 1
with open("my_file.csv", mode="r") as fh:
    file_content = fh.read()


names = []
for each_line in file_content.splitlines()[1:]:
    name = each_line.split(',')[1]
    names.append(name)

print(f"{names = }")
# names = ['Aaron Rogers', 'Tom Brady', 'Nick Bosa', 'TJ Watt']

# Method 2
with open("my_file.csv", mode="r") as fh:
    file_content = fh.readlines()

names = []
for each_line in file_content[1:]:
    name = each_line.split(',')[1]
    names.append(name)

print(f"{names = }")
# names = ['Aaron Rogers', 'Tom Brady', 'Nick Bosa', 'TJ Watt']