def mathPractice():
    y = 2 + 2
    print(y)

    x = 2**3, 22 % 8, 22 // 8, 22 / 8,3 * 5, 5 - 2, 2 + 2
    print(x)

    z = 2+3*6, (2+3)*6, 48565878*578453, 2 ** 8, 23/7, 23//7, 23%7, 2 + 2, (5-1)*((7+1/(3-1)))
    print(z)

    a = 'Alice' + 'Bob'
    print(a)

    b = 'Alice' * 5
    print(b)

def variablePractice():
    spam = 40
    print(spam)
    eggs = 2
    print(spam+eggs)
    print(spam+eggs+spam)
    spam = spam + 2
    print(spam)
    spam = 'Hello'
    print(spam)
    spam = 'Goodbye'
    print(spam)

def strIntFloatFunctions():
    a = str(0)
    print(a)
    b=str(-3.14)
    print(b)
    c=int('42')
    print(c)
    d=int('-99')
    print(d)
    e=int(1.25)
    print(e)
    f=int(1.99)
    print(f)
    g=float('-3.14')
    print(g)
    h=float(10)
    print(h)
    spam = input('Please enter an integer:')
    print(spam)
    spam = int(spam)
    print(type(spam))
    newSpam = spam * 10 / 5
    print(newSpam)
    i=int(7.7)
    print(i)
    i=int(7.7) + 1
    print(i)

def typeFunction():
    a = type(42)
    print(a)
    a = type(42.0)
    print(a)
    a = type('forty two')
    print(a)
    name = 'Zophie'
    print(type(name))
    print(len(name))

def roundFunction():
    a = round(3.14)
    print(a)
    a=round(7.7)
    print(a)
    a=round(-2.2)
    print(a)
    a=round(3.14,3)
    print(a)
    a=round(7.77777777,6)
    print(a)
    a=abs(25)
    print(a)
    a=abs(-25)
    print(a)

print("Welcome to practice.py! Which function would you like?")

while True:
    choice = int(input("""Pick your Function!
1: mathPractice
2: variablePractice
3: strIntFloatFunction
4: typeFunction
5: roundFunction
6: exit
Put choice here:"""))

    if choice == 1:
        mathPractice()
    if choice == 2:
        strIntFloatFunctions()
    if choice == 3:
        typeFunction()
    if choice == 4:
        variablePractice()
    if choice == 5:
        roundFunction()
    if choice == 6:
        print("Thank you!")
        break
    else:
        print("Please enter a valid answer.")

