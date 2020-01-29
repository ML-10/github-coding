from random import randint
from time import sleep
while True:
    l = [None,None,None,None,None]
    rolls = 0
    win = False
    while not win:
              for n in range(1, 6):
                        if l == [n,n,n,n,n]:
                                  rolls += 1
                                  print('Yahtzee! Rolls: ' + str(rolls) + ' ' + str(l))
                                  win = True
                        else:
                                  rolls += 1
              for n in range(5):
                        l[n] = randint(1,6)
    input()                 
