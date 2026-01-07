from appJar import gui
import random
import string

def buttonKlik(name):
  letter = random.choice(string.ascii_uppercase)
  letter2 = random.choice(string.ascii_uppercase)
  app.setLabel("Postcode", f'{random.randint(1000, 9999)} {letter}{letter2}')

app = gui("Postcode", "400x200")
app.setLabelFont(size=28)
app.addButton("Kies willekeurige postcode!", buttonKlik, 2, 2)
app.addLabel("Postcode", "", 1, 2)

app.go()