import random

#BlackJack in Python
#Stand: 30.04.2022
#


deck = []

spielerHand = []

spielerPunkte = 0

spielerSiege = 0

bankHand = []

bankPunkte= 0

bankSiege= 0

def randomKarte(player):
    zufallszahl = random.randint(0, len(deck))
    if player == True:
        spielerHand.append(deck[zufallszahl])
        print('Deine aktuelle Hand: ', end='')
        print(spielerHand)
    else:
        bankHand.append(deck[zufallszahl])
        print('Die aktuelle Hand der Bank: ', end='')
        print(bankHand)

    karte = 0

    if deck[zufallszahl] == '2':
        karte =+ 2
    elif deck[zufallszahl] == '3':
        karte =+ 3
    elif deck[zufallszahl] == '4':
        karte =+ 4
    elif deck[zufallszahl] == '5':
        karte =+ 5
    elif deck[zufallszahl] == '6':
        karte =+ 6
    elif deck[zufallszahl] == '7':
        karte =+ 7
    elif deck[zufallszahl] == '8':
        karte =+ 8
    elif deck[zufallszahl] == '9':
        karte =+ 9
    elif deck[zufallszahl] == '10':
        karte =+ 10
    elif deck[zufallszahl] == 'Bube':
        karte =+ 10
    elif deck[zufallszahl] == 'Dame':
        karte =+ 10
    elif deck[zufallszahl] == 'König':
        karte =+ 10
    elif deck[zufallszahl] == 'Ass':
        karte =+ 11
    deck.pop(zufallszahl)
    return karte


def reset():

    deck.clear()
    spielerHand.clear()
    bankHand.clear()

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
    spielerPunkte = 0
    bankPunkte = 0
    reset()

    spielerPunkte = spielerPunkte + randomKarte(True)
    spielerPunkte = spielerPunkte + randomKarte(True)
    bankPunkte = bankPunkte + randomKarte(False)
    bankPunkte = bankPunkte + randomKarte(False)

    while input('Möchtest du  noch eine Karte ziehen? (Ja/Nein) ') == 'Ja':
        spielerPunkte = spielerPunkte + randomKarte(True)

    for i in range(len(spielerHand)):
        if spielerHand[i] == 'Ass':
            ass = input('Soll das Ass als 1 oder 11 gewertet werden? ')
            if ass == '1':
                spielerPunkte = spielerPunkte - 10
            elif ass == '11':
                spielerPunkte = spielerPunkte
            else:
                print('Falsche Eingabe, Das Ass wird als 11 gewertet')

    print('Deine Punkte: ' + str(spielerPunkte))
