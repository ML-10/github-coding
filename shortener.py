inputStr = list(input('Type something: '))
for i in inputStr:
    if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E',  'I',  'O',  'U', ' ']:
        inputStr.remove(i)
    
    
inputStr = ''.join(inputStr)

print(inputStr)
