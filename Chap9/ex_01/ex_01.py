handle = open('words.txt')

words = dict()
for line in handle:
    lineList = line.split()
    for word in lineList:
        words[word] = None

print('these' in words)