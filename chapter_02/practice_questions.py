def practiceQuestions():
    while True:
        answer = input('What are two values of the boolean data type')
        if answer == 'True False':
            print('Correct!')
        else:
            print('wrong!')
            continue

    #What are the three boolean operators?
        #>, <, = 
    #Write out the truth tables for each Boolean Operator
        #and = True and True = True
        #True and False = False
        #False and False = True
        #False and True = False
        #or
        #True or False = True
        #True or True = True
        #False or True = True
        #False or False = False
        
    #What do the following expressions evaluate to?
    # (5 > 4) and (3 == 5)
    #False
    # not (5 > 4)
    #False
    # (5 > 4) or (3 == 5)
    #True
    # not ((5 > 4) or (3 == 5))
    #False
    # (True and True) and (True == False)
    #False
    # (not False) or (not True)
    #True

    #What are the 6 comparison operators?
    #!=, ==, >=, <=, >, <

    #What is the difference between the equal to operator and the assignment operator
    #assignment assigns to a variable equal to sees if they are truly matching
    #A condition is always a bool value. If it is true or false. You'd use it in a while loop.
    #Identify the three blocks in this code
    # spam = 0
    # if spam == 10:
        #block
    #     print('eggs')
    #     if spam > 5:
    #     print('bacon')
    #     else:
    #         print('ham')
    #     print('spam')
        #block
    # print('Done')

def practiceExercise():
    while True:
        spam = int(input('Please enter your choice'))
        if spam == 1:
            print('Howdy')
            break
        if spam == 2:
            print('Greetings!')
            break
        else:
            print('Fuck you!')
            continue

practiceExercise()