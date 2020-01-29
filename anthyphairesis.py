n = int(input('Number 1: '))
k = int(input('Number 2: '))
while n % k != 0:
    print('{0} divided by {1} gives {2} with remainder {3}'.format(str(n), str(k), str(n // k), str(n % k)))
    old_k = k
    k = n % k
    n = old_k
print('{0} divided by {1} gives {2} with no remainder'.format(str(n), str(k), str(n // k)) + '\nStop!')

