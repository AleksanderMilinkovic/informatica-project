from appJar import gui
app = gui("Demonstratie", "400x200")
app.go()
"""
Vereisten: Een Python-programma dat:
- werkt met een finite state machine (FSM) oftewel een eindige automaat;
- gebruikersinteracties simuleert via input en foutmeldingen;
- een voorraad beheert; - geldinvoer verwerkt en foutafhandeling toepast;
- logging en statistische analyse uitvoert na simulatie met meerdere gebruikers.

Opdracht A: snackautomaat
4 producten
Gebruiker kiest product, voert geld in
Controle, wisselgeld, voorraad aanpassen
20 willekeurige klanten simuleren
Overzicht: aantal verkopen per product, omzet en fouten

import random
from appJar import gui

# Producten en prijzen
producten = {
    "Chips": {"prijs": 1.5, "voorraad": 5},
    "Candy": {"prijs": 1.0, "voorraad": 5},
    "Frisdrank": {"prijs": 2.0, "voorraad": 5},
    "Chocolade": {"prijs": 2.5, "voorraad": 5}
}

# Verkoop- en foutstatistieken
verkopen = {product: 0 for product in producten}
omzet = 0
fouten = []

# FSM states
class FSM:
    def __init__(self):
        self.state = "Wachten op betaling"
    
    def process(self, product, betaalbedrag):
        global omzet
        global fouten
        
        if self.state == "Wachten op betaling":
            if product not in producten:
                fouten.append(f"Product {product} bestaat niet.")
                self.state = "Fout"
            else:
                prijs = producten[product]["prijs"]
                if producten[product]["voorraad"] == 0:
                    fouten.append(f"{product} is uitverkocht.")
                    self.state = "Fout"
                elif betaalbedrag < prijs:
                    fouten.append(f"Te weinig betaald voor {product}.")
                    self.state = "Fout"
                else:
                    producten[product]["voorraad"] -= 1
                    verkopen[product] += 1
                    omzet += prijs
                    self.state = "Product geleverd"
                    
        if self.state == "Product geleverd":
            return f"Product {product} geleverd!"
        
        if self.state == "Fout":
            return f"Er is een fout opgetreden."

# Simulatie van 20 klanten
def simuleer_automaat():
    global omzet, verkopen, fouten
    klanten = 20
    fsm = FSM()
    
    for klant in range(klanten):
        product = random.choice(list(producten.keys()))
        betaalbedrag = random.uniform(0.5, 3.0)  # Klant betaalt tussen 0.5 en 3.0
        resultaat = fsm.process(product, betaalbedrag)
        
        if "Product geleverd" in resultaat:
            print(f"Klant {klant + 1}: {resultaat} Betaling: {betaalbedrag:.2f} EUR")
        else:
            print(f"Klant {klant + 1}: {resultaat} Betaling: {betaalbedrag:.2f} EUR")

    print("\nVerkoopstatistieken:")
    for product, aantal in verkopen.items():
        print(f"{product}: {aantal} verkocht")
    print(f"Totaal omzet: {omzet:.2f} EUR")
    
    if fouten:
        print("\nFouten:")
        for fout in fouten:
            print(fout)

# GUI met appJar
def update_gui():
    simuleer_automaat()
    
    app.clear()
    
    app.addLabel("header", "Snackautomaat Simulatie")
    
    app.addLabel("omzet", f"Totale Omzet: {omzet:.2f} EUR")
    
    for product, aantal in verkopen.items():
        app.addLabel(f"{product}_verkocht", f"{product}: {aantal} verkocht")
    
    if fouten:
        app.addLabel("fouten", "Fouten:")
        for i, fout in enumerate(fouten):
            app.addLabel(f"fout_{i}", fout)

# Start GUI
app = gui("Snackautomaat Simulatie", "400x400")
app.addButton("Simuleer Verkoop", update_gui)

app.go()
"""