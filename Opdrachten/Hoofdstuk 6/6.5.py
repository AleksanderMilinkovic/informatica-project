from random import randint

gameover = False
getal1 = int(input('Wat is het laagste getal waaruit de computer moet kiezen? '))
getal2 = int(input('Wat is het hoogste getal waaruit de computer moet kiezen? '))

while not gameover:
    computerGetal = randint(getal1, getal2)
    print(f'Computer denkt {computerGetal}')
    vraag = input('Is het goed (g) of moet de computer hoger (h) of lager (l)? ')

    if vraag == "g":
        print('De computer heeft gewonnen!')
        gameover = True

    elif vraag == "h":
        print(f'De computer gaat nu een getal hoger dan {computerGetal} gokken')
        getal1 = computerGetal + 1

    elif vraag == "l":
        print(f'De computer gaat nu een getal lager dan {computerGetal} gokken')
        getal2 = computerGetal - 1

    else:
        print('Dit is geen geldige invoer!')
