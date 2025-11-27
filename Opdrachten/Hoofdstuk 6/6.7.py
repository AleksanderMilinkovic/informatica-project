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
        if hoeveelheid2 == 1:
            return f'Je hebt {hoeveelheid} zakjes gist nodig. In één verpakking zitten 3 zakjes.\nJe hebt 1 pak gist nodig.'
        else:
            return f'Je hebt {hoeveelheid} zakjes gist nodig. In één verpakking zitten 3 zakjes.\nJe hebt {hoeveelheid2} pakken gist nodig.'

    elif product == "ei":
        if hoeveelheid2 == 1:
            return f'Je hebt {hoeveelheid} stuks ei nodig. In één doos zitten 6 eieren.\nJe hebt 1 doos eieren nodig.'
        else:
            return f'Je hebt {hoeveelheid} stuks ei nodig. In één doos zitten 6 eieren. \nJe hebt {hoeveelheid2} eierdozen nodig.'

    else:
        return "Skibidi toilet ):"


print(f'Je hebt ingrediënten nodig voor {20 * recept} oliebollen, anders kloppen de verhoudingen niet.\n')
print('Ingrediëntenlijst:')
print(f'Melk\n')
print(ingredienten(melk, melkHoeveelheid, melkPakken))

print(f'Gist\n')
print(ingredienten(ei, recept, eierDozen))

print(f'Bloem\nJe hebt {500 * recept} g bloem nodig. In één verpakking zit 500 g bloem.')
print(f'Je hebt {math.ceil(recept/3)} pakken bloem nodig.\n')
print('Suiker, zout en zonnebloemolie heb je al genoeg.')
