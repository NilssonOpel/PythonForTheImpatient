# To make the print-outs more useful for the coming pages, let us talk about
# f'-strings, or formatted string literals
# In an f'-string an expression within { and } will give its value

a_string = "Counting"
a_list = ['1', '2', '3']
explicit_f_string = f'{a_string}'
print(f'{a_string} {a_list}')
print(explicit_f_string)
print(f'Just {explicit_f_string}')

# For debugging a common usage is to add a ' = ' inside { and }
test = 'unt' in a_string
print(f'{test = }')

# f-strings can look like
print(f'{test = }')
print(f"{test = }")
print(F'{test = }')

