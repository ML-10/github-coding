from random import randint
def pick(words):
    num_words = len(words)
    num_picked = randint(0, num_words - 1)
    word_picked = words[num_picked]
    return word_picked
items = ['ROCK', 'PAPER', 'SCISSORS']
while True:
    print('Welcome to rock, paper, scissors')
    player = input('Choose rock, paper, or scissors: ').upper()
    print('You chose', player.upper())
    computer = pick(items)
    print('I choose', computer)
    rules = {'ROCK':'SCISSORS','PAPER':'ROCK','SCISSORS':'PAPER'}
    if player == computer:
        print('It\'s a draw')
    elif rules[player] == computer:
        print('Player won')
    else:
        print('Computer won')

    
   
