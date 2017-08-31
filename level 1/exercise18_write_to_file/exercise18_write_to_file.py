# Exercise 18 : Write To A File

'''Take the code from the How To Decode A Website exercise 
(if you didn’t do it or just want to play with some different code, use the code from the solution), 
and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.

Extras:

Ask the user to specify the name of the output file that will be saved.
'''

from bs4 import BeautifulSoup
import requests

response = requests.get("http://quotes.toscrape.com")
html = response.text
name = input("Please edit the name of file : ")
with open(name+".txt", "wb") as f:
    f.write(html.encode("utf-8"))