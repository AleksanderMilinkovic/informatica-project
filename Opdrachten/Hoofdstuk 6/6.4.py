from random import randint

gameover = False
getalTeGroot = False
geraden = 0
controleGetal = 0

def getalKiezen():
    getal1 = int(input("Wat moet het laagste getal zijn waaruit de computer moet kiezen? "))
    getal2 = int(input("Wat moet het hoogste getal zijn waaruit de computer moet kiezen? "))
    while getal2 <= getal1:
        getal2 = int(input(f'Kies een hoger getal dan {getal1} '))
    return randint(getal1, getal2)

computerGetal = getalKiezen()

while not gameover:
    gebruikerGetal = int(input('Raad een getal: '))

    while gebruikerGetal <= controleGetal and getalTeGroot == False:
        gebruikerGetal = int(input(f'Je volgende poging moet groter zijn dan {controleGetal}! '))

    while gebruikerGetal >= controleGetal and getalTeGroot == True:
        gebruikerGetal = int(input(f'Je volgende poging moet kleiner zijn dan {controleGetal}! '))

    if computerGetal < gebruikerGetal:
        geraden += 1
        print('Het getal van de computer is kleiner!')
        print(f'Aantal keer geraden: {geraden}')
        controleGetal = gebruikerGetal
        getalTeGroot = True

    elif computerGetal > gebruikerGetal:
        geraden += 1
        print('Het getal van de computer is groter!')
        print(f'Aantal keer geraden: {geraden}')
        controleGetal = gebruikerGetal
        getalTeGroot = False

    else:
        geraden += 1
        print('Je hebt het geraden!')
        print(f'Geraden in: {geraden} keer')
        gameover = True

    if geraden >= 8 and gameover == False:
        print(f'Game over! Het getal was {computerGetal}')
        gameover = True