print('Welcome to the practice test!')
print("""Question 1: Which of the following are operators?
'hello' 
-88.8
-
/
+
5""")

while True:
    user_input = input('Which ones are operators? Please seperate them with a comma:')
    if user_input == '-,/,+':
        print('Correct!')
        break
    else:
        print('Wrong! Try again!')

print("""Question #2! Which of the following is a variable?
spam
'spam'""")

while True:
    user_input = input('Please enter your answer:')
    if user_input == 'spam':
        print('Correct!')
        break
    else:
        print('Wrong! Try again!')

print("Question #3! Name three data types")

while True:
    user_input = input('Please enter three data types:')
    if user_input == 'str,int,boolean':
        print('Correct!')
        break
    else:
        print('Wrong! Try again!')

print("""Question #4! What does the variable bacon contain after the following code runs?
bacon = 20
bacon + 1""")

while True:
    user_input = input('Please enter your answer:')
    if user_input == '21':
        print('Correct!')
        break
    else:
        print('Wrong! Try Again')

print('Good job, you passed the test!')        
