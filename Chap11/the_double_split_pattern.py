import re

# The old way
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')

print('Traditional way: ', pieces[1])

# The fashion way
w = re.findall('@([^ ]*)', line)

print('The fashion way:', w)
