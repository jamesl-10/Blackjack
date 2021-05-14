# Created by : James Lee
# Created on : June 2019

# The main program

from deck import deck
from card import card
from hand import hand
from player import player

# All the ranks and suits
ranks = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A']
suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

# Creates deck
deckOfCards = deck()

# Creates all the cards, then puts into deck
for i in range(len(ranks)):
  for j in range(len(suits)):
    c = card(suits[j], ranks[i])
    deckOfCards.addCard(c)

# Shuffles deck
deckOfCards.shuffle()

print("Welcome to Blackjack! The objective of the game is to draw cards until you get cards with values as close to 21 as possible!")

while True:
  
  # Creates hands
  user = hand()
  computer = hand()

  # Initial deal
  # Player dealt two cards
  for i in range(2):
    user.addCard(deckOfCards.drawCard())

  # Computer dealt one card
  # The other one is 'face down', (not dealt yet)
  computer.addCard(deckOfCards.drawCard())

  # Creates player
  p1 = player(user)

  # Shows dealer's card
  print('Dealer holds ' + computer.printCards() + " and a face down card.")

  # Method that hits, stands or splits
  p1.play(deckOfCards)

  # Draws computer second card
  computerSecondCard = deckOfCards.drawCard()
  computer.addCard(computerSecondCard)

  # Shows computer second card
  print("Dealer flips over card to reveal " + computerSecondCard.toString())
  print("Running count is " + str(deckOfCards.getRunningCount()))
  computer.checkForAce()

  # Dealer must keep drawing until total is above 16
  while computer.findTotal() < 16:
    newCard = deckOfCards.drawCard()
    computer.addCard(newCard)
    print("Dealer drew " + newCard.toString())
    print("Running count is " + str(deckOfCards.getRunningCount()))

  # Show dealer's final hand
  print("Dealer holds " + computer.printCards())

  # Finds winner
  p1.findWinner(computer.findTotal())

  # Plays again (or not)
  playAgain = input("Would you like to play again? (Yes/No) : ")

  if playAgain == 'Yes':
    print("Welcome back!")

  elif playAgain == 'No':
    print("Thanks for playing!")
    break

  else:
    print("Ok..? Thank you for playing now please leave our casino.")
    break
