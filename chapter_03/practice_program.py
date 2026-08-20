import random
import sys

def numGuess():

    guessNum = random.randint(1,20)
    i = 0
    while True:
        print("""I am thinking of a number between 1 and 20
        Take a guess.""")
        guess = int(input('>'))
        if guess > guessNum:
            print('Your number is too high!')
            i = i + 1
        elif guess < guessNum:
            print('Your number is too low!')
            i = i + 1
        elif guess == guessNum:
            print('You are correct!')
            print('It took you ', +i ,' guesses')
            break

def rockPaperScissors():
    w = 0
    l = 0
    t = 0
    while True:
        print('%s Wins, %s Losses, %s Ties' %(w,l,t))
        while True:
            print('Please enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit')
            choice = input('>')
            if choice == 'q':
                print('Goodbye!')
                sys.exit()
            if choice == 'r' or choice == 'p' or choice == 's':
                break

        if choice == 'r':
            print('You chose rock!')
        elif choice == 'p':
            print('You chose paper!')
        elif choice == 's':
            print('You chose scissor!')

        computerChoice = random.randint(1,3)
        if computerChoice == 1:
            computer_move = 'r'
            print('Computer chose Rock')
        elif computerChoice == 2:
            computer_move = 'p'
            print('Computer choce Paper!')
        elif computerChoice == 3:
            computer_move = 's'
            print('Computer chose scissors!')

        if choice == computer_move:
            print('Its a tie!')
            t = t + 1
        elif choice == 'r' and computer_move =='s':
            print('You win!')
            w = w + 1
        elif choice == 'p' and computer_move == 'r':
            print('You win!')
            w = w + 1
        elif choice == 's' and computer_move == 'p':
            print('You win!')
            w = w + 1
        elif choice == 'r' and computer_move == 'p':
            print('You lose!')
            l = l + 1
        elif choice == 'p' and computer_move == 's':
            print('You lose!')
            l = l + 1
        elif choice == 's' and computer_move == 'r':
            print('You lose!')
            l = l + 1

rockPaperScissors()