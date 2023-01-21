from pyfiles.list import list
from pyfiles.edit import edit
help = '''commands:
        - test: executes a test
        - list: choose a folder and see whats inside of it - 'self' to see existing folder 
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
while running:
    command = input("〉")
    if command == "test":
        print("hi test test")
    elif command == "list":
        print(list())
    elif command == "edit":
        print(edit())
    elif command == "help":
        print(help)
    elif command == "exit":
        print("exiting the program")
        break
    else:
        print("commmand not available, write 'help' for a list of existing commands")