# Finally some programming

def using_while(start, end):
    current = start
    while (current < end):  # Once again, not the ':' and indentation
        print(f'{current} < {end}', end=' (keep on), ')
        current = current + 1
    print(f'\nfinally done, {current = } {end = }')     # add a terminating new line

    return current

def using_if(test, facit):
    if test == facit:
        print(f'{test} equals {facit}')
    elif test < facit:
        print(f'{test} is less than {facit}')
    elif test > facit:
        print(f'{test} is larger than {facit}')
    else:
        print(f'{test} does not compare to {facit}')

def using_for():
    # One can define functions within functions as well
    def for_subfunction(sequence):
        for item in sequence:
            print(item, end=' ')
        print()

    # for can iterate over items in lists, dictionaries or strings
    mixed_list = [1,'b',"a string"]
    for_subfunction(mixed_list)

    capitals = {
        'France' : 'Paris',
        'Italy' : 'Rome',
        'England' : 'London',
        'Belgium' : 'Brussels'
    }
    for_subfunction(capitals)

    a_string = 'Keep Calm'
    for_subfunction(a_string)

def mimic_for_as_in_C():
    def for_subfunction(sequence):
        for item in sequence:
            print(item, end = ', ')
        print()

    # In C you can iterate over a sequence of numbers. To do that in Python you
    # first produce the number-sequence using the function(s) range()
    # range(start, stop[, step])  step is set to 1 if not given
    # range(stop) -> range(0, stop, 1)
    # Note that 'stop' is NOT included in the range
    zero_to_nine = range(10)    # or range(0, 10, 1), or range(0, 10)
    for_subfunction(zero_to_nine)

# You also use 'break', which end the current for or while loop
# and 'continue' that 'jumps back' to the start of the next iteration
def break_and_continue(start, end):
    while start < end:
        start = start + 1
        if start == 3:  # do not want to print that
            continue
        if start == 5:  # that is enough, stop the looping
            break
        print(f'{start = }')

mimic_for_as_in_C()
using_for()
using_if(47, 212)
using_while(0, 9)
break_and_continue(0, 9)
