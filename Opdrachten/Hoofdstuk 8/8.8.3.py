from appJar import gui
import random

app = gui("Hoger/lager", "600x400")
gameover = False
geraden = 0

def buttonKlik(name):
    global computerGetal, gameover, geraden

    if name == "Raden":
        if not gameover:
            gebruikersGetal = int(str(app.getEntry("Invoer")))
            geraden += 1
            afbeelding = f'hangman{geraden}.gif'
            
            if computerGetal < gebruikersGetal:
                app.setLabel("Status", "Het getal van de computer is kleiner")
                app.setImage("Hangman", afbeelding)
                app.clearEntry("Invoer")
            elif computerGetal > gebruikersGetal:
                app.setLabel("Status", "Het getal van de computer is groter")
                app.setImage("Hangman", afbeelding)
                app.clearEntry("Invoer")
            else:
                app.setLabel("Status", "Je hebt het getal geraden!")
                gameover = True

            if geraden >= 9 and not gameover:
                app.setLabel("Status", f'Game over! Het getal was {computerGetal}')
                gameover = True

    elif name == "Reset":
        app.setLabel("Status", "")
        app.setImage("Hangman", "hangman0.gif")
        app.clearEntry("Invoer")
        computerGetal = random.randint(1, 100)
        gameover = False
        geraden = 0


computerGetal = random.randint(1, 100)
app.addLabel("Titel", "Raad het getal tussen 0 en 100!", 0, 0)
app.addLabel("Status", "", 1, 0)
app.addEntry("Invoer", 2, 0)
app.addButtons(["Raden", "Reset"], buttonKlik, 5, 0)
app.addImage("Hangman", "hangman0.gif", 2, 2)

app.go()