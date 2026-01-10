from math import ceil

streepjescode = str(input("Voer een streepjescode in: "))
lengtes = [8,12,13,14,17,18]

if len(streepjescode) not in lengtes:
    streepjescode = str(input('Geef een code op met een geldige lengte: '))
    exit()

som = 0
code_zonder_controle = streepjescode[:-1]
lengte = len(streepjescode)

for i, num in enumerate(code_zonder_controle):
    num = int(num)

    if lengte % 2 == 0:
        som += num * 3 if i % 2 == 0 else num
    else:
        som += num if i % 2 == 0 else num * 3

controlecijfer = (10 - som % 10) % 10

if int(streepjescode[-1]) == controlecijfer:
    print('Deze code is geldig!')
else:
    print('Deze streepjescode is niet correct')
