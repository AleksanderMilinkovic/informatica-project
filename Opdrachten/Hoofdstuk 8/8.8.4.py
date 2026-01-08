from appJar import gui
import random
import string

getallen = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]

def btnClick(name):
    a = app.getOptionBox("lengte")
    for i in range(a):
        wachtwoord = ""

        b = random.randint(1,4)
        if b == 1:
            wachtwoord += random.choice(string.ascii_lowercase)
        elif b == 2:
            wachtwoord += random.choice(string.ascii_uppercase)
        elif b == 3:
            wachtwoord += random.choice(string.digits)
        elif b == 4:
            wachtwoord += random.choice(string.punctuation)

app = gui("Wachtwoordgenerator", "300x300")
app.addLabel("titel", "Wachtwoordgenerator")
app.addEntry("wachtwoord", "")
app.addButton("Genereren", btnClick)
app.addCheckBox("Kleine letters")
app.addCheckBox("Hoofdletters")
app.addCheckBox("Cijfers")
app.addCheckBox("Tekens")
app.addLabelOptionBox("lengte", getallen)