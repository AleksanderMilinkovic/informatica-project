"""
Verboden scores:
23, 29, 31, 35, 37, 41, 43, 44, 46, 47, 49, 52, 53, 55, 56, 58, 59, >60
"""
beurt = 1
punten = 501

def vraagScore(pijl):
    score = int(input(f'Score van pijl {pijl}: '))
    return score

while not gameover:
    print(f'Beurt {beurt}')
    print(f'Punten: {punten}\n')

    pijl1 = vraagScore(1)
    pijl2 = vraagScore(2)
    pijl3 = vraagScore(3)
    beurt += 1

    if pijl1 + pijl2 + pijl3 <= punten:
        punten = punten - pijl1 - pijl2 - pijl3
    else:
        print(f'Score is nu {punten - pijl1 - pijl2 - pijl3}, dus deze beurt telt niet!')

