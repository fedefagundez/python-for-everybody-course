import re
hand = open('./mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:  # if stuff has only one value
        continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum: ', max(numlist))
