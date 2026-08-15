def myFirstProgram():
    #This program says hello and asks for my name.
    print('Hello World!')
    print('What is your name?')
    my_name = input('>')
    print('Hello, ' + my_name, ', It is a pleasure to meet you')
    print('Your name is ' + str(len(my_name)), 'characters long')
    print('What is your age?')
    my_age = input('>')
    print('You will be ' + str(int(my_age) + 1) + ' next year')

myFirstProgram()