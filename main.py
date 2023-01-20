from pyfiles.list import list

help = '''commands:
        - test: executes a test
        - list: choose a folder and see whats inside of it - 'self' to see existing folder 
        - exit: stops the program
        '''

running = True

while running:
    command = input("〉")
    if command == "test":
        print("hi test test")
    elif command == "list":
        print(list())
    elif command == "help":
        print(help)
    elif command == "exit":
        print("exiting the program")
        break
    else:
        print("commmand not available, write 'help' for a list of existing commands")