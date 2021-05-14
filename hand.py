# Created by : James Lee
# Created on : June 2019

# Hand class

# The hand class holds all the player's cards
# This class is also held in the player class

class hand:

  # Constructor
  def __init__(self):
    self.__total = 0
    self.__cardsInHand = []

  # Adds card into hand
  def addCard(self, card):
    self.__cardsInHand.append(card)
    self.__total += card.getValue()

  # Removes card from hand
  # Used when splitting hand
  def removeCard(self):
    returnCard = self.__cardsInHand.pop()
    self.__total -= returnCard.getValue()
    return returnCard

  # Finds total value of cards in hand
  def findTotal(self):
    return self.__total

  # Prints out all cards in hand
  def printCards(self):
    output = ''

    for i in range(len(self.__cardsInHand)):
      output += self.__cardsInHand[i].toString() + " "

    return output

  # Checks wheter ace is worth 1 or 11
  # If the ace as 11 exceeds 21, ace value is 1
  # Else, ace value is 11
  def checkForAce(self):
    for i in range(len(self.__cardsInHand)):
      if self.__cardsInHand[i].getRank() == 'A':
        if self.__total + 10 <= 21:
          self.__total += 10

    return self.__total

  # Returns wheter hand can be split
  def canSplit(self):
    if self.__cardsInHand[0].getValue() == self.__cardsInHand[1].getValue():
      return True

    return False
