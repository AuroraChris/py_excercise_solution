# Exercise 19 : File Overlap

'''Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. 
One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any other number. 
And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. 
The explanation is easier with an example, which I will describe below.)

You’ll need to stitch together a few ideas of things I’ve previously talked about on this blog, 
so if you need a refresher in any of these topics, now is your chance! Of course, 
there are any number of ways to do this exercise, so these are only suggestions.
'''

def parser(filename):
    num_list = []
    with open(filename, "r") as f:
        num_lines = f.readlines()
        for p in num_lines:
            num = int(p.strip())
            num_list.append(num)
    return num_list

primes = parser("primes.txt")
luckynumbers = parser("luckynumbers.txt")
print([ele for ele in primes for ele2 in luckynumbers if ele == ele2])