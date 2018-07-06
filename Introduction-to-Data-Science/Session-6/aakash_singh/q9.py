import random


class deck:
    class card:
        def __init__(self, suit, val):
            self.suit = suit
            self.val = val

        def __str__(self):
            return '{} {}'.format(self.suit, self.val)

        def __repr__(self):
            return self.__str__()

    __suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    __values = ['A', '2', '3', '4', '5', '6',
                '7', '8', '9', '10', 'J', 'Q', 'K']

    Deck = []

    def deal(self,suit,value):
        i=0
        for i in range(len(self.Deck)):
            if self.Deck[i].suit==suit and self.Deck[i].val==value:
                del self.Deck[i]
                print('del')
                return

    def __init__(self):
        random.seed()
        for i in self.__suits:
            for j in self.__values:
                self.Deck.append(self.card(i, j))

    def swap(self, a, b):
        self.Deck[a], self.Deck[b] = self.Deck[b], self.Deck[a]

    def shuffle(self):
        if len(self.Deck) != 52:
            self.__init__()
        for i in range(1000):
            self.swap(random.randrange(0, 52), random.randrange(0, 52))