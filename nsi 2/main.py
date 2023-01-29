from pyfiles.list import list
from pyfiles.edit import edit
from pyfiles.nombre_lettres import nombre_lettres
help = '''commands:
        - test: executes a test
        - list: choose a folder and see whats inside of it
        - edit: gives you the ability to manipulate text files.
        - occ: lets you see how many times a letter is occurring in the chosen text file 
        - exit: stops the program
        '''
art = """
        __________
        |^|     | |
        | |_____| |
        |  _____  |
        | |     | |
        | |_____| |
        |_|_____|_|
    """
print(art)

running = True
# each command is explained in the help variable
# we have an other help command in the edit file
while running:
    #we lowercase the command in case the user input with shift on
    command = (input("〉")).lower()
    if command == "hello world":
        print("hello friend! ^_^")
    elif command == "list":
        print(list())
    elif command == "occ":
        nombre_lettres()
    elif command == "edit":
        edit()
    elif command == "help":
        print(help)
    elif command == "exit":
        print("exiting the program")
        break
    else:
        print("commmand not available, write 'help' for a list of existing commands")