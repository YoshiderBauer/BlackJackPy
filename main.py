import random

#BlackJack in Python
#Stand: 30.04.2022


deck = []

spielerHand = []
spielerPunkte = 0
spielerSiege = 0

bankHand = []
bankPunkte = 0
bankSiege = 0

def randomKarte(karteZiehen): # True: Spieler bekommt Karte, False: Bank bekommt karte
    zufallszahl = random.randint(0, len(deck))
    if karteZiehen == True:
        spielerHand.append(deck[zufallszahl])
        print('Deine aktuelle Hand: ' + spielerHand)
    else:
        bankHand.append(deck[zufallszahl])
        print('Die aktuelle Hand der Bank: ' + bankHand)
    deck.pop(zufallszahl)

def reset():

    deck.clear()
    spielerHand.clear()
    bankHand.clear()
    spielerPunkte = 0
    bankPunkte = 0

    for i in range(24):
        deck.append('2')
        deck.append('3')
        deck.append('4')
        deck.append('5')
        deck.append('6')
        deck.append('7')
        deck.append('8')
        deck.append('9')
        deck.append('10')
        deck.append('Bube')
        deck.append('Dame')
        deck.append('König')
        deck.append('Ass')

while spielerSiege < 10 or bankSiege < 10:
    reset()
    randomKarte(True)
    randomKarte(True)
    randomKarte(False)
    randomKarte(False)

    while input('Möchtest du  noch eine Karte ziehen? (Ja/Nein') == 'Ja':
        randomKarte(True)

#test