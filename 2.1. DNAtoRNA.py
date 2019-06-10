t = input(f'Type DNA sequence: ')
t_upper = t.upper()
def f(t_upper):
    if len(t_upper) <= 1000:
        u = t_upper.replace('T','U')
        print(f'RNA sequence: {u}')
    else:
        print ('DNA sequence shoud not contain more then 1000 nk!')
f(t_upper)
