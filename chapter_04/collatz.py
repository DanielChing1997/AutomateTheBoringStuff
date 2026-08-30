# Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.

# Then, write a program that lets the user enter an integer and that keeps calling collatz() on that number until the function returns the value 1. 
# (Amazingly enough, this sequence actually works for any integer; sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. 
# Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)

# Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value. 
# To make the output more compact, the print() calls that print the numbers should have a sep=' ' named parameter to print all values on one line.

# The output of this program could look something like this:
import sys


def collatz():
    while True:
    
        try:
            number = int(input('Please enter a number'))
            count = 0
    

            while number != 1:
                if number % 2 == 0:
                    number = number // 2
                    count = count + 1

                else:
                    number = 3 * number + 1
                    count = count + 1 
                   
                print(number)
                print(f"Count = {count}")

        except ValueError:
            print('Please enter a valid number')

        except KeyboardInterrupt:
            print('Thank you!')
            sys.exit()

    

collatz()