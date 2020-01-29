from secrets import randbelow
def capwords(s, sep=None):
    return (sep or ' ').join(x.capitalize() for x in s.split(sep))
def isCap(s):
          return s == capwords(s)
ed = input('e/d: ')
c = input('c: ')
d = dict(zip(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], list(range(1,100))))
dr = dict(zip(list(range(1,100)), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']))
dc = dict(zip(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], list(range(1,100))))
dcr = dict(zip(list(range(1,100)), ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
l = []
if ed == 'e':
          r = randbelow(1000000)
          for i in c:
                    if isCap(i):
                              l.append(str(dc[i]+r) + '-1 ')
                    elif i == ' ':
                              pass
                    elif not isCap(i):
                              l.append(str(d[i]+r) + '-0 ')
          l.append(str(r))
          print(''.join(l))
if ed == 'd':
          l = c.split(' ')
          for i in l:
                    i = str(int(i) - int(l[-1])) + i[-1]
                    if i[-2] + i[-1] == '-1':
                              i = dcr[i-(i[-1]+i[-2])]
          ''.join(l)
          
                    
          
