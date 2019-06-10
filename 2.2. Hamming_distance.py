s = input(f'Type 1st sequence: ')
t = input(f'Type 2nd sequence: ')
s_upper = s.upper()
t_upper = t.upper()
def f(s_upper, t_upper):
    if len(s_upper) == len(t_upper):
        return sum(i != j for i,j in zip(s_upper, t_upper))
    else:
        print ('DNA sequences shoud have equal length!')
print(f(s_upper, t_upper))
