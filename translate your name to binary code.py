#translate your name to binary code
while True:
    name = input('What\'s your name? ')
    for c in name:
        print(c, bin(ord(c)))
    input()
    
