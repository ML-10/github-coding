import random as r
while True:
    a = str(r.randint(1,15))
    b = str(r.randint(1,15))
    c = str(r.randint(1,15))
    d = str(r.randint(1,15))
    print('{}     {}'.format(a, c))
    print('__  +  __  = ?')
    print('{}     {}'.format(b, d))
    ans1 = float(input('? = a/b\n\na = '))
    ans2 = float(input('b = '))
    if ans1/ans2 == int(a)/int(b) + int(c)/int(d):
        print('correct!')
    else:
        print('no')
