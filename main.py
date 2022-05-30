import random

#BlackJack in Python
#Stand: 30.04.2022
#


deck = []

spielerHand = []
global spielerPunkte
spielerPunkte = 0
global spielerSiege
spielerSiege = 0

bankHand = []
global bankPunkte
bankPunkte= 0
global bankSiege
bankSiege= 0

def randomKarte(karteZiehen, punkte): # True: Spieler bekommt Karte, False: Bank bekommt karte
    zufallszahl = random.randint(0, len(deck))
    if karteZiehen == True:
        spielerHand.append(deck[zufallszahl])
        print('Deine aktuelle Hand: ', end='')
        print(spielerHand)
        spielerPunkte = punkte
        if spielerHand[-1] == '2':
            spielerPunkte = spielerPunkte + 2
        elif spielerHand[-1] == '3':
            spielerPunkte = spielerPunkte + 3
        elif spielerHand[-1] == '4':
            spielerPunkte = spielerPunkte + 4
        elif spielerHand[-1] == '5':
            spielerPunkte = spielerPunkte + 5
        elif spielerHand[-1] == '6':
            spielerPunkte = spielerPunkte + 6
        elif spielerHand[-1] == '7':
            spielerPunkte = spielerPunkte + 7
        elif spielerHand[-1] == '8':
            spielerPunkte = spielerPunkte + 8
        elif spielerHand[-1] == '9':
            spielerPunkte = spielerPunkte + 9
        elif spielerHand[-1] == '10':
            spielerPunkte = spielerPunkte + 10
        elif spielerHand[-1] == 'Bube':
            spielerPunkte = spielerPunkte + 10
        elif spielerHand[-1] == 'Dame':
            spielerPunkte = spielerPunkte + 10
        elif spielerHand[-1] == 'König':
            spielerPunkte = spielerPunkte + 10
        elif spielerHand[-1] == 'Ass':
            spielerPunkte = spielerPunkte + 11
        return spielerPunkte
    else:
        bankHand.append(deck[zufallszahl])
        print('Die aktuelle Hand der Bank: ', end='')
        print(bankHand)
        bankPunkte = punkte
        if bankHand[-1] == '2':
            bankPunkte = bankPunkte + 2
        elif bankHand[-1] == '3':
            bankPunkte = bankPunkte + 3
        elif bankHand[-1] == '4':
            bankPunkte = bankPunkte + 4
        elif bankHand[-1] == '5':
            bankPunkte = bankPunkte + 5
        elif bankHand[-1] == '6':
            bankPunkte = bankPunkte + 6
        elif bankHand[-1] == '7':
            bankPunkte = bankPunkte + 7
        elif bankHand[-1] == '8':
            bankPunkte = bankPunkte + 8
        elif bankHand[-1] == '9':
            bankPunkte = bankPunkte + 9
        elif bankHand[-1] == '10':
            bankPunkte = bankPunkte + 10
        elif bankHand[-1] == 'Bube':
            bankPunkte = bankPunkte + 10
        elif bankHand[-1] == 'Dame':
            bankPunkte = bankPunkte + 10
        elif bankHand[-1] == 'König':
            bankPunkte = bankPunkte + 10
        elif bankHand[-1] == 'Ass':
            bankPunkte = bankPunkte + 11
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

    spielerPunkte = randomKarte(True, spielerPunkte)
    spielerPunkte = randomKarte(True, spielerPunkte)
    bankPunkte = randomKarte(False, bankPunkte)
    bankPunkte = randomKarte(False, bankPunkte)

    while input('Möchtest du  noch eine Karte ziehen? (Ja/Nein) ') == 'Ja':
        randomKarte(True)

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

    for i in range(len(bankHand)):
        if bankHand[i] == '2':
            bankPunkte = bankPunkte + 2
        elif bankHand[i] == '3':
            bankPunkte = bankPunkte + 3
        elif bankHand[i] == '4':
            bankPunkte = bankPunkte + 4
        elif bankHand[i] == '5':
            bankPunkte = bankPunkte + 5
        elif bankHand[i] == '6':
            bankPunkte = bankPunkte + 6
        elif bankHand[i] == '7':
            bankPunkte = bankPunkte + 7
        elif bankHand[i] == '8':
            bankPunkte = bankPunkte + 8
        elif bankHand[i] == '9':
            bankPunkte = bankPunkte + 9
        elif bankHand[i] == '10':
            bankPunkte = bankPunkte + 10
        elif bankHand[i] == 'Bube':
            bankPunkte = bankPunkte + 10
        elif bankHand[i] == 'Dame':
            bankPunkte = bankPunkte + 10
        elif bankHand[i] == 'König':
            bankPunkte = bankPunkte + 10
        elif bankHand[i] == 'Ass':
            print()