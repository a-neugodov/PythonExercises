s = input(f'Type DNA sequence: ')
s_upper = s.upper()
s_reversed = s_upper[::-1]
def f(s_reversed):
    if len(s_reversed) <= 1000:
        print('Complement DNA: ')
        for i in s_reversed:
            if i == 'A':
                print('T', end = '')
            elif i == 'T':
                print('A', end = '')
            elif i == 'C':
                print('G', end = '')
            elif i == 'G':
                print('C', end = '')
    else:
        print ('DNA sequence shoud not contain more then 1000 nk!')
f(s_reversed)
