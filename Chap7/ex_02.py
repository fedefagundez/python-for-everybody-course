fname = input('Enter a file name:')

try:
    fhand = open(fname)
except:
    print('File can not be open: ', fname)
    exit()

count = 0
totalconf = 0
confidence = 0
for line in fhand:
    if line.find('X-DSPAM-Confidence') == -1:
        continue
    count = count + 1
    confidence = float(line[line.find('0'):])
    totalconf = confidence + totalconf

print('Average spam confidence: ', totalconf/count)
