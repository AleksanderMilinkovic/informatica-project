from appjar import gui
from random import randint

app = gui("Hoger/lager")

def buttonKlik(name):
    global computerGetal
    gameover = False
    geraden = 0

    if name == "Raden":
        while not gameover:
            gebruikersGetal = int(str(app.getEntry("Raden")))
            geraden += 1
            if computerGetal < gebruikersGetal:
                app.setLabel("Status", "Het getal van de computer is kleiner")
                app.setImage("Hangman", f'hangman{geraden}.png')
            elif computerGetal > gebruikersGetal:
                app.setLabel("Status", "Het getal van de computer is groter")
                app.setImage("Hangman", f'hangman{geraden}.png')
            else:
                app.setLabel("Status", "Je hebt het getal geraden!")
                gameover = True

            if geraden >= 8 and gameover == False:
                print(f'Game over! Het getal was {computerGetal}')
                gameover = True

    elif name == "Reset":
        app.stop()


computerGetal = random.randint(1, 100)
app.addLabel("Titel", "Raad het getal tussen 0 en 100!", 0, 2)
app.addLabel("Status", "", 1, 1)
app.addEntry("invoer", 2, 0)
app.addButtons(["Raden", "Reset"], buttonKlik, 3, 1)
app.addImage("Hangman", "hangman0.gif")

app.go()