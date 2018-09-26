import random
import enum


class Value(enum.Enum):
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14


class Suit(enum.Enum):
    CLUB = 'Club'
    SPADE = 'Spade'
    HEART = 'Heart'
    DIAMOND = 'Diamond'


class Card:
    def __init__(self, value: Value, suit: Suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value.name} of {self.suit.value}s'

    def compare_to(self, card: 'Card'):
        if self.value.value < card.value.value:
            return -1
        if self.value.value == card.value.value:
            return 0
        if self.value.value > card.value.value:
            return 1


class Deck:
    def __init__(self, kind: str='normal'):
        if kind == 'normal':
            self.cards = Deck.new_deck()
        elif kind == 'empty':
            self.cards = []

    def __iter__(self):
        return self.cards

    def __repr__(self):
        return self.cards.__repr__()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop(0)

    @classmethod
    def draw_cards(cls, num: int):
        cards = []
        for card in range(num):
            cards.append(self.cards.pop())
        return cls(cards)

    def put_card_on_bottom(self, card: Card):
        self.cards.append(card)

    def put_cards_on_bottom(self, deck: 'Deck'):
        for card in deck.cards:
            self.cards.append(card)

    def reset_deck(self):
        self.cards = Deck.new_deck()

    def size(self) -> int:
        return len(self.cards)

    @staticmethod
    def new_deck():
        cards = []
        for suit in Suit:
            for value in Value:
                cards.append(Card(value=value, suit=suit))
        return cards

