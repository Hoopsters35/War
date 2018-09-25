from Deck import Deck, Card
from Player import Player


def compare(card1: Card, card2: Card) -> int:
    return card1.compare_to(card2)


def war(p1: Player, p2: Player):
    risked_cards = Deck(kind='empty')
    for i in range(3):
        risked_cards.put_card_on_bottom(p1.draw_card())
        risked_cards.put_card_on_bottom(p2.draw_card())

    card1 = p1.draw_card()
    card2 = p2.draw_card()

    risked_cards.put_card_on_bottom(card1)
    risked_cards.put_card_on_bottom(card2)

    if card1.compare_to(card2) < 0:
        winner = p2
    elif card1.compare_to(card2) > 0:
        winner = p1
    else:
        winner, risked_cards = war(p1, p2)

    return winner, risked_cards


def take_turn(p1: Player, p2: Player):
    card1 = p1.draw_card()
    card2 = p2.draw_card()

    print(f'Player 1 drew {card1}')
    print(f'Player 2 drew {card2}')

    if compare(card1, card2) > 0:
        p1.give_card(card1)
        p1.give_card(card2)
        print('Player 1 wins the hand!')
    elif compare(card1, card2) < 0:
        p2.give_card(card1)
        p2.give_card(card2)
        print('Player 2 wins the hand!')
    else:
        print('War!')
        winner, cards = war(p1, p2)
        winner.give_card(card1)
        winner.give_card(card2)
        winner.give_cards(cards)


if __name__ == '__main__':

    NUMBER_OF_PLAYERS = 2

    cards = Deck()
    cards.shuffle()

    players = []

    for i in range(NUMBER_OF_PLAYERS):
        players.append(Player(i, deck=Deck(kind='empty')))

    for i in range(int(cards.size()/2)):
        players[0].give_card(cards.draw_card())
    for i in range(cards.size()):
        players[1].give_card(cards.draw_card())

    take_turn(players[0], players[1])




