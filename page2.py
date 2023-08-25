# Complex built-in types
# list is an array
# dictionaries are like Perl's hash (or Ruby's Hash)
# Then there are sets, tuples etc that we ignore for now

# lists
# To declare
direct_integer_list = [1,2,3]
direct_character_list = ['a','b','c']
direct_mixed_list = [1,'b',"a string"]

pre_define_list1 = []
pre_define_list2 = list()   # "constructor" declaration

# Some simple operations - there are many more
my_list = ['d', 'e' , 'g']
my_list.append('q') # Add 'q' (to the end of the list)
my_list.append('a') # Add 'q' (to the end of the list)
print(my_list)
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
print(my_list[2])               # lists starts at index 0
print(my_list[0], my_list[-1])  # index -1 is the 'last' index

# dictionaries
# To declare
direct_dict1 = { 'name' : 'Fritz', 'address' : 'Belgium' }

pre_define_dict1 = {}
pre_define_dict1 = dict()      # "constructor" declaration

# Some simple operations
my_dict = {
    'France' : 'Paris',
    'Italy' : 'Rome',
    'England' : 'London',
    'Belgium' : 'Brussels'
}

my_dict['Spain'] = 'Madrid'
print(my_dict.keys())
print(my_dict.values())
countries = list(my_dict.keys())
print(countries)

test = 'Spain' in my_dict
print(test)
test = 'Norway' in my_dict
print(test)
test = 'Paris' in my_dict.values()
print(test)

print(my_dict['Italy'])


# More built-in function:
# len(s)
# Return the length (the number of items) of an object. The argument
# may be a sequence (such as a string, bytes, tuple, list, or range)
# or a collection (such as a dictionary, set, or frozen set).
#
# str()
# Return a string version of object.
#
print(str(my_dict) + ' has ', end = '')
print(len(my_dict), end = '')
print(' items')

print()     # insert a newline
# Or if you print it as an object, print will use str(object)
# To print the same as above
print(my_dict, 'has',len(my_dict), 'items', sep=' ')

# repr()
# Return a string containing a printable representation of an object
print('\nPrinted as repr(): ' + repr(my_list))


# int(x, base=10)
# Return an integer object constructed from a number or string x
a_value_as_a_string = "4711"
print(int(a_value_as_a_string))
print(repr(a_value_as_a_string))        # A string
print(repr(int(a_value_as_a_string)))   # A number