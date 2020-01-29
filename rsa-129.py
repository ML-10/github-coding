def isPrime(n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
            return True
n = 114381625757888867669235779976146612010218296721242362562561842935706935245733897830597123563958705058989075147599290026879543541
for p in range(2, n):
    for q in range(2, n):
        if isPrime(p) and isPrime(q) and p * q == n:
            print('p = ' + str(p) + ' q = ' + str(q) + ', p * q = ' + str(n))

        
