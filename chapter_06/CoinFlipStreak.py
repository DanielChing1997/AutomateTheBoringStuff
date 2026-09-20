import random
number_of_streaks = 0
for experiment_number in range(10000):  # Run 100,000 experiments total.
    # Code that creates a list of 100 'heads' or 'tails' values
    headstails = []
    for i in range(100):
        type(i)
        if random.randint(0, 1) == 0:
            headstails.append('H')
        else:
            headstails.append('T')
    for i in range(len(headstails)):
        type(i)
        if headstails[i:i+6] == ['H', 'H', 'H', 'H', 'H', 'H'] or headstails[i:i+6] == ['T', 'T', 'T', 'T', 'T', 'T']:
            number_of_streaks += 1

    
            



    # Code that checks if there is a streak of 6 heads or tails in a row
print(number_of_streaks)
print('Chance of streak: %s%%' % (number_of_streaks / 1000))


# def coinTossBugs():
#     guess =''
#     while guess not in ('heads', 'tails'):
#         print('Please enter in your guess!')
#         guess = input()
#     toss = random.randint(0,1)
#     if toss == guess:
#         print('You got it!')
#     else:
#         print('Nope, guess again!')
#         guess = input()
#         if toss == guess:
#             print('You got it')
#         else:
#             print('Nope, youu are really bad at this game')


    # Code that creates a list of 100 'heads' or 'tails' values
    # if experiment_number == 100 and random.randint(0,1) == 1:
    #     headstails.append('H')
    # elif experiment_number == 100 and random.randint(0,1) == 0:
    #     headstails.append('T')
    # elif random.randint(0,1) == 1:
    #     headstails.append('H, ')
    # else:
    #     headstails.append('T, ')