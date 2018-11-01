from Deck import Deck, Card
from Player import Player


def war(p1: Player, p2: Player):
    risked_cards = Deck(kind='empty')
    for i in range(3):
        if p1.deck.size() > 1:
            risked_cards.put_card_on_bottom(p1.draw_card())
        else:
            return p2, risked_cards
        if p2.deck.size() > 1:
            risked_cards.put_card_on_bottom(p2.draw_card())
        else:
            return p1, risked_cards

    cards = []
    for player in players:
        cards.append(player.draw_card())
        print(f'{player} draws a {cards[player.id - 1]} in the war')

    risked_cards.put_cards_on_bottom(Deck(cards=cards))

    if cards[0].compare_to(cards[1]) < 0:
        winner = p2
    elif cards[0].compare_to(cards[1]) > 0:
        winner = p1
    else:
        winner, extra_cards = war(p1, p2)
        risked_cards.put_cards_on_bottom(extra_cards)

    print(f'{winner} won the war!')
    return winner, risked_cards


def take_turn(players):
    cards = [player.draw_card() for player in players]

    for player in players:
        print(f'{player} drew {cards[player.id - 1]}')
    
    risked_cards = Deck(cards=cards)
    winner = players[0]

    if cards[0].compare_to(cards[1]) < 0 or players[0].num_cards() is 0:
        winner = players[1]
    elif cards[0].compare_to(cards[1]) is 0:
        print('War!')
        winner, war_cards = war(players[0], players[1])
        print(f'Cards won: {war_cards}')
        risked_cards.put_cards_on_bottom(war_cards)
    
    winner.give_cards(risked_cards)
    print(f'{winner} won the hand!')


if __name__ == '__main__':

    NUMBER_OF_PLAYERS = 2
    MAX_TURNS = 5000

    cards = Deck()
    cards.shuffle()

    players = []

    for i in range(NUMBER_OF_PLAYERS):
        players.append(Player(i+1, deck=Deck(kind='empty')))

    for i in range(int(cards.size()/2)):
        players[0].give_card(cards.draw_card())
    for i in range(cards.size()):
        players[1].give_card(cards.draw_card())

    print('---------Start game----------')
    for player in players:
        print(f'{player} has {player.deck.size()} cards')

    num_turns = 0

    while players[0].num_cards() > 0 and players[1].num_cards() > 0 and num_turns < MAX_TURNS:
        take_turn(players)
        num_turns += 1
        for player in players:
            print(f'{player}: {player.deck.size()}')
        print()

    if players[0].num_cards() > players[1].num_cards():
        print('Player 1 wins!')
    elif players[1].num_cards() > players[0].num_cards():
        print('Player 2 wins!')
    else:
        print("It's a tie!")
    print(f'Total turns: {num_turns}')




