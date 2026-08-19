def ifStatement():
    spam = 0
    if spam < 5:
        print('Hello, world.')
        spam = spam + 1

def whileStatement():
    spam = 0
    while spam < 5:
        print('Hello, world.')
        spam = spam + 1

def booleanPractice():
    spam = bool(0)
    print(spam)
    spam = bool(42)
    print(spam)
    spam = bool('Hello')
    print(spam)
    spam = bool('')
    print(spam)


booleanPractice()