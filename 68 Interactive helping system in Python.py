'''Make a mini-system that uses the Python Interactive Help. 
The user will enter the command and the manual will appear. 
When the user types the word 'end', the program will end. IMPORTANT: Use colors.'''
from pydoc import help

def interactive_help():
    while True:
        command = input('\033[1;34mEnter a command or "end" to quit: \033[m')
        if command == 'end':
            break
        else:
            print('\033[1;33m')
            help(command)
            print('\033[m')

interactive_help()