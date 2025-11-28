import math

oliebollen = int(input('Hoeveel oliebollen wil je bakken? '))
recept = math.ceil(oliebollen / 20)
melkHoeveelheid = 500 * recept
melkPakken = math.ceil(melkHoeveelheid/1000)
eierDozen = math.ceil(recept/3)

def ingredienten(product, hoeveelheid, hoeveelheid2):
    if product == "melk":
        if hoeveelheid2 == 1:
            return f'Je hebt {hoeveelheid} ml melk nodig. In één verpakking zit 1000 ml melk.\nJe hebt 1 pak melk nodig.'
        else:
            return f'Je hebt {hoeveelheid} ml melk nodig. In één verpakking zit 1000 ml melk.\nJe hebt {hoeveelheid2} pakken melk nodig.'

    elif product == "gist":
        if hoeveelheid1 == 1:
            return f'Je hebt 1 zakje gist nodig. In één pak zitten 3 zakjes.\nJe hebt 1 pak gist nodig.'
        elif hoeveelheid2 == 1:
            return f'Je hebt {recept} zakjes gist nodig. In één pak zitten 3 zakjes.\nJe hebt 1 pak gist nodig.'
        else:
            return f'Je hebt {hoeveelheid} zakjes gist nodig. In één pak zitten 3 zakjes.\nJe hebt {hoeveelheid2} pakken gist nodig.'

    elif product == "ei":
        if hoeveelheid2 == 1:
            return f'Je hebt {hoeveelheid} stuks ei nodig. In één doos zitten 6 eieren.\nJe hebt 1 doos eieren nodig.'
        else:
            return f'Je hebt {hoeveelheid} stuks ei nodig. In één doos zitten 6 eieren.\nJe hebt {hoeveelheid2} eierdozen nodig.'

    elif product == "bloem":
        if hoeveelheid2 == 1:
            return f'Je hebt {hoeveelheid} g bloem nodig. In één pak zit 500 g.\nJe hebt precies genoeg aan 1 pak bloem!'
        else:
            return f'Je hebt {hoeveelheid} g bloem nodig. In één pak zit 500 g.\nJe hebt precies genoeg aan {hoeveelheid2} pakken bloem!'

    else:
        return "Skibidi toilet ):"


print(f'Je hebt ingrediënten nodig voor {20 * recept} oliebollen, anders kloppen de verhoudingen niet.\n')
print('Ingrediëntenlijst:')
print(f'Melk')
print(f'{ingredienten("melk", melkHoeveelheid, melkPakken)}\n')

print(f'Gist')
print(f'{ingredienten("ei", recept, eierDozen)}\n')

print(f'Bloem')
print(f'{ingredienten("bloem", (recept * 500), recept)}\n')
print('Suiker, zout en zonnebloemolie heb je al genoeg.')
