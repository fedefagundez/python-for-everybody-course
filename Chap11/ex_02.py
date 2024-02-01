import re
import math

fname = input('Enter file: ')

if len(fname) < 1:
    fname = 'mbox.txt'

try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()

regex = 'New Revision: (\d+)'

count = 0
sum = 0
for line in fhand:
    line = line.rstrip()
    if re.search(regex, line):
        count = count + 1
        number = re.findall(regex, line)[0]
        sum = sum + float(number)
        print(number)

average = sum / count

print(math.floor(average))
