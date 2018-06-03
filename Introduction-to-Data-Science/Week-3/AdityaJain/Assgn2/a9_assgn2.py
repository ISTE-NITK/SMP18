#!/usr/bin/python3 
import random

class Card() :
    def __init__(self,value,suit):
        "Create and initialize a new card instance"
        self.__value=value
        self.__suit=suit 
        return
    @property
    def value(self):
        return self.__value
    @property 
    def suit(self):
        return self.__suit 
    def __str__(self):
        return ("Card[%s,%s]"%(self.value,self.suit))
    def __repr__(self):
        return self.__str__()
    def __eq__(self,other):
        if(self.suit==other.suit and self.value==other.value):
            return True
        return False


class Deck():
    def __init__(self):
        "Create a new deck containig 52 cards"
        self.__dlist=[]
        for i in ["Hearts",'Diamonds','Clubs','Spade'] :
            for j in range(1,14):
                self.__dlist.append(Card(j,i))
        return  

    def deal(self,card):
        "Deal a card from the deck. If the card is not present, the topmost card in the deck is dealt"
        if(card in self.__dlist):
            self.__dlist.remove(card)
            print(card)
        else:
            print(self.__dlist[-1])
            self.__dlist.pop()
        return 
    def shuffle(self):
        "Shuffle the deck"
        random.shuffle(self.__dlist)
        return
    def __str__(self):
        return ("Deck%s"%self.__dlist)
    def __repr__(self):
        return self.__str__()

card=Card(10,'Clubs')
print('Card ->',card.value,card.suit)
d=Deck()

print('Initial Deck\n',d,'\n\n')
d.deal(card)
print('Dealt 1 card\n',d,'\n\n')
d.shuffle()
print('Shuffled\n',d,'\n\n')
d.deal(Card(1,'Hearts'))
print('Dealt another card\n',d,'\n')





