# Your first name:
# Your section:

import random
import matplotlib.pyplot as plt

# Write your functions with their docstrings here

# nextMiddleSquare


# listMiddleSquare

   
# nextLehmer


# listLehmer


# listRandom


def chartRandomNumbers(mid, lehmer, rand):
  '''
  This function draws a histogram of the three lists on the same plot
  :param mid: a list of random numbers from middle squares
  :param lehmer: a list of random numbers from lehmer
  :param rand: a list of random numbers from Python random module
  '''
  multi = [mid, lehmer, rand]
  plt.hist(multi, histtype='bar', label=['middle square', 'lehmer', 'random module'])
  plt.legend(prop={'size': 10})
  plt.show()
  


def main():
  start = 29
  list1 = listMiddleSquare(start)
  list2 = listLehmer(start)
  list3 = listRandom()
  chartRandomNumbers(list1, list2, list3)

if __name__ == "__main__":
  main()
