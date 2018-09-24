from Deck import Deck, Card


class Player:
    def __init__(self, number: int, deck: Deck=None):
        self.id = number
        self.deck = deck

    def give_cards(self, deck: Deck):
        self.deck = deck

    def draw_card(self) -> Card:
        return self.deck.draw_card()

    def give_card(self, card: Card):
        self.deck.put_card_on_bottom(card)
