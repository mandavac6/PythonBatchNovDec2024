"""
Purpose: constructor is a method which will be
    called the moment instance is created
"""

from pprint import pp


class Person(object):
    """class definition"""

    my_class_var = 111  # class - level variable

    def __init__(self):
        print("New instance is born! Adding default features")
        self.inst_var = 222
        local_var = 333
        # return 123  # TypeError: __init__() should return None, not 'int'
        # NOTE: Construction should return only None

    def instance_method(self):
        return "This is an instance method"


# Instantiation
p1 = Person()
print(p1)


print(Person.instance_method(p1))
print(p1.instance_method())
assert p1.instance_method() == Person.instance_method(p1)




# p1.__init__() # But NOT RECOMMEND, as code duplicate execution

for each_attribute in dir(p1):
    print(each_attribute)

print()

# To get only the instance variables
print(f"p1.__dict__: {p1.__dict__}")
print(f"vars(p1)   : {vars(p1)}")
assert vars(p1) == p1.__dict__
print()


print("vars(Person):")
pp(vars(Person))
print()
# -------------------------------------------------


pp(vars())  # pp(globals())

# Note: calling the vars() function without parameters will
# return a dictionary containing the local symbol table.


"""
Assignment:
    run below in shell
    vars(list)

    pp(vars(list))
mappingproxy({'__new__': <built-in method __new__ of type object at 0x5587c1a44ba0>,
              '__repr__': <slot wrapper '__repr__' of 'list' objects>,
              '__hash__': None,
              '__getattribute__': <slot wrapper '__getattribute__' of 'list' objects>,
              '__lt__': <slot wrapper '__lt__' of 'list' objects>,
              '__le__': <slot wrapper '__le__' of 'list' objects>,
              '__eq__': <slot wrapper '__eq__' of 'list' objects>,
              '__ne__': <slot wrapper '__ne__' of 'list' objects>,
              '__gt__': <slot wrapper '__gt__' of 'list' objects>,
              '__ge__': <slot wrapper '__ge__' of 'list' objects>,
              '__iter__': <slot wrapper '__iter__' of 'list' objects>,
              '__init__': <slot wrapper '__init__' of 'list' objects>,
              '__len__': <slot wrapper '__len__' of 'list' objects>,
              '__getitem__': <method '__getitem__' of 'list' objects>,
              '__setitem__': <slot wrapper '__setitem__' of 'list' objects>,
              '__delitem__': <slot wrapper '__delitem__' of 'list' objects>,
              '__add__': <slot wrapper '__add__' of 'list' objects>,
              '__mul__': <slot wrapper '__mul__' of 'list' objects>,
              '__rmul__': <slot wrapper '__rmul__' of 'list' objects>,
              '__contains__': <slot wrapper '__contains__' of 'list' objects>,
              '__iadd__': <slot wrapper '__iadd__' of 'list' objects>,
              '__imul__': <slot wrapper '__imul__' of 'list' objects>,
              '__reversed__': <method '__reversed__' of 'list' objects>,
              '__sizeof__': <method '__sizeof__' of 'list' objects>,
              'clear': <method 'clear' of 'list' objects>,
              'copy': <method 'copy' of 'list' objects>,
              'append': <method 'append' of 'list' objects>,
              'insert': <method 'insert' of 'list' objects>,
              'extend': <method 'extend' of 'list' objects>,
              'pop': <method 'pop' of 'list' objects>,
              'remove': <method 'remove' of 'list' objects>,
              'index': <method 'index' of 'list' objects>,
              'count': <method 'count' of 'list' objects>,
              'reverse': <method 'reverse' of 'list' objects>,
              'sort': <method 'sort' of 'list' objects>,
              '__class_getitem__': <method '__class_getitem__' of 'list' objects>,
              '__doc__': 'Built-in mutable sequence.\n'
                         '\n'
                         'If no argument is given, the constructor creates a '
                         'new empty list.\n'
                         'The argument must be an iterable if specified.'})
_______________________________________________________________________________________

    vars(str)

    >>> pp(vars(str))
mappingproxy({'__new__': <built-in method __new__ of type object at 0x5587c1a503c0>,
              '__repr__': <slot wrapper '__repr__' of 'str' objects>,
              '__hash__': <slot wrapper '__hash__' of 'str' objects>,
              '__str__': <slot wrapper '__str__' of 'str' objects>,
              '__getattribute__': <slot wrapper '__getattribute__' of 'str' objects>,
              '__lt__': <slot wrapper '__lt__' of 'str' objects>,
              '__le__': <slot wrapper '__le__' of 'str' objects>,
              '__eq__': <slot wrapper '__eq__' of 'str' objects>,
              '__ne__': <slot wrapper '__ne__' of 'str' objects>,
              '__gt__': <slot wrapper '__gt__' of 'str' objects>,
              '__ge__': <slot wrapper '__ge__' of 'str' objects>,
              '__iter__': <slot wrapper '__iter__' of 'str' objects>,
              '__mod__': <slot wrapper '__mod__' of 'str' objects>,
              '__rmod__': <slot wrapper '__rmod__' of 'str' objects>,
              '__len__': <slot wrapper '__len__' of 'str' objects>,
              '__getitem__': <slot wrapper '__getitem__' of 'str' objects>,
              '__add__': <slot wrapper '__add__' of 'str' objects>,
              '__mul__': <slot wrapper '__mul__' of 'str' objects>,
              '__rmul__': <slot wrapper '__rmul__' of 'str' objects>,
              '__contains__': <slot wrapper '__contains__' of 'str' objects>,
              'encode': <method 'encode' of 'str' objects>,
              'replace': <method 'replace' of 'str' objects>,
              'split': <method 'split' of 'str' objects>,
              'rsplit': <method 'rsplit' of 'str' objects>,
              'join': <method 'join' of 'str' objects>,
              'capitalize': <method 'capitalize' of 'str' objects>,
              'casefold': <method 'casefold' of 'str' objects>,
              'title': <method 'title' of 'str' objects>,
              'center': <method 'center' of 'str' objects>,
              'count': <method 'count' of 'str' objects>,
              'expandtabs': <method 'expandtabs' of 'str' objects>,
              'find': <method 'find' of 'str' objects>,
              'partition': <method 'partition' of 'str' objects>,
              'index': <method 'index' of 'str' objects>,
              'ljust': <method 'ljust' of 'str' objects>,
              'lower': <method 'lower' of 'str' objects>,
              'lstrip': <method 'lstrip' of 'str' objects>,
              'rfind': <method 'rfind' of 'str' objects>,
              'rindex': <method 'rindex' of 'str' objects>,
              'rjust': <method 'rjust' of 'str' objects>,
              'rstrip': <method 'rstrip' of 'str' objects>,
              'rpartition': <method 'rpartition' of 'str' objects>,
              'splitlines': <method 'splitlines' of 'str' objects>,
              'strip': <method 'strip' of 'str' objects>,
              'swapcase': <method 'swapcase' of 'str' objects>,
              'translate': <method 'translate' of 'str' objects>,
              'upper': <method 'upper' of 'str' objects>,
              'startswith': <method 'startswith' of 'str' objects>,
              'endswith': <method 'endswith' of 'str' objects>,
              'removeprefix': <method 'removeprefix' of 'str' objects>,
              'removesuffix': <method 'removesuffix' of 'str' objects>,
              'isascii': <method 'isascii' of 'str' objects>,
              'islower': <method 'islower' of 'str' objects>,
              'isupper': <method 'isupper' of 'str' objects>,
              'istitle': <method 'istitle' of 'str' objects>,
              'isspace': <method 'isspace' of 'str' objects>,
              'isdecimal': <method 'isdecimal' of 'str' objects>,
              'isdigit': <method 'isdigit' of 'str' objects>,
              'isnumeric': <method 'isnumeric' of 'str' objects>,
              'isalpha': <method 'isalpha' of 'str' objects>,
              'isalnum': <method 'isalnum' of 'str' objects>,
              'isidentifier': <method 'isidentifier' of 'str' objects>,
              'isprintable': <method 'isprintable' of 'str' objects>,
              'zfill': <method 'zfill' of 'str' objects>,
              'format': <method 'format' of 'str' objects>,
              'format_map': <method 'format_map' of 'str' objects>,
              '__format__': <method '__format__' of 'str' objects>,
              'maketrans': <staticmethod(<built-in method maketrans of type object at 0x5587c1a503c0>)>,
              '__sizeof__': <method '__sizeof__' of 'str' objects>,
              '__getnewargs__': <method '__getnewargs__' of 'str' objects>,
              '__doc__': "str(object='') -> str\n"
                         'str(bytes_or_buffer[, encoding[, errors]]) -> str\n'
                         '\n'
                         'Create a new string object from the given object. If '
                         'encoding or\n'
                         'errors is specified, then the object must expose a '
                         'data buffer\n'
                         'that will be decoded using the given encoding and '
                         'error handler.\n'
                         'Otherwise, returns the result of object.__str__() '
                         '(if defined)\n'
                         'or repr(object).\n'
                         'encoding defaults to sys.getdefaultencoding().\n'
                         "errors defaults to 'strict'."})
_______________________________________________________________________________________

    vars(dict)

    >>> pp(vars(dict))
mappingproxy({'__new__': <built-in method __new__ of type object at 0x5587c1a468e0>,
              '__repr__': <slot wrapper '__repr__' of 'dict' objects>,
              '__hash__': None,
              '__getattribute__': <slot wrapper '__getattribute__' of 'dict' objects>,
              '__lt__': <slot wrapper '__lt__' of 'dict' objects>,
              '__le__': <slot wrapper '__le__' of 'dict' objects>,
              '__eq__': <slot wrapper '__eq__' of 'dict' objects>,
              '__ne__': <slot wrapper '__ne__' of 'dict' objects>,
              '__gt__': <slot wrapper '__gt__' of 'dict' objects>,
              '__ge__': <slot wrapper '__ge__' of 'dict' objects>,
              '__iter__': <slot wrapper '__iter__' of 'dict' objects>,
              '__init__': <slot wrapper '__init__' of 'dict' objects>,
              '__or__': <slot wrapper '__or__' of 'dict' objects>,
              '__ror__': <slot wrapper '__ror__' of 'dict' objects>,
              '__ior__': <slot wrapper '__ior__' of 'dict' objects>,
              '__len__': <slot wrapper '__len__' of 'dict' objects>,
              '__getitem__': <method '__getitem__' of 'dict' objects>,
              '__setitem__': <slot wrapper '__setitem__' of 'dict' objects>,
              '__delitem__': <slot wrapper '__delitem__' of 'dict' objects>,
              '__contains__': <method '__contains__' of 'dict' objects>,
              '__sizeof__': <method '__sizeof__' of 'dict' objects>,
              'get': <method 'get' of 'dict' objects>,
              'setdefault': <method 'setdefault' of 'dict' objects>,
              'pop': <method 'pop' of 'dict' objects>,
              'popitem': <method 'popitem' of 'dict' objects>,
              'keys': <method 'keys' of 'dict' objects>,
              'items': <method 'items' of 'dict' objects>,
              'values': <method 'values' of 'dict' objects>,
              'update': <method 'update' of 'dict' objects>,
              'fromkeys': <method 'fromkeys' of 'dict' objects>,
              'clear': <method 'clear' of 'dict' objects>,
              'copy': <method 'copy' of 'dict' objects>,
              '__reversed__': <method '__reversed__' of 'dict' objects>,
              '__class_getitem__': <method '__class_getitem__' of 'dict' objects>,
              '__doc__': 'dict() -> new empty dictionary\n'
                         'dict(mapping) -> new dictionary initialized from a '
                         "mapping object's\n"
                         '    (key, value) pairs\n'
                         'dict(iterable) -> new dictionary initialized as if '
                         'via:\n'
                         '    d = {}\n'
                         '    for k, v in iterable:\n'
                         '        d[k] = v\n'
                         'dict(**kwargs) -> new dictionary initialized with '
                         'the name=value pairs\n'
                         '    in the keyword argument list.  For example:  '
                         'dict(one=1, two=2)'})


"""