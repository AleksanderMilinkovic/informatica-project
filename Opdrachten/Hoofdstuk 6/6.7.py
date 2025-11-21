import math

oliebollen = int(input('Hoeveel oliebollen wil je bakken? '))
recept = math.ceil(oliebollen / 20)
melk = 500 * recept

print(f'Je hebt ingrediënten nodig voor {20 * recept} oliebollen, anders kloppen de verhoudingen niet.\n')
print('Ingrediëntenlijst:')
print(f'Melk\nJe hebt {melk} ml melk nodig. In één verpakking zit 1000 ml melk.')
print(f'Je hebt {math.ceil(melk/1000)} pakken melk nodig.\n')

print(f'Gist\nJe hebt {recept} zakjes gist nodig. In één verpakking zitten 3 zakjes.')
print(f'Je hebt {math.ceil(recept/3)} verpakkingen gist nodig.\n')

print(f'Ei\nJe hebt {recept} stuks ei nodig. In één verpakking zitten 6 stuks.')
print(f'Je hebt {math.ceil(recept/3)} verpakkingen ei nodig.\n')

print(f'Bloem\nJe hebt {500 * recept} g bloem nodig. In één verpakking zit 500 g bloem.')
print(f'Je hebt {math.ceil(recept/3)} pakken bloem nodig.\n')
print('Suiker, zout en zonnebloemolie heb je al genoeg.')

"""
def ingrediënten(hoeveelheid, product):
"""