def booleanPracitce():
    spam = True
    print(spam)
    spam = 42 == 42
    print(spam)
    spam = 2 != 3
    print(spam)
    spam = 2 != 2
    print(spam)
    spam = 42 == 99
    print(spam)
    spam = 'hello' == 'hello'
    print(spam)
    spam = 'hello' == 'Hello'
    print(spam)
    spam = 'dog' != 'cat'
    print(spam)
    spam = True == True
    print(spam)
    spam = True != False
    print(spam)
    spam = 42 == 42.0
    print(spam)
    spam = 42 == '42'
    print(spam)
    spam = 42 < 100
    print(spam)
    spam = 42 > 100
    print(spam)
    spam = 42 < 42
    print(spam)
    eggs = 42
    spam = eggs <= 42
    print(spam)
    my_age = 29
    spam = my_age >= 10
    print(spam)

def booleanOperators():
    spam = True and True
    print(spam)
    spam = True and False
    print(spam)
    spam = True and True
    print(spam)
    spam = True and False
    print(spam)
    spam = False and True
    print(spam)
    spam = False and False
    print(spam)
    spam = False or True
    print(spam)
    spam = False or False
    print(spam)
    spam = True or True
    print(spam)
    spam = True or False
    print(spam)
    spam = False or True
    print(spam)
    spam = False or False
    print(spam)

def booleanComparisons():
    spam = (4 < 5) and (5 < 6)
    #True and True
    print(spam)
    spam = (4 < 5) and (9 < 6)
    #True and FAlse
    print(spam)
    spam = (1 == 2) or (2 == 2)
    #False and True
    print(spam)
    spam = 4
    2 + 2 == spam and not 2 + 2 == (spam + 1) and 2 * 2 == 2 + 2
    print(spam)

def fibonacciSeries():
    a, b = 0, 1
    while a < 10:
        print(a)
        a, b = b, a+b

def smallProgram():
    username = 'Mary'
    password = 'Swordfish'
    if username == 'Alice':
        print('Hello Alice')
    elif username  == 'Mary':
        print('Hello Mary.')
        if password == 'Swordfish':
            print('Access granted')
        else:
            print('wrong password DORK!')

def aliceProgram():
    name = 'Alice'
    if name == 'Alice':
        print('Hello Alice')
    else:
        print('FUCK YOU!!!')

def aliceProgramTwo():
    name = 'no'
    if name == 'Alice':
        print('hello Alice')
    else:
        print('DIE!!!')

def aliceAge():
    name = 'no'
    age = 33
    if name == 'Alice':
        print('Hello Alice')
    elif age > 10:
        print('old mfer')

def vampyreProgram():
    name = 'Carol'
    age = 3000
    if name == 'Alice':
        print('Hi Alice')
    elif age < 12:
        print('You are not Alice, Kiddo')
    elif age > 2000:
        print('Unlike you, Alice is not an undead, immortal vampire.')
    elif age > 100:
        print('You are nto Alice, Grannie')
        
def vampyreProgramTwo():
    name = 'Carol'
    age = 3000
    if name == 'Alice':
        print('Hi, Alice')
    elif age < 12:
        print('You are not alice Kiddo')
    elif age > 100:
        print('You are not alice Grandma')
    elif age > 2000:
        print('old mfer')

def vampyreProgramThree():
    name = 'Carol'
    age = 3000
    if name =='Alice':
        print('Hi alice')
    elif age < 12:
        print('die')
    else: 
        print('whatever loser')

def oppositeDay():
    today_is_opposite_day = False
    if today_is_opposite_day == True:
        say_it_is_opposite_day = True
    else:
        say_it_is_opposite_day = False

    if today_is_opposite_day == True:
        say_it_is_opposite_day = not say_it_is_opposite_day

    if say_it_is_opposite_day == True:
        print('Today is oposite Day.')
    else:
        print('Today SUCKS')

oppositeDay()