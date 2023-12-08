def middle(t):
    t = t[1:len(t)-1]
    return t

list = [1, 2, 3, 4, 5]
print(list)
newlist = middle(list)

print('List:',list)
print('New list:',newlist)