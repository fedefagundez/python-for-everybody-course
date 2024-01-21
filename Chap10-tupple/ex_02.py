name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hours = dict()
for line in handle:
    if not line.startswith('From '):
        continue
    splited = line.split()
    splited_hour = splited[5].split(':')

    hours[splited_hour[0]] = hours.get(splited_hour[0], 0) + 1

for h, c in sorted(hours.items()):
    print(h, c)
