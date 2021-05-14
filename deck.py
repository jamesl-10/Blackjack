# Created by : James Lee
# Created on : June 2019

# Deck class

# The deck class holds all the cards
# It can return a card via its drawCard method

import random

class deck:

  #Constructor
  def __init__(self):
    self.__deckOfCards = []
    self.__runningCount = 0

  # Shuffles deck
  def shuffle(self):
    random.shuffle(self.__deckOfCards)

  # Adds card into deck
  def addCard(self,card):
    self.__deckOfCards.append(card)

  # Draws card (removes card from deck)
  def drawCard(self):
    if len(self.__deckOfCards) == 0:
      return None
    else:
      returnCard = self.__deckOfCards.pop()
      self.__runningCount += returnCard.getHiLoValue()
      return returnCard

  # Returns running count
  def getRunningCount(self):
    return self.__runningCount
