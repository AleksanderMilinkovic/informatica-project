verbodenScore = [23, 29, 31, 35, 37, 41, 43, 44, 46, 47, 49, 52, 53, 55, 56, 58, 59]
gameover = False
beurt = 1
punten = 501

def vraagScore(pijl):
    score = int(input(f'Score van pijl {pijl}: '))
    while score in verbodenScore or score > 60:
        score = int(input('Dat is geen geldige score! Voor een geldige score in: '))
    return score

while not gameover:
    print(f'Beurt {beurt}')
    print(f'Punten: {punten}\n')

    pijl1 = vraagScore(1)
    pijl2 = vraagScore(2)
    pijl3 = vraagScore(3)

    if pijl1 + pijl2 + pijl3 < punten:
        punten = punten - pijl1 - pijl2 - pijl3
    elif pijl1 + pijl2 + pijl3 == punten:
        if beurt == 3:
            print('Je hebt een 9-darter!')
        else:
            print('Yes, uit!')
        gameover = True
    else:
        print(f'Score is nu {punten - pijl1 - pijl2 - pijl3}, dus deze beurt telt niet!')
    beurt += 1
