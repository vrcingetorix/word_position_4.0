# paulina strunnikova - code from word position 1 and 2

import os
# TODO: The program should help the user by first printing out the current working directory
print(os.getcwd())
# TODO: and a list of the contents of that directory, to help the user enter in a proper path to a file.
print(os.listdir())
# open a file and read the contents
with open("spam_song.txt") as file_connection:
    file_contents = file_connection.read()
# print contents
print(file_contents)
# TODO: The program should calculate the position of a specific string in a file.

(file_contents.find("Shut up!! Baked beans are off."))
file_contents.count("Shut up!! Baked beans are off.")
len("Shut up!! Baked beans are off.")

# TODO: The position should be expressed as a percent. For example, “the word was found at the point
# 10.4% of the way through the file.”

position = (file_contents.find("Shut up!! Baked beans are off."))

percent = position/len(file_contents)*100

print("The string was found at this point:", (percent))
# TODO: The program should ask the user to specify the path to the file to be searched.


path_to_txtfile = input("Specify path to spam song: ")

# TODO: The program should ask the user to specify the word to be located.



specific_string = input("Specify the word to be located: ")

file_contents.find(specific_string)

print(str(specific_string))

# TODO: All user input should be provided interactively at the terminal, not by modifying the program.

# TODO: The program should also print out this same results message to a file called “wordposition_results.txt”

with open("wordposition_results.txt", mode = "a") as write_connection:
    write_connection.write(file_contents)

# 9. In WP 1.0, if the user made a mistake when entering the path of the file to search, the program
# would stop with an error. In this version, the program should respond to this kind of mistake by
# giving the user a helpful message and giving them another chance to provide a valid path.

path_to_txtfile = input("Specify path to spam song: ")
if os.path.isfile(path_to_txtfile):
    with open(path_to_txtfile, 'r') as file_connection:
        file_contents = file_connection.read()
    print("Found it!")
else:
    print("This path does not seem to work, please try again: ")


if os.path.isfile(path_to_txtfile):
        with open(path_to_txtfile, 'r') as file_connection:
            file_contents = file_connection.read()
        print("Found it!")

# 10. The output message printed to the terminal should be modified, so that it only says which quarter
# of the file the target string occurred in. For example: “The string <STRING> was found in the
# <first/second/third/fourth> quarter of the file <FILEPATH>.”

quarter_position = len(file_contents)/4

if position < quarter_position:
    quarter_option = "first"
elif position < quarter_position * 2:
    quarter_option = "second"
elif position < quarter_position * 3:
    quarter_option = "third"
else:
    quarter_option = "fourth"

if position == -1:
    print("The string was not found.")
else:
    print("This is what quarter the string was found in:", (quarter_option))

# 16. Instead of searching for a single word, the program should allow the user to enter in multiple
# words/strings, and results should be provided for each word/string provided. This includes both
# the printed results and the results written to the output file. (Side note: this feature is ambiguous
# on how the words/phrases should be entered. They could be entered one at a time or maybe all
# at once; that’s up to your design.)



multiple_string_input = str(input("List the string you would like to locate: "))


# final vers

while True:
    with open("spam_song.txt", "r") as file:
        file_contents = file.read()
    multiple_string_input = input("List the string you would like to locate. If you would not like to locate a string, hit enter: ")
    if multiple_string_input == "":
        break
    if multiple_string_input in file_contents:
        print(f"The string {multiple_string_input} was found in the file.")
        result = f"The string {multiple_string_input} was found in the file.\n"
    else:
        print(f"The string '{multiple_string_input}' was not found in the file.")
        result = f"The string '{multiple_string_input}' was not found in the file.\n"
    with open("wordposition_results.txt", mode = "a") as write_connection:
        write_connection.write(result)

# 17. In Feature 9 of WP 2.0, the user was given one additional attempt to enter a correct file path. In
# this version, the program should continue asking for a valid path until either a) the user provides
# a valid path, or b) the user opts to quit the program. (Tip: this means providing a valid directory
# path if you are implementing Feature 15, or a valid file path otherwise.)

folder_contents = os.listdir()

print(folder_contents)

while True:
    path_to_txtfile = input("Specify path to spam song: ")
    if os.path.isfile(path_to_txtfile):
        with open(path_to_txtfile) as file_connection:
            file_contents = file_connection.read()
        print("Found it!")
        break
    else:
        print("Couldn't find it, please try again: ")

