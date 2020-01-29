from palintools import forcePalindrome
while True:
    n = int(input('Number: '))
    print('Palindrome: ' + forcePalindrome(n)[0] + ', done in ' + forcePalindrome(n)[1] + ' steps')
    

