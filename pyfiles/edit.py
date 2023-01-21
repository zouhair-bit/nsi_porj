import os
def checker():
    while True:
        print(os.listdir("folders"))
        direct_name = input("Please input directory name: ")
        #checks if the directory exists
        test = os.path.exists("folders/"+direct_name)
        if test:
            lister= os.listdir("folders/"+direct_name)
            if lister == []:
                print("directory empty")
                break
            print(os.listdir("folders/"+direct_name))
            while True:
                file_name = input("Please input file name(without file extention): ")
                #checks if the file exists
                test = os.path.exists("folders/"+direct_name+"/"+file_name+".txt")
                if test:
                    path = "folders/"+direct_name+"/"+file_name+".txt"
                    return(path)
                else:
                    print("File not found")
        else:
            #if its not found it while return an error
            print("Directory not found")

def action():
    #read - r
    #overwrite - w+
    #write - a+
    help = '''commands:
        - read: read the contents of the chosen file
        - overwrite: empty a file and write to it
        - write: add o a file
        '''
    while True:
        action_input = input("how would you like to edit it?: ")
        if action_input == "read":
            return "r"
        elif action_input == "overwrite":
            return "w+"
        elif action_input == "write":
            return "a+"
        elif action_input == "help":
            print(help)
        else:
            print("action unavailable, command 'help' is available")


def edit():
    path = checker()
    act = action()
    file = open(path, act)
    if act == "r":
        return(file.read())
    data = input("what would you like to write: ")
    file.write(data)
    read = input("would you like to read the file?(y/n): ")
    if read == "y":
        return(file.read())


