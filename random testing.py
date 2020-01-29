from random import randint
l = []
for i in range(101):
          l.append(0)
for j in range(1000):
          l[randint(1,100)] = l[randint(1,100)]+1
for k in l:
          print(str(k*('O')))
