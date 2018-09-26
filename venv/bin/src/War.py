from Deck import Deck, Card
from Player import Player


def war(p1: Player, p2: Player):
    risked_cards = Deck(kind='empty')
    for i in range(3):
        if p1.deck.size() > 1:
            risked_cards.put_card_on_bottom(p1.draw_card())
        if p2.deck.size() > 1:
            risked_cards.put_card_on_bottom(p2.draw_card())

    card1 = p1.draw_card()
    print(f'Player 1 draws a {card1} in the war')
    card2 = p2.draw_card()
    print(f'Player 2 draws a {card2} in the war')

    risked_cards.put_card_on_bottom(card1)
    risked_cards.put_card_on_bottom(card2)

    if card1.compare_to(card2) < 0:
        winner = p2
        print('Player 2 won the war!')
    elif card1.compare_to(card2) > 0:
        winner = p1
        print('Player 1 won the war!')
    else:
        if p1.deck.size() > 0 and p2.deck.size() > 0:
            winner, extra_cards = war(p1, p2)
            risked_cards.put_cards_on_bottom(extra_cards)
        else:
            if p1.deck.size() > 0:
                winner = p1
            else:
                winner = p2

    return winner, risked_cards


def take_turn(p1: Player, p2: Player):
    card1 = p1.draw_card()
    card2 = p2.draw_card()

    print(f'Player 1 drew {card1}')
    print(f'Player 2 drew {card2}')

    if card1.compare_to(card2) > 0:
        p1.give_card(card1)
        p1.give_card(card2)
        print('Player 1 wins the hand!')
    elif card1.compare_to(card2) < 0:
        p2.give_card(card1)
        p2.give_card(card2)
        print('Player 2 wins the hand!')
    else:
        if p1.deck.size() == 0:
            p2.give_card(card1)
            p2.give_card(card2)
        elif p2.deck.size() == 0:
            p1.give_card(card1)
            p1.give_card(card2)
        else:
            print('War!')
            winner, cards = war(p1, p2)
            winner.give_card(card1)
            winner.give_card(card2)
            print(f'Cards won: {cards}')
            winner.give_cards(cards)
            print(f'Gave cards to {winner}')


if __name__ == '__main__':

    NUMBER_OF_PLAYERS = 2
    MAX_TURNS = 5000

    cards = Deck()
    cards.shuffle()

    players = []

    for i in range(NUMBER_OF_PLAYERS):
        players.append(Player(i, deck=Deck(kind='empty')))

    for i in range(int(cards.size()/2)):
        players[0].give_card(cards.draw_card())
    for i in range(cards.size()):
        players[1].give_card(cards.draw_card())

    print('---------Start game----------')
    print(f'Player 1 has {players[0].deck.size()} cards')
    print(f'Player 2 has {players[1].deck.size()} cards')
    num_turns = 0

    while players[0].deck.size() > 0 and players[1].deck.size() > 0 and num_turns < MAX_TURNS:
        take_turn(players[0], players[1])
        num_turns += 1
        print(f'Player 1: {players[0].deck.size()} Player 2: {players[1].deck.size()}')
        print()

    if players[0].deck.size() > players[1].deck.size():
        print('Player 1 wins!')
    elif players[1].deck.size() > players[0].deck.size():
        print('Player 2 wins!')
    else:
        print("It's a tie!")
    print(f'Total turns: {num_turns}')




