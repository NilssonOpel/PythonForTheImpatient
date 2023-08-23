# Complex built-in types
# list is an array
# dictionaries are like Perl's hash
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



