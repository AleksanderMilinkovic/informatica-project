print('De ABC-formule!')

a = float(input('Welke waarde heeft a? '))
b = float(input('Welke waarde heeft b? '))
c = float(input('Welke waarde heeft c? '))
D = b**2 - 4*a*c

print(f'D = {D}')
if D < 0:
    print("Deze vergelijking heeft geen oplossingen!")
elif D == 0:
    x = -b/(2*a)
    print(f'x = {x}')
else:
    x1 = round((-b - D**0.5) / (2*a), 2)
    x2 = round((-b + D**0.5) / (2*a), 2)
    print(f'x = {x1} V x = {x2}')