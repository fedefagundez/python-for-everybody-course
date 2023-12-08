def chop(t):
    del t[0]
    del t[len(t)-1]
    return None

list = [1, 2, 3, 4, 5]
print(list)
chop(list)

print('List:',list)