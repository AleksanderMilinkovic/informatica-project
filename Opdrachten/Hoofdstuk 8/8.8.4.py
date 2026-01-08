from appJar import gui
import random
import string

def btnClick(name):
    a = int(str(app.getOptionBox("lengte")))
    tekens = ""
    wachtwoord = ""

    if app.getCheckBox("Kleine letters"):
        tekens += string.ascii_lowercase
    if app.getCheckBox("Hoofdletters"):
        tekens += string.ascii_uppercase
    if app.getCheckBox("Cijfers"):
        tekens += string.digits
    if app.getCheckBox("Tekens"):
        tekens += string.punctuation

    for i in range(a):
        wachtwoord += random.choice(tekens)

    app.setEntry("wachtwoord", wachtwoord)


app = gui("Wachtwoordgenerator", "400x300")
app.addLabel("titel", "Wachtwoordgenerator", 0, 0, 2)
app.addEntry("wachtwoord", 1, 0, 2)
app.addOptionBox("lengte", ["4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32"], 2, 0)
app.addCheckBox("Kleine letters", 2, 1, 0)
app.addCheckBox("Hoofdletters", 3, 1, 0)
app.addCheckBox("Cijfers", 4, 1, 0)
app.addCheckBox("Tekens", 5, 1, 0)
app.addButton("Genereren", btnClick, 4, 0, 1)
app.go()