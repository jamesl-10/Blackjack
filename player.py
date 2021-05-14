# Created by : James Lee
# Created on : June 2019

# Player class

# The player class holds all the hands

from hand import hand

class player:

  # Constructor
  def __init__(self, initHand):
    self.__initHand = initHand
    self.__hands = []
    self.__hands.append(self.__initHand)
    self.__gameWon = False

  def split(self, currentHand, c1, c2):
    splitHand = hand()
    self.__hands.append(splitHand)
    splitHand.addCard(currentHand.removeCard())
    currentHand.addCard(c1)
    splitHand.addCard(c2)

  def playerHands(self):
    return self.__hands

  def play(self, deckOfCards):

    for i, currentHand in enumerate(self.__hands):
      while True:

        # Breaks if player busts
        if currentHand.findTotal() > 21:
          print("You are busted!")
          self.__gameWon = False
          break

        # Asks if user wants to hit or stand
        print("User has " + currentHand.printCards() + "in hand " + str(i + 1))
        print("Running count is " + str(deckOfCards.getRunningCount()))
        userChoice = input("Would you like to hit or stand or split? (Hit/Stand/Split) : ")

        # Draws additional card
        if userChoice == 'Hit':
          hitCard = deckOfCards.drawCard()
          print("User drew " + hitCard.toString())
          currentHand.addCard(hitCard)

        # Does not draw additional cards
        elif userChoice == 'Stand':
          print("User did not draw a card")
          break;

        elif userChoice == 'Split':
            if currentHand.canSplit() == True:
              c1 = deckOfCards.drawCard()
              c2 = deckOfCards.drawCard()

              print("User was given " + c1.toString() + " and " + c2.toString())
              self.split(currentHand, c1, c2)
            else:
              print("Error : You cannot split hands!")
        
        else:
          print("Error : Invalid input!")
        
    currentHand.checkForAce()
    
  def findWinner(self, dealerTotal):
    for i, currentHand in enumerate(self.__hands):
      # Shows totals of each player
      print("Total of hand " + str(i+1) + " is " + str(currentHand.findTotal()))
      print("Dealer total is " + str(dealerTotal))

      # Checks for winner
      if currentHand.findTotal() > 21:
        currentHand.__gameWon = False

      elif currentHand.findTotal() == 21:
        currentHand.__gameWon = True

      elif currentHand.findTotal() < dealerTotal and dealerTotal <= 21:
        currentHand.__gameWon = False

      elif currentHand.findTotal() > dealerTotal:
        currentHand.__gameWon = True

      elif currentHand.findTotal() <= 21 and dealerTotal > 21:
        currentHand.__gameWon = True

      if currentHand.findTotal() == dealerTotal and dealerTotal < 21 and dealerTotal < 21:
        print("It's a tie!")

      elif currentHand.__gameWon == True:
        print("You win!")

      elif currentHand.__gameWon == False:
        print("You lose!")
