# Excercise 24 : Birthday :: part 3 Birthday Month

'''This exercise is Part 3 of 4 of the birthday data exercise series. 
The other exercises are: Part 1, Part 2, and Part 4.

In the previous exercise we saved information about famous scientists’ names and birthdays to disk. 
In this exercise, load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month.

Your program should output something like:

{
	"May": 3,
	"November": 2,
	"December": 1
}'''
from datetime import datetime
from collections import Counter
import json

def get_date():
	d = {}
	with open("birthday.json", "r") as f:
		d = json.loads(f.read())
		for k in d:
			yield d[k]

def get_month(callback_gen):
	d_list = []
	try:
		while True:
			date = callback_gen.send(None)
			month = datetime.strptime(date, "%Y-%m-%d").month
			d_list.append(month)
	except StopIteration:
		return d_list

def count_month():
	l = get_month(get_date())
	return Counter(l)


if __name__ == "__main__":
	c = count_month()
	print(c)

#g = get_month()
#for i in g:
	#print(i)