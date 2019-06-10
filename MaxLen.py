import re
a = input(f'Type your phrase: ')
c = re.findall(r"[\w']+", a)
d = len(max(c))
print(f'Max-length word: {max(c)}')
print(f'Length: {d}')
