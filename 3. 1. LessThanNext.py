a = input(f'Type elements of your list:')
b = [int(symbol) for symbol in a.split(', ')]
c = []
for i, j in enumerate(b[:-1]):
    if j < b[i+1]:
        c.append(b[i+1])
print(f'List of elements which more than previous: {c}')
