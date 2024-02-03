import re

fhand = open('./regex_sum_1791085.txt')

regex = '\d+'

sum = 0
for line in fhand:
    line = line.rstrip()
    numbers = re.findall(regex, line)
    if len(numbers) > 0:
        for number in numbers:
            sum = sum + int(number)

print(sum)
