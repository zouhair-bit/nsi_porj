import os

def list():
    while True:
        #the directory 'folders' is where all directories and files will be located
        # we print whats in the folders dir to help the user
            print(os.listdir("folders")) 
            direct_name = input("Please input directory name that you need to list:")
            try:
                directory = os.listdir("folders/"+direct_name)
                return(directory)
            #when the folder isn't found, we ask again
            except FileNotFoundError:
                print("directory not found")
                
                