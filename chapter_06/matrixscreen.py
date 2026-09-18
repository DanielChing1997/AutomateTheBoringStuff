import random
import sys
import time

WIDTH = 70

try:
    #For each column, when the counter is 0, no stream is shown
    #Otherwise, it acts as a counter for how many times a 1 or a 0 should be displayed
    column = [0] * WIDTH
    while True:
        #Loop over each column
        for i in range(WIDTH):
            if random.random() < 0.02:
                #restart a stream counter on this column
                #stream length will be between 4 and 14 characters long
                column[i] = random.randint(4, 20)

            #print a character in this column
            if column[i] == 0:
                #change this ' '' to '.' to see the empty spaces:
                print(' ', end ='')
            else:
                #print a 0 or a 1
                print(random.choice([0,1]), end ='')
                column[i] -= 1 #Decrements the counter for the column

        print() #print a new line at the beginnign of each column 
        time.sleep(0.1) #each row pauses for a tenth of a second 

except KeyboardInterrupt:
    sys.exit()