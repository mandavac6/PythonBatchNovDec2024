"""
Purpose:
    file operations
        - read  - r
        - write - w -> if file not present, file will be created;
                       if present, existing content will be overwritten
        - append- a

        default is read mode

"""

# open('a_first_file.txt')
# .venv@mandavac6 ➜ /workspaces/PythonBatchNovDec2024/13_File_Operations/01_Unstructured_file (class25) $ python 01_create_file.py 
# Traceback (most recent call last):
#   File "/workspaces/PythonBatchNovDec2024/13_File_Operations/01_Unstructured_file/01_create_file.py", line 13, in <module>
#     open('a_first_file.txt')
# FileNotFoundError: [Errno 2] No such file or directory: 'a_first_file.txt'

# open('a_first_file.txt', mode='r')
# .venv@mandavac6 ➜ /workspaces/PythonBatchNovDec2024/13_File_Operations/01_Unstructured_file (class25) $ python 01_create_file.py 
# Traceback (most recent call last):
#   File "/workspaces/PythonBatchNovDec2024/13_File_Operations/01_Unstructured_file/01_create_file.py", line 20, in <module>
#     open('a_first_file.txt', mode='r')
# FileNotFoundError: [Errno 2] No such file or directory: 'a_first_file.txt'

# open('a_first_file.txt', mode='w')

file_handler = open("a_first_file.txt", mode="w")
print(f"{type(file_handler) =}")
print(f"{file_handler       =}")

# type(file_handler) =<class '_io.TextIOWrapper'>
# file_handler       =<_io.TextIOWrapper name='a_first_file.txt' mode='w' encoding='UTF-8'>

file_handler.write("This is the first line\n")
file_handler.write("This is the second line\n")

file_handler.close()