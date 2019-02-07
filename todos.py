from sys import argv
from os.path import exist
from textwrap import dedent

script, from_file, to_file = argv


# i feel i have to do something similar to this but read only a single line
# where my list is 
def main():
    in_file = open(from_file)
    in_data = in_file.read()

    print(f'''
          Copying my todo list {from_file} to a txt file.
          Does the file exist? {exists(to_file)}. Hit ENTER to continue.''')

    input()

    out_file = open(to_file, 'w')
    out_file.write(in_data)
    out_file.close()
    in_file.close()

main()



#  how to open a file that is not created yet
#
#
#
#
#

# how to read a file
# def main():
#     f=open("guru99.txt", "r")
# if f.mode == 'r':
#     contents =f.read()
# print(contents)
