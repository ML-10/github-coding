while True:
    x = int(input('Number: '))
    n = x
    debug = bool(input('DEBUG: '))
    lim = int(input(
    while n != 1:
            if n % 2 == 0:
                      if debug: print('           ', n, '/ 2 = ', end='')
                      n = int(n / 2)
                      if debug: print(n)
            elif n % 2 != 0:
                      if debug: print('           ', n, 'x 3 + 1 = ', end='')
                      n = int((3*n+1))
                      if debug: print(n)
            else:
                     raise TypeError('The number must be an integer')
            
    print('Done')
