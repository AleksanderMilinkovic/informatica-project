print('De ABC-formule!')

a = int(input('Welke waarde heeft a? '))
b = int(input('Welke waarde heeft b? '))
c = int(input('Welke waarde heeft c? '))
D = b**2 - 4*a*c

print(f'D: {D}')
print(f'x1: {-b+D**0.5/2*a}')
print(f'x2: {(-b-D**0.5)/(2*a)}')