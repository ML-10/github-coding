def pigLatin(s):
     stringCopy = s.split(' ')
     for word in stringCopy:
          vowel = 'aeiou' + 'aeiou'.upper()
          consonant = 'bcdfghjklmnpqrstvwxyz' + 'bcdfghjklmnpqrstvwxyz'.upper()
          consonants = ''
          for i in range(len(s)):
               if word[i] in consonant: consonants += word[i]
               else: break
          word = ''.join(word.rsplit(consonants))
          word += '-' + consonants + 'ay'
          print(word)
pigLatin(input())
