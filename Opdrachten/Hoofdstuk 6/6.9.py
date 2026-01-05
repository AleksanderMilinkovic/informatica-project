import math

invoer = int(input("Geef een getal kleiner dan 256: "))
while invoer >= 256 or invoer < 0:
    invoer = int(input("Geef een getal kleiner dan 256: "))

def decNaarHex(decimaal):
    if decimaal == 0:
        return 0
    else:
        a = math.floor(decimaal / 16)
        if a < 10:
            A = a
        elif a == 10:
            A = "A"
        elif a == 11:
            A = "B"
        elif a == 12:
            A = "C"
        elif a == 13:
            A = "D"
        elif a == 14:
            A = "E"
        elif a == 15:
            A = "F"

        b = decimaal % 16
        if b < 10:
            B = b
        elif b == 10:
            B = "A"
        elif b == 11:
            B = "B"
        elif b == 12:
            B = "C"
        elif b == 13:
            B = "D"
        elif b == 14:
            B = "E"
        elif b == 15:
            B = "F"

        return str(A) + str(B)


print(decNaarHex(invoer))
