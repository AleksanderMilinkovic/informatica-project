def kleurNaarGrijs(hexadecimaalGetal):
    r = hexadecimaalGetal[0:2]
    g = hexadecimaalGetal[2:4]
    b = hexadecimaalGetal[4:6]

    R = int(r, 16)
    G = int(g, 16)
    B = int(b, 16)
    decimaleGrijswaarde = int((R + G + B) / 3)
    hexadecimaleGrijswaarde = hex(decimaleGrijswaarde)

    return hexadecimaleGrijswaarde[2:]


kleurwaarde = input("Geef een hexadecimale waarde van een kleur: ")
while len(kleurwaarde) != 6:
    kleurwaarde = input("Voer een waarde in van 6 tekens: ")

grijswaarde = kleurNaarGrijs(kleurwaarde)
print(f'De grijswaarde is: {grijswaarde}{grijswaarde}{grijswaarde}')
