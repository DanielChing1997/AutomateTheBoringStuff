import logging
import random
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')

def coinFlip():
    heads = 0
    for i in range(1, 1001):
        if random.randint(0, 1) == 1:
            heads = heads + 1
        if i == 500:
            print('Halfway done!')
    print('Heads came up ' + str(heads), ' times!')

# coinFlip()

 
def factorial(n):
    logging.debug('Start of factorial(' + str(n) + ')')
    total = 1
    for i in range(n+1):
        total *= i + 3
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(' + str(n) + ')')
    return total

# print(factorial(5))
# logging.debug('End of program')

def box_print(symbol,width,height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string')
    if width <= 2:
        raise Exception('Width must be greater than 2')
    if height <= 2:
        raise Exception('Height must be greater than 2')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

# try:
#     box_print('*',4,4)
#     box_print('0',20,5)
#     box_print('x',1,3)
#     box_print('ZZ',3,3)
# except Exception as err:
#     print('An exception happened : ' + str(err))

# try:
#     box_print('ZZ',3,3)
# except Exception as err:
#     print('An exception happened: ' +str(err))

def ageSort():
    ages = [50, 70, 90, 100, 202, 50, 60, 22, 25, 28]
    print(ages)
    ages.sort()
    print(ages)

    assert ages [0] <= ages[-1]

def ageReverse():
    ages = [1,3,4,99,22,3,5,666,433,1,123,445]
    print(ages)
    ages.reverse()
    print(ages)

    assert ages [-1] <= ages[0]

def addThreeNums():
    firstNum = input('Pleae enter your first number')
    secNum = input('Please enter your second number')
    thirdNum = input('Please enter your third number')

    total = firstNum + secNum + thirdNum

    print('Your total is ' + total)

# addThreeNums()

def coinTossBugs():
    guess =''
    while guess not in ('heads', 'tails'):
        print('Please enter in your guess!')
        guess = input()
    toss = random.randint(0,1)
    if toss == guess:
        print('You got it!')
    else:
        print('Nope, guess again!')
        guess = input()
        if toss == guess:
            print('You got it')
        else:
            print('Nope, youu are really bad at this game')

coinTossBugs()