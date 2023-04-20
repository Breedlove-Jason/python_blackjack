# Command Line Blackjack Game

````
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
````
This is a simple command line blackjack game implemented in Python.

# Rules

- The deck is unlimited in size.
- There are no jokers.
- The Jack/Queen/King all count as 10.
- The Ace can count as 11 or 1.
- Use the following list as the deck of cards: [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
- The cards in the list have equal probability of being drawn.
- Cards are not removed from the deck as they are drawn.
- The computer is the dealer.

## How to Play

- Run the script in your terminal by running python blackjack.py.
- The game will start by dealing two cards to the player and two cards to the dealer.
- The player will be asked whether they want to hit or stand. If the player chooses to hit, another card will be dealt from the deck.
- If the player's total exceeds 21, they bust and the game is over.
- If the player chooses to stand, the dealer will start drawing cards from the deck until their total is at least 17.
- If the dealer's total exceeds 21, they bust and the game is over.
- If neither the player nor the dealer busts, the one with the highest total wins.

## How to Run

- Clone the repository to your local machine.
- Navigate to the directory where the file blackjack.py is located.
- Run the command python blackjack.py in your terminal to start the game.

# License

This project is licensed under the terms of the MIT license.