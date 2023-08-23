# Comments starts with an # to the end of line
# C:\Python\Python310\Doc>python3107.chm
# Note: Python is UTF8 by nature

# Primitive types are numbers and strings
an_integer = 4711
a_float = 3.15926

string_1 = "In double quote strings you can have ' quotes\n"
string_2 = 'and with single quotes you can have " quote characters\n'

# Simple operators
sum = an_integer + 34
pi  = a_float - 0.01
product = sum * 3
quote = product / 3

# String operators
string_3 = "There is no other difference " + 'between them\n' # literal + concatenation
str4 = 'Another ' 'concatenation'  # "automatic" concatenation
separator_line = 80 * '-'   # Will print 80 hypthens
str5 = str4 + '\n' + separator_line  # Use + to concatenate variables

# Built-in functions
# print() adds a newline by default
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print('Hello World')
print(separator_line)
print('Hello', end = '')
print(' ', end = '')
print('World')

# len(s)
# Return the length (the number of items) of an object. The argument
# may be a sequence (such as a string, bytes, tuple, list, or range)
# or a collection (such as a dictionary, set, or frozen set).


print(str4 + ' has ', end = '')
print(len(str4), end = '')
print(' characters')

# Common functions str() repr() int() ord() char()

# chr(i)
# Return the string representing a character whose Unicode code point
# is the integer i. For example, chr(97) returns the string 'a',
# while chr(8364) returns the string '€'. This is the inverse of
# ord().


# ord(c)
# Given a string representing one Unicode character, return an integer
# representing the Unicode code point of that character. For example,
# ord('a') returns the integer 97 and ord('€') (Euro sign) returns
# 8364. This is the inverse of chr().


# Define functions

# More complex built-in types, data structures
# list, dictionaries (tuple, set)

