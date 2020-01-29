num = int(input('Enter number: '))
from math import factorial
def isPrime(n):
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return False
	return True
def PrimesUpTo(n):
	a = range(1, n+1)
	for i in a:
		if not isPrime(i):
			list(a).remove(i)
	return a
wieferichPrimes = PrimesUpTo(num)
for p in wieferichPrimes:
	if (p ** 2) % (2 ** (p - 1)) - 1 != 0:
		list(wieferichPrimes).remove(p)
if len(wieferichPrimes) > 0:
	print(list(wieferichPrimes))
else:
	print('No Wieferich primes found in range 1 to ' + num + '!')
input('Press enter to exit.')
