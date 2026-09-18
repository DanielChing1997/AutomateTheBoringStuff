import random
import copy

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

def multipleAssignments():
    cat = ['fat', 'gay', 'loud']
    size, color, disposition = cat
    print(size)
    print(color)
    print (disposition)

def enumerationPractice():
    listPractice = ['cat','dog','hamster','poopy']
    for index, item in enumerate(listPractice):
        print(item, 'is number ', str(index))

def randomPractice():
    pets = ['dog','cat','hamster']
    randomPet = random.choice(pets)
    print(randomPet)
    randomShuffle = random.shuffle(pets)
    print(pets)

def findingValues():
    pets = ['dog','cat','hamster']
    print(pets.index('hamster'))

def appendPractice():
    pets = ['dog', 'cat', 'hamster']
    pets.append('poopy')
    print(pets)

def insertPractice():
    pets = ['dog', 'cat', 'hamster']
    pets.insert(2, 'poopy')
    print(pets)

def removePractice():
    pets = ['dog', 'cat', 'hamster']
    pets.remove('dog')
    print(pets)

def sortPractice():
    spam = [1,4,6,78,32,5]
    spamString = ['dog','cat','pervs','network','one million']
    spamString.sort()
    spam.sort()
    print(spam)
    print(spamString)

def reversePractice():
    spam = [1,33,24,222222,55]
    spam.reverse()
    print(spam)

def booleanPractice():
    spam = ['cat','dog']
    if spam[0] == 'cat':
        print('Yes cat')
    else:
        print('No cat')

def emptyListPractice():
    spam = []
    if len(spam) > 0 and spam[0] == 'cat':
        print('A cat yes a cat')
    else:
        print('The first item is not a cat')

def magicEightBall():
    magicBall = ['Yes', 'No', 'Maybe', 'Ask again']
    randomFortune = random.choice(magicBall)
    print(randomFortune)

def magicEightBallAlt():
    magicBall = ['Yes', 'No', 'Maybe', 'Ask again']
    print(magicBall[random.randint(0, len(magicBall) - 1)])

def listTest():
    name = 'Zophie'
    print(name[0])
    print(name[1])
    print(name[0:5])
    nameTest = 'Zo' in name
    print(nameTest)

    for i in name:
        print('**** ' +i,'****')

def stringChange():
    name = 'Zophie a cat'
    new_name = name[0:6] + ' the ' +name[9:12]
    print(name, new_name)
def listChange():
    eggs = ['A', 'B', 'C']
    del eggs[0]
    del eggs[1]
    del eggs[0]
    eggs.append('x')
    eggs.append('y')
    eggs.append('z')
    print(eggs)

def tupleTest():
    firstTuple = (1, 2, 3, 'hey')
    len(firstTuple)
    firstTuple[0]
    print(firstTuple)
    newList = list('hello')
    print(newList)

def mutableList():
    eggs = [0 ,1, 2, 3]
    spam = eggs
    eggs[1] = 'hello'
    print(eggs)
    print(spam)

def appendTest():
    def eggs(some_parameter):
        some_parameter.append('Hello')

    spam = [1,2,3,4]
    print(spam)
    eggs(spam)
    print(spam)

def copyTest():
    spam = ['A','B','C']
    cheese = copy.copy(spam)
    print(spam)
    print(cheese)
    cheese[1] = 42
    print(cheese)

copyTest()

# appendTest()

# mutableList()

# tupleTest()
    
# listChange()

# stringChange()

# listTest()

# magicEightBallAlt()

# emptyListPractice()


# booleanPractice()

# reversePractice()

# sortPractice()

# removePractice()

# insertPractice()

# appendPractice()

# findingValues()

# randomPractice()

# enumerationPractice()

# multipleAssignments()

# petList()

# inAndNotIn()

# forLoopListTwo()

# forLoopList()

# forLoopReview()

# workList()

# delUpdates()

# listUpdates()

# valueUpdates()

# sliceIndex()