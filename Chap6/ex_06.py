# Read the documentation of the string methods at

# https://docs.python.org/3.5/library/...string-methods

# You might want to experiment with some of them to make sure you understand how they work. strip and replace are particularly useful.

str = '    Esto es una string     '
new_str = str.strip()
print(str)
print(new_str)

url = 'https://docs.python.org/3.5/library/...string-methods'
new_url = url.strip('/string-meh:.ps')
print(url)
print(new_url)

str_2 = 'Estaba el ratón persiguiendo al ratón.'
replace = 'gato'
new_str2 = str_2.replace('ratón', 'gato', 1)
print(new_str2)
