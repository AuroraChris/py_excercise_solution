# Exercise 14 : Decode a Webpage

'''This is the first 4-chili exercise of this blog!
We’ll see what people think, and decide whether or not to continue with 4-chili exercises in the future.
 
Concepts for this week:

requests
BeautifulSoup
'''

# Scrapy : See in my scrapy project

# built with requests and beautiful-soup

import requests
from bs4 import BeautifulSoup
r = requests.get("https://www.nytimes.com/")
html = r.text
soup = BeautifulSoup(html)
print(soup.find_all("h2", class_= "story-heading"))