fhand = open('./mbox-short.txt')
count = 0
for line in fhand:
    if not line.startswith('From:'):
        continue
    print(line)
