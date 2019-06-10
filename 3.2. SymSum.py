a = input(f'Type your number: ')
c = []
b = []
for symbol in a:
    c.append(int(symbol))
    b.append(int(symbol))
    for i, j in enumerate(c[:-1]):
        if i < len(c):
            c[i+1] = j * c[i+1]
    for x, z in enumerate(b[:-1]):
        if x < len(b):
            b[x+1] = z + b[x+1]
print(f'Multiplication result: {c[i+1]}')
print(f'Addition result: {b[x+1]}')
