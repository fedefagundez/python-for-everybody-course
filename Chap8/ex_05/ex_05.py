fname = input('Enter file: ')
fhand = open(fname)

count = 0
for line in fhand:
    if not line.startswith('From') or line.startswith('From:'): continue
    lineList = line.split()   
    email = lineList[1]  
    count = count + 1
    print(email)      

print('There were', count, 'lines in the file with From as the first word')           
