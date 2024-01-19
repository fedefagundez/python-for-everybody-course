str = 'X-DSPAM-Confidence: 0.8475'
i = str.find('0')
number = float(str[i:])

print('The number is:', end=" ")
print(number)
