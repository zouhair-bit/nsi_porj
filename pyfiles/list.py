import os

def list():
    while True:
            direct_name = input("Please input directory name that you need to list:")
            if direct_name == "self":
                directory = os.listdir("folders")
                return(directory)
            try:
                directory = os.listdir("folders/"+direct_name)
                return(directory)
            except FileNotFoundError:
                print("directory not found")