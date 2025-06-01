print("hello world")

# strings
# list
# tuple
# map
# sets
# dictionary


a = 10 + 10
print(a)     # prints value of a
print(id(a))    # id is to prints the memory location of variable a

# there are methods to specific data type
print(type(a))  # type function is to print the data type of variable a

print("value of a : ", a)     # prints value of a
print("memory location of a is : ", id(a))    # id is to prints the memory location of variable a

# there are methods to specific data type
print("data type of a is: "type(a))  # type function is to print the data type of variable a

x = 1.29
y = 3.45
a = x + y
print("value of a is : ", a)

print("value of a: ", a , " data type of a : ", type(a))


# this is for line comment
"""
This is for block comment. We can comment a block of lines
"""

sample_str = "it is string"
print(sample_str, type(sample_str))
# to show attributes of an object we use dir function. Eg: sample_str.join, sample_str.count, sample_str.isupper etc
"""
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 
'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 
'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 
'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 
'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
"""
print(dir(sample_str))

print(sample_str.capitalize())    # It changes first letter to capital
print(sample_str.casefold())    # it changes the capital letters to small letters
print(sample_str.swapcase())
print(sample_str.split(' '))    # to convert each word to list
print(sample_str.find('i'))

sample_str = "Hello"
# indexing starts with 0 in python
print(sample_str.index('H'))
print(sample_str[2])
print(len(sample_str))

a = True
b = False

print(a and b)
print(a or b)

a = 2
b = 3
print(a % b)    # modulo division. Returns remainder
print(a // b)   # floor division: means integer division
print(a ** b)   # exponentiation: 2^3

sample_str = "this is a string"
sample_str[0] = 'T'
# TypeError: 'str' object does not support item assignment

print(sample_str)
