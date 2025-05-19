# paulina strunnikova - word position 4

import os

def show_working_directory():
    print("This is your current working directory:", os.getcwd())
    print("These are the contents of your directory:", os.listdir())

def get_valid_file_path():
        while True:
            path = input("Specify path to the text file (or type 'quit' to exit: ")
            if path # not found () == "quit":
                print("Goodbye!")
                exit()
            if os.path.isfile(path):
                print("Found it!")
                return path
            print("Couldn't find it, please try again.")
