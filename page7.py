#!/usr/bin/env python3
#
#----------------------------------------------------------------------

import argparse
import os
import sys
import textwrap

have_colorama = True
try:
    import colorama
    # import redis
except ModuleNotFoundError:
    print(f'You can install colorama by executing')
    print(f'pip install colorama\n')
    have_colorama = False

_my_name = os.path.basename(__file__)

if have_colorama:
    RED=colorama.Fore.LIGHTRED_EX
    RST=colorama.Style.RESET_ALL
else:
    RED=''
    RST=''

DESCRIPTION = f"""
Collect all files in directory --directory with the extension --extension.
List them by giving option --list

It should be quite easy to make this script better (or even useful)!
"""
USAGE_EXAMPLE = f"""
Examples:
> {_my_name} -d . -l

"""

#-------------------------------------------------------------------------------
def parse_arguments():
    parser = argparse.ArgumentParser(_my_name,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(DESCRIPTION),
        epilog=textwrap.dedent(USAGE_EXAMPLE))
    add = parser.add_argument   # Make a 'shortcut' to the function

    add('-q', '--quiet', action='store_true',
        help='be more quiet')
    add('-v', '--verbose', action='store_true',
        help='be more verbose')

    add('-d', '--directory', metavar='test-dir',
        required=True,
        help='root path where to look for files (recursively)')
    add('-e', '--extension', metavar='.EXT',
        default='.py',
        help='extension of the files to look for, .py by default')
    add('-l', '--list_files', action='store_true',
        help='print files found')

    return parser.parse_args()

#-------------------------------------------------------------------------------
def collect_all_files(directory, extension):
    the_chosen_ones = {}
    ext = extension
    for root, _dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(ext):
                full_path = os.path.join(root, file)
                if file in the_chosen_ones:
                    print(RED + f'Skipping {full_path} - ')
                    print(f'  {file} already found as {the_chosen_ones[file]}')
                    print(RST)
                the_chosen_ones[file] = full_path

    return the_chosen_ones

#-------------------------------------------------------------------------------
def list_files(file_list, options):
    for file in file_list:
        print(f'{file} = {file_list[file]}')

#-------------------------------------------------------------------------------
#
#-------------------------------------------------------------------------------
def main():
    if have_colorama:
        colorama.init()
    options = parse_arguments()

    test_dir = options.directory
    ext = options.extension

    test_files = collect_all_files(test_dir, ext)
    if not test_files:
        print(f'No {ext} files found in directory {test_dir}')
        return 3

    if options.list_files:
        list_files(test_files, options)

    return 0

#-------------------------------------------------------------------------------
# Execute main only if this script was invoked
if __name__ == "__main__":
    sys.exit(main())
