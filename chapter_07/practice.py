def firstDictionary():
    my_cat = {'size' : 'fat', 'color': 'grey', 'age' : 17}
    print(my_cat)
    print(type(my_cat))
    print(my_cat['size'])

def dictionaryTest():
    spam = ['cats', 'dogs', 'moose']
    bacon = ['dogs', 'moose', 'cats']
    print(spam == bacon)
    eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
    ham = {'species': 'cat', 'age': 8, 'name': 'Zophie'}
    print(eggs == ham)
    try:
        spam = {'name': 'Zophie', 'age': 7}
        spam['color']
    except KeyError:
        print('This isnt gonna work man')

def dictionaryLoop():
    spam = {'Age': '42', 'Name': 'Daniel'}
    for i in spam.values():
        print(i)
    for k in spam.keys():
        print(k)
    for x in spam.items():
        print(x)
    print('color' in spam)
    print('color' in spam.keys())
    print(list(spam.keys()))
    print(spam.keys())

def keyExists():
    picnic_items = {'food': 'apples', 'cups': '2'}
    print('I am bringing ' + str(picnic_items.get('cups', 0)) + ' cups.')
    print('I am bringing ' + str(picnic_items.get('eggs', 50)) + ' eggs.')

def defaultSetting():
    spam = {'name': 'Daniel', 'age': '42'}
    if 'color' not in spam:
        spam['color'] = 'black'

    print(spam)

defaultSetting()    


# keyExists()

# dictionaryLoop()

# dictionaryTest()

# firstDictionary()