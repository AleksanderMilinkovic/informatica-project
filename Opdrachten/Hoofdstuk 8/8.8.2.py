from appJar import gui
import random

def buttonKlik(name):
    global getal1, getal2

    antwoord = str(app.getEntry("Uitkomst"))
    antwoord = int(antwoord)

    if antwoord == getal1 * getal2:
      getal1 = random.randint(1, 10)
      getal2 = random.randint(1, 10)
      app.setLabel("Som", f'{getal1} * {getal2} = ?')
      app.setBg("green")
    else:
      app.setBg("red")

getal1 = random.randint(1,10)
getal2 = random.randint(1,10)

app = gui("Tafeltrainer", "400x200")

app.addLabel("Som", f'{getal1} * {getal2} = ?', 0, 1)
app.addLabelEntry("Uitkomst", 1, 1)
app.addButton("Controleer", buttonKlik, 2, 1)

app.go()
