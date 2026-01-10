tekst = input('Welke tekst wil je verwerken? ')
sleutel = input('Wil je versleutelen (v) of ontsleutelen (o)? kies v of o: ')

verschuiving = 3 if sleutel == 'v' else -3
resultaat = ''

for letter in tekst:
    if letter.isalpha():
        if letter.islower():
            basis = ord('a')
        else:
            basis = ord('A')

        nieuwe_letter = chr((ord(letter) - basis + verschuiving) % 26 + basis)
        resultaat += nieuwe_letter
    else:
        resultaat += letter

print(f'Resultaat: {resultaat}')