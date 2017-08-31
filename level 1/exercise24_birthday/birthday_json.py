# Excercise 24 : Birthday :: part 2 Birthday JSON

'''This exercise is Part 2 of 4 of the birthday data exercise series. 
The other exercises are: Part 1, Part 3, and Part 4.

In the previous exercise we created a dictionary of famous scientists’ birthdays. 
In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program.

Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you have on disk with the scientist’s name. 
If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.'''

import json
import birthday_dict

d = birthday_dict.Birthday_dict

def dump_to_file():
    with open("birthday.json", "w") as f:
        f.write(json.dumps(d))
def ask_for_recording():
    ipt = input("Do you want to add some new records y/n (default is no)?")
    if ipt == "y":
        name = input("Please enter a name : ")
        date = input("Please enter a date : ")
        if name not in d:
            d[name] = date

if __name__ == "__main__":
    ask_for_recording()
    dump_to_file()