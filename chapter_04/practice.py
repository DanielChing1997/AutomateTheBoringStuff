import random

def get_answer(answer_number):
    if answer_number == 1:
        return 'It is certain'
    elif answer_number == 2:
        return 'It is decidedly so'
    elif answer_number == 3:
        return 'Yes'
    elif answer_number == 4:
        return 'Reply hazy try again'
    elif answer_number == 5:
        return 'Ask again later'
    elif answer_number == 6:
        return 'Concentrate and ask again'
    elif answer_number == 7:
        return 'My reply is no'
    elif answer_number == 8:
        return 'Outlook not so good'
    elif answer_number == 9:
        return 'very doubtful'

#print('Please ask a yes or no question')
#input('>')
#r = random.randint(1,9)
#fortune = get_answer(r)
#print(fortune)

#get_answer()

def hello():
    print('Good morning!')
    print('Good afternoon!')
    print('Good evening!')


def say_hello_to(name):
    print('Good morning, ' + name)
    print('Good afternoon, ' + name)
    print('Good evening, ' + name)

# spam = print('Hello')
# spamTrue = None == spam
# print(spamTrue)

# for i in range(100): #perform 100 coin flips
#     if random.randint(0, 1) == 0:
#         print('H', end=' ')
#     else:
#         print('T', end =' ')

# print('cats','dogs','mice',sep=',')

def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

# a()

# def spam():
#     eggs = 'SPAMSPAM'
#     bacon()
#     print(eggs)
    

# def bacon():
#     ham = 'hamham'
#     eggs = 'BACONBACON'

# spam()

# def spam():
#     eggs = 'spam local'
#     print(eggs) #prints 'spam local'

# def bacon():
#     eggs = 'bacon local'
#     print(eggs)
#     spam()
#     print(eggs)

# # eggs = 'global'
# # bacon()
# # print(eggs)

# def spamTwo():
#     global eggs 
#     eggs = 'spam'

# eggs = 'global'
# spamTwo()
# print(eggs)

# def spam():
#     global eggs
#     eggs = 'spam'

# def bacon():
#     eggs = 'bacon'

# def ham():
#     print(eggs)

# eggs = 'global'
# spam()
# print(eggs)

def spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('Error: Invalid Argument')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))