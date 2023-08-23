# Some useful internal variables, including argv
# Lib\site-packages\pip\_vendor\pygments\lexers\python.py
import sys  # We will come to import later

print(f'{sys = }')          # Will show that sys is a module
print(f'{dir(sys) = }')     # dir() lists what the module sys defines
print(f'{sys.argv = }')     # Invokation arguments
print(f'{sys.platform = }') # Identifies operating system
print(f'{sys.version = }')  # Version information for your Python interpreter
print(f'{__name__ = }')     # Says __main__ for primary source file
print(f'{__file__ = }')     # Path of current source file
