from random import randint

gameover = False
getal1 = int(input('Wat is het laagste getal waaruit de computer moet kiezen? '))
getal2 = int(input('Wat is het hoogste getal waaruit de computer moet kiezen? '))

while not gameover:
    computerGetal = randint(getal1, getal2)
    print(f'Computer denkt een getal tussen {getal1} en {getal2}: {computerGetal}')
    vraag = input('Heeft de computer het goed (g) of moet het hoger (h) of lager (l)? ')

    if vraag == "g" or vraag == "goed":
        print('De computer heeft gewonnen!')
        gameover = True

    elif vraag == "h" or vraag == "hoger":
        getal1 = computerGetal + 1

    elif vraag == "l" or vraag == "lager":
        getal2 = computerGetal - 1

    else:
        print('Dit is geen geldige invoer!')
