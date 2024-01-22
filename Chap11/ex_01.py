import re

regex = input('Enter a regular expression: ')

fhand = open('./mbox.txt')
count = 0
for line in fhand:
    if re.search(regex, line):
        count = count + 1

print('mbox.txt had %d lines that matched %s' % (count, regex))
