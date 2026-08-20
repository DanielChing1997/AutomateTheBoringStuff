import random
import sys

def randomProgram():
    for i in range(5):
        print(random.randint(1,10))

def yourName():
    name = ''
    while name != 'your name':
        print('Please type your name.')
        name = input('>')
    print('Thank you!')

def yourNameTwo():
    while True:
        print('Please type your name.')
        name = input('>')
        if name == 'your name':
            break
    print('Thank you!')

def swordFish():
    password = input('Please enter your own password:')
    username = input('Please enter a username')

 
    usernameEntry = ''
    passwordEntry = ''
    print('Please enter your username:')
    usernameEntry = input('>')
    while True:
        if usernameEntry == username:
            print('Welcome ' +username)
            print('Please enter your password')
            passwordEntry = input('>')
            if passwordEntry == password:
                print('Thank you for logging in!')
                break
            else:
                print('Wrong password. Try again')
        else:
            print('Invalid username')
            
def booleanValues():
    name = ''
    while not name:
        print('Enter your name:')
        name = input('>')
    print('How many guests will you have?')
    num_of_guests = int(input('>'))
    if num_of_guests:
        print('be sure to hav enough room!')
    print('Done!')         

def fiveTimes():
    print('Hello!')
    for i in range(5):
        print('On this iteration, i is set to ' + str(i))
    print('Goodbye!')

def twentyTimes():
    print('Im Gay!')
    for i in range(20):
        print('I am gay' +str(i))
    print('cya')

def carlGauss():
    total = 0
    for num in range(101):
        total = total + num
        print(total)
    print(total)

def whileLoop():
    print('Hello!')
    i = 0
    while i < 5:
        print('On this iteration, i is set to ' + str(i))
        i = i + 1
    print('Goodbye!')

def ownLoop():
    print('Hello!')
    i = 0
    while i < 100:
        print(str(i))
        i = i + 1
    print('yo')

def rangeLoop():
    for i in range(12, 16):
        print(i)

def rangePractice():
    for i in range(0, 10, 2):
        print(i)

def negativeRange():
    for i in range(5,-1,-1):
        print(i)

def sysTest():
    while True:
        print('Type exit to exit.')
        response = input('>')
        if response == 'exit':
            sys.exit()
        print('You typed ' + response + '.')

sysTest()