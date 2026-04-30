a = 'A'
b = 'B'
c = 12.5

string = "a={nome1}  b={nome2} c={nome3:.2f} d={nome1}"
formato = string.format(
    nome1=a, nome2=b, nome3=c
    )

print(formato)