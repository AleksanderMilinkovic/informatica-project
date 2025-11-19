from random import randint

def getalKiezen():
    getal1 = int(input("Wat moet het laagste getal zijn waaruit de computer moet kiezen? "))
    getal2 = int(input("Wat moet het hoogste getal zijn waaruit de computer moet kiezen? "))
    while getal2 <= getal1:
        getal2 = int(input(f'Kies een hoger getal dan {getal1} '))
    return randint(getal1, getal2)

computerGetal = getalKiezen()
gameover = False
geraden = 0

while not gameover:
    gebruikerGetal = int(input('Raad een getal: '))

    if computerGetal < gebruikerGetal:
        geraden += 1
        print('Het getal van de computer is kleiner!')
        print(f'Aantal keer geraden: {geraden}')

    elif computerGetal > gebruikerGetal:
        geraden += 1
        print('Het getal van de computer is groter!')
        print(f'Aantal keer geraden: {geraden}')

    else:
        geraden += 1
        print('Je hebt het geraden!')
        print(f'Geraden in: {geraden} keer')
        gameover = True

    if geraden >= 8 and gameover == False:
        print('Game over')
        gameover = True