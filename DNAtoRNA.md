# [Transcribing DNA into RNA](http://rosalind.info/problems/rna)
def f(t):
    if len(t) <= 1000:
        u = t.replace('T','U')
        print(f'RNA sequence: {u}')
    else:
        print ('DNA sequence shoud not contain more then 1000 nk!')
f(input(f'Type DNA sequence: '))
