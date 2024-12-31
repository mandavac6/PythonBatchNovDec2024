"""
Purpose: To copy a file from one directory, to another
"""
# import os
# import shutil

# print(dir(shutil))


'''
'COPY_BUFSIZE', 'Error', 'ExecError', 'ReadError', 'RegistryError', 'SameFileError', 'SpecialFileError', 
'_ARCHIVE_FORMATS', '_BZ2_SUPPORTED', '_GiveupOnFastCopy', '_HAS_FCOPYFILE', '_LZMA_SUPPORTED', '_UNPACK_FORMATS',
'_USE_CP_SENDFILE', '_WINDOWS', '_WIN_DEFAULT_PATHEXT', '_ZLIB_SUPPORTED', '__all__', '__builtins__', '__cached__',
'__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_access_check', '_basename', 
'_check_unpack_options', '_copyfileobj_readinto', '_copytree', '_copyxattr', '_destinsrc', '_ensure_directory',
'_fastcopy_fcopyfile', '_fastcopy_sendfile', '_find_unpack_format', '_get_gid', '_get_uid', '_is_immutable',
'_islink', '_make_tarball', '_make_zipfile', '_ntuple_diskusage', '_rmtree_islink', '_rmtree_safe_fd', 
'_rmtree_unsafe', '_samefile', '_stat', '_unpack_tarfile', '_unpack_zipfile', '_use_fd_functions', 
'_win_path_needs_curdir', '_winapi', 'chown', 'collections', 'copy', 'copy2', 'copyfile', 'copyfileobj', 
'copymode', 'copystat', 'copytree', 'disk_usage', 'errno', 'fnmatch', 'get_archive_formats', 'get_terminal_size',
'get_unpack_formats', 'ignore_patterns', 'make_archive', 'move', 'nt', 'os', 'posix', 'register_archive_format', 
'register_unpack_format', 'rmtree', 'stat', 'sys', 'unpack_archive', 'unregister_archive_format', 'unregister_unpack_format', 'warnings', 'which'
'''

# python_path = shutil.which("python")
# print(python_path)

'''
/workspaces/PythonBatchNovDec2024/.venv/bin/python
'''


# ls_path = shutil.which("ls")
# print(ls_path)

'''
/usr/bin/ls
'''


import os
import shutil


# Purpose: To copy a file from one directory, to another

def copy_file(src_dir, dest_dir, filename):
    source_path = os.path.join(src_dir, filename)
    dest_path = os.path.join(dest_dir, filename)

    if os.path.exists(dest_path):
        print("file already exists. So, deleting")
        os.remove(dest_path)
    os.makedirs(dest_dir)

    shutil.copyfile(source_path, dest_path)


copy_file("test_dir1", "test_dir2", "text_file1.txt")