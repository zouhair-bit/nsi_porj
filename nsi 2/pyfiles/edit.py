import os
def checker():
    while True:
        print(os.listdir("folders"))
        direct_name = input("Please input directory name: ")
        #the test variable is used to test for the existence of a directory
        test = os.path.exists("folders/"+direct_name)
        # if dir exists now ask for file
        if test:
            lister= os.listdir("folders/"+direct_name)
            #checks if the directory is empty because there wont be any files to edit
            if lister == []:
                print("directory empty")
                break
            #lists alll the files in that dir to help the user
            print(lister)
            #and if the dir isnt empty we will ask for the file inside of it
            while True:
                file_name = input("Please input file name(without file extention): ")
                #checks if the file exists
                test = os.path.exists("folders/"+direct_name+"/"+file_name+".txt")
                if test:
                    #we add the directory name and file name to make a complete path and return it to the edit function 
                    #to open the chosen file
                    path = "folders/"+direct_name+"/"+file_name+".txt"
                    return(path)
                else:#if the file isnt found, we ask again
                    print("File not found")
        else:
            #if directory isnt found, we ask again
            print("Directory not found")

def action():
    help = '''commands:
        - read: read the contents of the chosen file
        - overwrite: empty a file and write to it
        - write: add o a file
        '''
    while True:
        #read - r
        #overwrite - w+
        #write - a+
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
    #we use 2 fuinction to get the variables needed to open a file
    path = checker()
    act = action()
    file = open(path, act)
    # we just need to read we wont be writing to the file
    if act == "r":
        print(file.read())
    else:
        data = input("what would you like to write: ")
        file.write(data)
    file.close()

