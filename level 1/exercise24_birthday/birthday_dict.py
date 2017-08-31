# Excercise 24 : Bithday :: part 1 Birthday Dictionary

'''This exercise is Part 1 of 4 of the birthday data exercise series. The other exercises are: Part 2, Part 3, and Part 4.

For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based on their name. 
Create a dictionary (in your file) of names and birthdays. 
When you run your program it should ask the user to enter a name, and return the birthday of that person back to them. 
The interaction should look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.'''

Birthday_dict = {"Albert Einstein" : "1879-3-14", "Benjamin Franklin" : "1706-1-17", "Ada Lovelace" : "1815-12-10"}
print("Welcome to the birthday dictionary. We know the birthdays of:")
for keys in Birthday_dict:
    print(keys)
def look_up():
    name = input(">>> Who's birthday do you want to look up?")
    if name in Birthday_dict:
        print(Birthday_dict.get(name))
    else:
        print("Sorry, no recrods!")

if __name__ == "__main__":
    look_up()
