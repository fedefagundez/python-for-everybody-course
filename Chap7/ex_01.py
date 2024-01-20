fname = input('Enter a file name: ')

try:
    fhand = open(fname)
except:
    print('File can not be opened: ', fname)
    exit()

for line in fhand:
    line = line.upper()
    line = line.strip()
    print(line)
