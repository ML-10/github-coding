players = []
np = int(input('num of players: '))
playerlist = []
class Player(name, scores=[], puddings=0, tscore=0):
    '''def __init__(self, name, scores=[], puddings=0, tscore=0):
          self.name = name
          self.score = score
          self.puddings = puddings
          self.tscore = tscore'''
          
for i in range(1, np+1):   
     playerlist.append(Player(input('name of player '+str(i)+': ')))
for i in range(1,4):
     for ip in range(1,np+1):
          playerlist[ip].scores.append(input('Score of round ' + i + ' for ' + playerlist[ip].name + ': '))
          if i == 3:
               playerlist[ip].puddings = input('Puddings of ' + playerlist[ip].name + ': ')
          playerlist[ip].tscore = sum(playerlist[ip].scores)
for i in playerlist:
     print(i.name + '.....................................................................................................................' + i.tscore)
