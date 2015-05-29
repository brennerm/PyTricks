#! /usr/bin/env python3

""" How to use dunder methods to add behavior to objects.
Here it's an example of how implement a french deck that can be used as a list"""

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class Deck:

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

card_a = Card('A', 'spades')
print(card_a)

deck = Deck()
len(deck)

print(deck[0])
print(deck[-1])
for card in deck:
    print(card)
