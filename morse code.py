ed = input('e/d: ')
c = input('c: ').upper()
if ed == 'e':
    s = input('t/f: ')
    if s == 't': sec = float(input('s: '))
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'} 
def encrypt(message): 
    cipher = '' 
    for letter in message:
         if letter != ' ': cipher += MORSE_CODE_DICT[letter] + ' '
         else: cipher += ' '
    return cipher 
def decrypt(message): 
    message += ' '
    decipher = '' 
    citext = '' 
    for letter in message: 
        if (letter != ' '): 
            i = 0
            citext += letter 
        else: 
            i += 1
            if i == 2 : decipher += ' '
            else: 
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)] 
                citext = '' 
    return decipher
if ed == 'e':
    print(encrypt(c))
    if s == 't':
        from winsound import Beep
        from time import sleep
        for i in encrypt(c):
            if i == '.':
                Beep(1000, round(sec*1000))
                sleep(round(sec))
            elif i == '-':
                Beep(1000, round(sec*3000))
                sleep(round(sec))
            elif i == ' ':
                sleep(round(sec*7))
elif ed == 'd': print(decrypt(c))