fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File can not be opened: ', fname)
    exit()


count = 0
for line in fhand:
    if line.startswith('Subject:'):
        line = line.strip()
        count = count + 1
        print(line)
print('There were', count, 'subject lines in', fname)
