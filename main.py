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
        print('Deine aktuelle Hand: ', end='')
        print(spielerHand)
    else:
        bankHand.append(deck[zufallszahl])
        print('Die aktuelle Hand der Bank: ', end='')
        print(bankHand)
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

    while input('Möchtest du  noch eine Karte ziehen? (Ja/Nein) ') == 'Ja':
        randomKarte(True)

for i in range(len(spielerHand)):
    if spielerHand[i] == '2':
        spielerPunkte + + 2
    elif spielerHand[i] == '3':
        spielerPunkte + + 3
    elif spielerHand[i] == '4':
        spielerPunkte + + 4
    elif spielerHand[i] == '5':
        spielerPunkte + + 5
    elif spielerHand[i] == '6':
        spielerPunkte + + 6
    elif spielerHand[i] == '7':
        spielerPunkte + + 7
    elif spielerHand[i] == '8':
        spielerPunkte + + 8
    elif spielerHand[i] == '9':
        spielerPunkte + + 9
    elif spielerHand[i] == '10':
        spielerPunkte + + 10
    elif spielerHand[i] == 'Bube':
        spielerPunkte + + 10
    elif spielerHand[i] == 'Dame':
        spielerPunkte + + 10
    elif spielerHand[i] == 'König':
        spielerPunkte + + 10
    elif spielerHand[i] == 'Ass':
        ass = input('Soll das Ass als 1 oder 11 gewertet werden?')
        if ass == 1:
            spielerPunkte + + 1
        elif ass == 11:
            spielerPunkte + + 11
        else:
            print('Falsche Eingabe, Das Ass wird als 11 gewertet')
            spielerPunkte + + 11

print('Deine Punkte: ' + spielerPunkte)

