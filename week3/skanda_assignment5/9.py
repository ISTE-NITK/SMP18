

import random

class Card:
    suit=['Hearts','Diamonds','Clubs','Spades']
    value=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']


class Deck(Card):
    def __init__(self):
        self.cards=[(a,b) for a in self.value for b in self.suit]

    def deal(self):
        t=random.choice(self.cards)
        print('Dealt:',t)  
        self.cards.remove(t)

    def Shuffle(self):
        self.cards=[(a,b) for a in self.value for b in self.suit]
        random.shuffle(self.cards)


a=Deck()  #An object of class Deck

#prints all the cards present in a deck currently
print('Cards present in a deck: ',a.cards)

#gets back all the dealt cards and shuffles the deck
a.Shuffle()

print()

#dealing cards
a.deal()
a.deal()   
a.deal()
        
print('Cards present in a deck: ',a.cards)

a.Shuffle()

print()
print('Cards present in a deck: ',a.cards)


