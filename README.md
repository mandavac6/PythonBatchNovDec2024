# PythonBatchNovDec2024

## Local setup in windows

    Install 

    git for windows

    Visual Studio code

    python
        microsoft store -- python3 (version)


    git clone https://github.com/mandavac6/PythonBatchNovDec2024.git

    first time you need to pass the credentials, when running

## Git Commands 

To clone the Repo to Local 

    git clone <url>

to get the status of the repo 

    git status

to list Branches

    git branch 

To create a new branch 

    git checkout -b <branchname>

To pull the latest code from main branch

    git pull origin <branchname>

To add a file to the Stagging area 
    
    git add <filename>

to commit the code to the repo 

    git commit -m "message for the commit"

to push the latest code to main branch

    git push origin <branchname>

to check the changes in the exsisting file 

    git diff <filename>

### Daily Commands

to get the status of the repo 

    git status

To checkout to the main branch 

    git checkout main

To pull the latest code from main branch

    git pull origin <branchname>

To create a new branch

    git checkout -b <branchname>

## Virtual Environment

    Isolated environment 

    why needed
        - same system, multiple projects
            - different python versions 
            - same python verison, but differenet module versions

    How to create Virtual Environment 
        - Virtualenv
        - venv
        - pipenv
        - poetry 
        - uv

    Using Virtualenv
        
        Install
            pip install virtualenv
        
        create virtual environment
            python -m virtualenv .venv
        
        activate virtual environment
            linux
                source .venv/bin/activate

            windows
                .venv/script/activate

    Using Poetry
    pip install -U pip
    pip install poetry
    python -m poetry init
    python -m poetry shell

    pip install poetry
    poetry add pandas 


## Course Completed

[Class recording drive folder Link](https://drive.google.com/drive/folders/1nz25v0dUyiwZf2bAFQ9OPtmbH3rCpu9E)

[Class 00 Nov 4th 2024]()
    
    Dev Setup
    Installing IDE/Editor
    Installing Python and local setup
    Github access, creating project

[Class01 Nov 6th 2024]()

    Git Commands
    markdown syntax
    Daily activity and usage 
    Importance of python
    two versions of python (2.x & 3.x) 

[Class02 Nov 11th 2024]()

    PEP 8 Guidelines (https://peps.python.org/pep-0008/)
    shebang line
    Indendation issues and best practices
    Built-in Functions
    Print functions 
    Scriptmode vs interactive mode 
    Jupyter notebook usage 
    Ascii and Unicade Characters 

[Class03 Nov 13th 2024]()
    
    Comment Operator 
    Keyword and Identifiers 
    Line continution and statement seperator operators
    02.Basics
        Arthematic Operations 
        +, -, *, /, //, %, 
        divmod()
        pow()
        compound operators

[Class04 Nov 15th 2024]()

    Practical Problem solving
    working with complex numbers
    abs() function
    Operator precedence in Arithmetic operations

[Class05 Nov 20th 2024]()

    String operations
    Usage of single, double and triple quotes
    len() function
    Indexing and Slicing Strings
    


[Class06 Nov 22th 2024]()

    String attributes
    

[Class07 Nov 25th 2024]()

    String attributes

[Class08 Nov 27th 2024]()

    String formatting: old & new styles, f-strings
    unicode strings
    
[Class09 Nov 29th 2024]()

    bytearray() and byte() strings
    Usage of help
    Usage of pydoc

    03.Language Components
        Relational Operations
        Logical Operations

[Class10 Dec 2nd 2024]()

    Logical Operations
    Boolean Operations
    Bitwise Operations
    Identity Operations
    Dual Memory management Strategy
    range() function
    Conditional Operations

[Class11 Dec 4th 2024]()

    Structural Pattern Matching
    Loops: for & while, break, continue, pass, sys.exit
    Assignments

[Class12 Dec 6th 2024]()

    Walrus Operator

    04.Exception Handling
        Exceptions Hierarchy
        Different types of errors, error vs exception and exception groups
        Handling single and multiple exceptions
        raising exceptions
        asserts
        traceback
        exception Groups
        warnings


[Class13 Dec 9th 2024]()

    05.Debugging
        Importance of logical errors
        Debugging with pydevd
        Debugging with pdb, ipdb
        breakpoint() function
        PYTHONBREAKPOINT environment variable usage
        post analyses of executed script

[Class14 Dec 10th 2024]()

    06.Collections
        Lists

[Class15 Dec 11th 2024]()

    Copy Problem - shallow copy vs deepcopy
    Tuples & namedtuples
    Immutability & unpacking
    Sets
        attributes, operations

[Class16 Dec 13th 2024]()

    fronzensets
    Dictionaries
        zip() function
        workaround for switch case
    Comprehensions
    Working with Iterables - sum(), max(), min()

[Class17 Dec 16th 2024]()

    07.Functions
    Functions with & without arguments, keyword arguments
    Functions with Different return types and unpacking
    Functions with with Default arguments
    variadic functions : variable arguments and variable keyword arguments
    Functions with keyword only arguments
    Scoping: Global vs Local
        call by reference
        call by value

[Class18 Dec 17th 2024]()

    Partial Functions
    Anonymous(Lambda) Functions
    Higher order functions: map(), filter(), functool.reduce()
    Recursions and recursions limit


[Class19 Dec 18th 2024]()

    inner functions
    closures

    08.Decorator Design Pattern
    Necessity
    function Decorator
    Practical Examples
    syntactic sugar for decorators
    multiple decorators on same function
    decorators with arguments
    functools - wrap, lru_cache
    class decorator


[Class20 Dec 19th 2024]()

    Iterables, Iterators, Generators and co-routines
    Iterables
        different ways of extracting values from iterables
    Iterators
        iter() protocol
        itertools module

[Class21 Dec 20th 2024]()

    Generators
    yield vs return
    function vs Generator
    Generator pipelining
    Generator Expression

[Class22 Dec 23rd 2024]()

    Coroutine
    Generator vs Coroutine
    coroutine pipelining

    10.Modules
        Basic Modules
        - math, sys, argparse

[Class23 Dec 24th 2024]()

    os, shutil, pathlib

[Class24 Dec 26th 2024]()

    shutil, subprocess, getpass
    time related
        - time, datetime, pytz, timeit, calendar
    others
        - random, collections, atexit, contextlib, base64

[Class25 Dec 27th 2024]()

    create user-defined module
    creating user-defined package

    packaging
    creating the wheel files, tar files
    publishing with twine
    egg files

    11.File Operations
    flat files


[Class26 Dec 30th 2024]()

    Non-flat files
    pickle 
    shelve 
    xml 
    csv

[Class27 Jan 02nd 2025]()

    windows local setup
    poetry installation
    Troubleshooting experince
    csv
    dat
    tsv


## Next Class 

    