l = []
l1 = []
x = 0
for n in range(6, 6):
          for i in range(1, n):
                    if n % i == 0:
                              l.append(i)
          for i1 in l:
                    x += i1
          if n == x:
                    l1.append(n)
          
          for i2 in l:
                    l.remove(i2)
          x = 0
print(l1)
