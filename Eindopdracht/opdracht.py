import random
from appJar import gui
import logging

#FSM-states
A = "START"
B = "SELECT_PRODUCT"
C = "CHECK_VOORRAAD"
D = "BETALING"
E = "AFHANDELING"
F = "EIND"

#Format logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%H:%M:%S"
)

#Initialisatie variabelen
logger = logging.getLogger(__name__)
verkopen = {"Chips": 0, "Autodrop": 0, "Frisdrank": 0, "Chocolade": 0}
omzet = 0
fouten = []

producten = {
    "Chips": {"prijs": 1.5, "voorraad": 5},
    "Autodrop": {"prijs": 2.5, "voorraad": 5},
    "Frisdrank": {"prijs": 1.0, "voorraad": 5},
    "Chocolade": {"prijs": 2.0, "voorraad": 5}
}

def simuleer_automaat():
    global omzet, verkopen, fouten, producten
    klanten = 20

    for i in range(klanten):
        state = A
        product = ""
        betaalBedrag = 0
        wisselgeld = 0

        logger.info(f"Klant {i + 1} start transactie")

        while state != F:

            if state == A:
                logger.debug("State: START")
                state = B

            elif state == B:
                product = random.choice(list(producten.keys()))
                betaalBedrag = round(random.uniform(1.0, 3.5) * 10) / 10

                logger.info(
                    f"Klant {i + 1}: {product} geselecteerd, €{betaalBedrag:.2f} ingevoerd"
                )
                state = C

            elif state == C:
                if producten[product]["voorraad"] > 0:
                    logger.debug(f"{product} op voorraad")
                    state = D
                else:
                    logger.warning(f"{product} niet op voorraad")
                    fouten.append(f"{product} niet op voorraad")
                    state = F

            elif state == D:
                prijs = producten[product]["prijs"]
                wisselgeld = betaalBedrag - prijs

                if wisselgeld >= 0:
                    logger.debug("Voldoende betaald")
                    state = E
                else:
                    logger.warning(
                        f"Onvoldoende betaling voor {product}: "
                        f"€{betaalBedrag:.2f} < €{prijs:.2f}"
                    )
                    fouten.append(f"Onvoldoende betaald voor {product}")
                    state = F

            elif state == E:
                producten[product]["voorraad"] -= 1
                verkopen[product] += 1
                omzet += producten[product]["prijs"]

                logger.info(
                    f"{product} verkocht voor €{producten[product]["prijs"]:.2f}"
                )

                if wisselgeld > 0:
                    logger.info(f"Wisselgeld teruggegeven: €{wisselgeld:.2f}")
                else:
                    logger.info("Geen wisselgeld")

                state = F

        logger.info(f"Klant {i + 1} transactie afgerond\n")
    logger.info(f"Totale omzet: €{omzet:.2f}")
    logger.info(f"Verkochte producten: {verkopen['Chips']} chips,"
                f"{verkopen['Autodrop']} autodrop,"
                f"{verkopen['Frisdrank']} frisdrank,"
                f"{verkopen['Chocolade']} chocolade")
        

def update_gui():
    simuleer_automaat()
    
    app.addLabel("header", "Snackautomaat Simulatie")
    
    app.addLabel("omzet", f"Totale Omzet: €{omzet:.2f}")
    
    for product, aantal in verkopen.items():
        app.addLabel(f"{product}_verkocht", f"{product}: {aantal} verkocht")
    
    if fouten:
        app.addLabel("fouten", "Fouten:")
        for i, fout in enumerate(fouten):
            app.addLabel(f"fout_{i}", fout)
        app.addLabel("mededeling", "Zie de log voor uitgebreide info")


app = gui("Snackautomaat Simulatie", "400x400")
app.addButton("Simuleer Verkoop", update_gui)
app.setBg("lightgray")

app.go()