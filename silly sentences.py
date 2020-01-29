'''
===========================
|         IMPORTS         |
===========================
'''
from random import randint
'''
===========================
|       DEFINITIONS       |
===========================
'''
name = ['Lee', 'Sam', 'Jacqueline', 'Matthew', 'Lucy', 'Sophia', 'Tom', 'Lynda', 'Maya', 'Palma', 'Louann', 'Jaunita', 'Emmie', 'Catherine', 'Sanford', 'Luis', 'Mose', 'Allyn', 'Lourdes', 'Carly', 'Gaynelle', 'Roosevelt', 'Rae', 'Emmy', 'Jerry', 'Hildegarde', 'Mirta', 'Roxy', 'Breana', 'Chastity', 'Dave', 'Merissa', 'Lanette', 'Olimpia', 'Madonna', 'Hye', 'Ermelinda', 'Claude', 'Tobie', 'Alonzo', 'Tad', 'Sharie', 'Brinda', 'Natacha', 'Abbie', 'Somer', 'Jacalyn', 'Ozella', 'Justine', 'Crissy', 'Alysha', 'Tonda', 'Danyel', 'Rosalie', 'Maryjo', 'Naoma', 'Sulema']
verb = ['rides', 'kicks', 'punches', 'eats', 'annoys', 'calms', 'upsets', 'poops']
noun = ['lion', 'bicycle', 'plane', 'book', 'computer', 'rubber', 'poop', 'turtle', 'snail', 'shell', 'midnight', 'interaction', 'cigarette', 'sector', 'basket', 'definition', 'singer', 'pizza', 'instruction', 'moment', 'republic', 'drawer', 'bedroom', 'nation', 'contract', 'storage', 'currency', 'cousin', 'police', 'setting', 'tennis', 'method', 'discussion', 'concept', 'society', 'solution', 'ability', 'philosophy', 'theory', 'patience', 'winner', 'strategy', 'customer', 'inspector', 'manager', 'variety', 'reception', 'studio', 'instance', 'member', 'baseball', 'promotion', 'initiative', 'analyst', 'investment', 'message', 'injury', 'worker', 'girlfriend', 'internet', 'chemistry', 'comparison', 'importance', 'permission', 'outcome', 'reaction', 'birthday', 'revenue', 'people', 'analysis', 'editor', 'satisfaction', 'procedure', 'honey', 'application', 'administration', 'technology', 'vehicle', 'marketing', 'woman', 'education', 'engine', 'basis', 'cookie', 'secretary', 'magazine', 'quantity', 'photo', 'guitar', 'reflection', 'county', 'insurance', 'presentation', 'equipment', 'sister', 'context', 'obligation', 'lady', 'library', 'student', 'farmer', 'expression', 'emotion', 'entry', 'profession', 'appointment', 'football', 'management', 'piano', 'highway']
def pick(words):
    num_words = len(words)
    num_picked = randint(0, num_words - 1)
    word_picked = words[num_picked]
    return word_picked
x = None
times = input('Times(y/n): ')
if times not in ['y', 'n']: times = 'n'
thenoun = pick(noun)
'''
===========================
|        MAINLOOP         |
===========================
'''
while True:
    x = randint(0, 100)
    thenoun = pick(noun)
    if times == 'y':
        print(pick(name), pick(verb), 'an' if thenoun[0] in ['a', 'e', 'i', 'o' ,'u'] else 'a', thenoun, str(x), 'times', end='.')
    elif times == 'n':
        print(pick(name), pick(verb), 'an' if thenoun[0] in ['a', 'e', 'i', 'o' ,'u'] else 'a', thenoun, end='.')
    input()
    
