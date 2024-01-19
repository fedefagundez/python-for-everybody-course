fout = open('output.txt', 'w')
print(fout)

line1 = 'Estoy probando la funcionalidad de escribir un archivo,\n'
nbrlines = fout.write(line1)

fout.close()

print(nbrlines, 'characters has been writen on the text file.')
