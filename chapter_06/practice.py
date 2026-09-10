def firstLists():
    spamNum = [1, 2, 3]
    spamAnimal = ['cat', 'bat', 'rat', 'elephant']
    spamValues = ['hello', 3.14159, True, None, 42]
    print(spamNum[1])
    print(spamAnimal[3])
    print(spamValues[0])
    print(spamNum[0])
    print(spamAnimal[2])
    print(spamValues[1])

# firstLists()

def secondLists():
    spam = [[1, 2, 3],['cat', 'bat', 'rat']]
    print(spam[1][2])
    print(spam[0][1])

# secondLists() 

def indexPratice():
    spam = ['cat','bat','rat','elephant']
    print(spam[0])
    print(spam[1])
    print(spam[2])
    print('Hello ' + spam[2])

# indexPratice()

def negativeIndex():
    spam = ['cat', 'bat', 'rat', 'elephant']
    print(spam[-1])
    print(spam[-3])
    print('The ' +spam[-1], 'is afraid of the ' +spam[-3])

# negativeIndex()

def sliceIndex():
    spam = ['cat', 'bat', 'rat', 'elephant']
    print(spam[0:4])
    print(spam[1:3])
    print(spam[0:-1])
    print(spam[0:])
    print(spam[:3])
    print(len(spam))

def valueUpdates():
    spam = ['cat', 'bat', 'rat', 'elephant']
    print(spam)
    spam[-1] = 'aardvark'
    print(spam)

def listUpdates():
    spam = [1, 2, 3]
    spamTwo = [4, 5, 6]
    newSpam = spam + spamTwo
    print(newSpam)

def delUpdates():
    spam = [1, 2, 3, 4, 5]
    print(spam)
    del spam[2]
    print(spam)

def workList():
    cat_names = []
    while True:
        print('Enter the name of a cat ' +str(len(cat_names) + 1)
            + ' (or enter nothing to stop.): ')
        name = input()
        if name == '':
            break
        cat_names = cat_names + [name]
    print('The cat names are:')
    for name in cat_names:
        print(' ' + name)

def forLoopReview():
    for i in range(4):
        print(i)

def forLoopList():
    supplies = ['pen', 'paper', 'dude', 'hello', 'hey']
    count = 0
    for i in range(len(supplies)):
        print(supplies[count])
        count = count + 1

def forLoopListTwo():
    supplies = ['fire', 'flames', 'paper', 'truth']
    for i in range(len(supplies)):
        print('The supply is ' + supplies[i])

def inAndNotIn():
    testList = ['howdy', 'hey', 'hello', 'whats up']
    testListTrue = 'howdy' in testList
    testListFalse = 'waddap' in testList
    print(testListTrue)
    print(testListFalse)

def petList():
    my_pets = ['Dog', 'Cat', 'Hamster', 'Guinea Pig']
    while True:
        petChoice = input('Please enter a pet: ')
        if petChoice in my_pets:
            print('Yes we have a ' +petChoice)
            break
        else:
            print('We do not a ' +petChoice)

petList()

# inAndNotIn()


# forLoopListTwo()

# forLoopList()

# forLoopReview()

# workList()

# delUpdates()

# listUpdates()

# valueUpdates()

# sliceIndex()