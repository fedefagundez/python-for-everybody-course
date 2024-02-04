import urllib.request

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
# The wb argument for open() opens a binary file for writing only. This program will work if the size of the file is less than the size of the memory of your computer.
fhand = open('cover3.jpg', 'wb')
fhand.write(img)
fhand.close()

# Code: https://www.py4e.com/code3/curl1.py
