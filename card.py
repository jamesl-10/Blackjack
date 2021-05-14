# Created by : James Lee
# Created on : June 2019

# Card class

# The card class holds all information pertinent to its value, rank, suit, and its hi/lo value
# used to calculate the running count

class card:

  # Constructor
  def __init__(self, suit, rank):
    self.__suit = suit
    self.__rank = rank

    # Assigns values to each card (J, Q, K = 10, A = 1)
    if rank == 'J' or rank == 'Q' or rank == 'K':
      self.__value = 10

    elif rank == 'A':
      self.__value = 1

    else:
      self.__value = int(rank)

    # Assigns hi/lo value
    # 2-6 = 1
    # 7-9 = 0
    # 10-A = -1
    if rank == '2' or rank == '3' or rank == '4' or rank == '5' or rank == '6':
      self.__hiloValue = 1

    elif rank == '7' or rank == '8' or rank == '9':
      self.__hiloValue = 0

    else:
      self.__hiloValue = -1

  # Returns suit
  def getSuit(self):
    return self.__suit

  # Returns rank
  def getRank(self):
    return self.__rank

  # Returns value
  def getValue(self):
    return self.__value

  # Prints the card's information
  def toString(self):
    return self.__rank + " of " + self.__suit

  # Returns hilo value
  def getHiLoValue(self):
    return self.__hiloValue
