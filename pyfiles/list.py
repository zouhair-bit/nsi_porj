import os

def list():
    while True:
            print(os.listdir("folders")) 
            direct_name = input("Please input directory name that you need to list:")
            try:
                directory = os.listdir("folders/"+direct_name)
                return(directory)
            except FileNotFoundError:
                print("directory not found")