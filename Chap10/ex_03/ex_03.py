import string 

file = input('Enter file name:')

try:
    handle = open(file)
except:
    print('File cannot be opened:', file)
    quit()

count = dict()
for line in handle:
    for letter in line:
        if not letter in string.punctuation and not letter is ' ' and not letter is '\n':
            letter = letter.lower()
            count[letter] = count.get(letter, 0) + 1

print(count)