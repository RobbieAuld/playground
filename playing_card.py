import collections
from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = {"spades": 3, "hearts": 2, "diamonds": 1, "clubs": 0}

    def spades_high(self, card):
        rank_value = self.ranks.index(card.rank)
        return rank_value * len(self.suits.values()) + self.suits[card.suit]

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits.keys() for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == "__main__":
    deck = FrenchDeck()

    [print(card) for card in sorted(deck, key=deck.spades_high)]

