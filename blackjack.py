from art import logo
import random

############### Blackjack Project #####################
print(logo)

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

# Create a list to store the deck of cards
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


def shuffle_deck():
    random.shuffle(ranks)


shuffle_deck()


def calc_card(card):
    """Calculate the value of the card"""
    if card == 'Jack' or card == 'Queen' or card == 'King':
        return 10
    if card == 'Ace':
        ace_input = input("Ace Drawn! Do you want to use it as 1 or 11? ")
        if ace_input == '1':
            return 1
        if ace_input == '11':
            return 11
    else:
        return int(card)


def hit():
    """Deal a card from the deck"""
    return calc_card(random.choice(ranks))


# Player Cards
player_card_1 = calc_card(random.choice(ranks))
print(f"Player Draws: {player_card_1}")
player_card_2 = calc_card(random.choice(ranks))
print(f"Player Draws: {player_card_2}")
player_total = player_card_1 + player_card_2

# Computer Cards
computer_card_1 = calc_card(random.choice(ranks))
print(f"Computer Draws: {computer_card_1}")
computer_card_2 = calc_card(random.choice(ranks))
print(f"Computer Draws: ##")
computer_total = computer_card_1 + computer_card_2

user_hit = True
computer_hit = True

# User Game Loop
while user_hit:
    user_input = input("Hit or Stand? 'h/s' ").lower()

    if user_input == 'h':
        hit_me = hit()
        player_total += hit_me
        print(f"You draw: {hit_me} and your total is {player_total} ")
        if player_total > 21:
            print("You Bust!")
            print("Computer Wins!")
            computer_hit = False
            break
            # user_hit = False
        elif player_total == 21:
            print("Player Gets Blackjack!")
            print("You Win!")
            computer_hit = False
            user_hit = False
    if user_input == 's':
        print("You stand!")
        print(player_total)
        print(f"Computer Reveals: {computer_card_2} and their total is {computer_total} ")
        user_hit = False

# Computer Game Loop
while computer_hit:
    if computer_total < 17:
        computer_hit = hit()
        computer_total += computer_hit
        print(f"Computer draws: {computer_hit} and their total is {computer_total} ")
    elif computer_total > 21:
        print("Computer Busts!")
        print("You Win!")
        break
    elif computer_total == 21:
        print("Computer Gets Blackjack!")
        print("Computer Wins!")
        break
    elif computer_total > player_total:
        print("Computer Wins!")
        break
    elif computer_total == player_total:
        print("Draw!")
        break
