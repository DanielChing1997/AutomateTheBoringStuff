# Write a function that takes a list value as an argument 
# and returns a string with all the items separated by a comma 
# and a space, with and inserted before the last item. 
# For example, passing the previous spam list to the function 
# would return 'apples, bananas, tofu, and cats'. 
# But your function should be able to work with any list 
# value passed to it. Be sure to test the case where an empty list [] is 
# passed to your function.

def commaCode(items):
    #This creates an empty string
    result = ""
    #len(items) gets the amount of items in the list
    #range(len(items)) produces the numbers 0, 1, 2 which is the value index
    #for i in ... runs the code below it once per number. i is set to the number each run
    for i in range(len(items)):
        #if i == len(items) - 1 gets the amount of items (3) and subtracts it by 1 because its indexed like 0, 1, 2 <-- (3 - 1 == 2)
        #len(items) > 1: is true only if the list has more than 1 item in the list
        if i == len(items) - 1 and len(items) > 1:
            #this adds "and " + the final item in the list to result
            result += "and " + str(items[i])
        #This is for items with only 1 item in the list. No and or trailing ,
        elif i == len(items) - 1:
            result += str(items[i])
        #This just prints the item with a ", " at the end of it.
        else:
            result += str(items[i]) + ", "
    return result

print(commaCode(["one", "two", "three"]))



# def forLoopList():
#     supplies = ['pen', 'paper', 'dude', 'hello', 'hey']
#     count = 0
#     for i in range(len(supplies)):
#         print(supplies[count])
#         count = count + 1

# def forLoopListTwo():
#     supplies = ['fire', 'flames', 'paper', 'truth']
#     for i in range(len(supplies)):
#         print('The supply is ' + supplies[i])