from art import logo
import random

############### Blackjack Project #####################
print(logo)

# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Create a list to store the deck of cards
deck = []

# Generate the deck of cards
# for suit in suits:
#     for rank in ranks:
#         card = {
#             'suit': suit,
#             'rank': rank
#         }
#         deck.append(card)


# Print the deck of cards
# for card in deck:
#     print(card['rank'], 'of', card['suit'])

# Shuffle the deck of cards
def shuffle_deck():
    random.shuffle(ranks)


shuffle_deck()


def calc_card(card):
    """Calculate the value of the card"""
    if card == 'Jack' or card == 'Queen' or card == 'King':
        return 10
    elif card == 'Ace':
        return 11
    else:
        return int(card)


# Deal a card from the deck
# Player Cards
player_card_1 = calc_card(random.choice(ranks))
player_card_2 = calc_card(random.choice(ranks))
print(f"Player's cards: {player_card_1}, {player_card_2}")
total_player_cards = player_card_1 + player_card_2
print(f"Total: {total_player_cards}")

# Computer Cards
computer_card_1 = calc_card(random.choice(ranks))
computer_card_2 = calc_card(random.choice(ranks))
total_computer_cards = computer_card_1 + computer_card_2
print(f"Computer's cards: {computer_card_1}, {computer_card_2}")
print(f"Total: {total_computer_cards}")
