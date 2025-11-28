def decimaalNaarBinair(getal):
    if getal >= 128:
        binair = str(1)
        getal -= 128
    else:
        binair = str(0)

    if getal >= 64:
        binair += str(1)
        getal -= 64
    else:
        binair += str(0)

    if getal >= 32:
        binair += str(1)
        getal -= 32
    else:
        binair += str(0)

    if getal >= 16:
        binair += str(1)
        getal -= 16
    else:
        binair += str(0)

    if getal >= 8:
        binair += str(1)
        getal -= 8
    else:
        binair += str(0)

    if getal >= 4:
        binair += str(1)
        getal -= 4
    else:
        binair += str(0)

    if getal >= 2:
        binair += str(1)
        getal -= 2
    else:
        binair += str(0)

    if getal >= 1:
        binair += str(1)
        getal -= 1
    else:
        binair += str(0)

    return binair

decimaal = int(input("Geef een decimaal getal < 256: "))
while decimaal > 255 or decimaal <= 0:
    decimaal = int(input('Voer een geldig getal in! '))
print(f'Het decimale getal {decimaal} is binair: {decimaalNaarBinair(decimaal)}')