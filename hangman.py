from random import choice
wordList = ['HOUSE']
word = choice(wordList)
gameWord = len(word) * '*'
guess = ''
guessList = []
def ask():
          guess = input('Guess a letter! ').upper()
          if len(guess) != 1:
                    print('One letter, please!')
                    ask()
          guessList.append(guess)
def showWord():
          print('The word so far: ' + gameWord)
while guess != word:
          print(guess)
          showWord()
          ask()
          for n in range(len(word)):
                    if guess == word[n]:
                              gameWord[n] = guess
                              hasLetter = True
                              print('Good guess!')
                    else:
                              hasLetter = False

          if not hasLetter:
                    print('Not in the word!')
                    
                              
                    


print('The word was '+ word + '!')
          
          
          
      
    
