# How to define your own functions


def my_function(parameter1, parameter2):    # Note the terminating ':'!
    # And then an indentation of four spaces - 'scoping' with Pyhon is done
    # using whitespace, not '{' and '}' as in C, or 'end' as in Ruby ...
    sum = parameter1 + parameter2
    result = len(str(sum))
    print(f'{sum = }\n{result = }')
    return result

# You can call it with strings and integers
my_function('First', 'Second')
my_function(1, 4)
# and  with lists
list1 = ['element1', 'element2']
list2 = ['item1', 'item2']
my_function(list1, list2)

# This works as long as the parameters has a '+' operator and a 'str()'

# So this will not work since you cannot 'add' a string and an integer
#my_function('First', 4)
# But this will, since str(42) will produce the string "42", not the value 42
my_function('First', str(42))
