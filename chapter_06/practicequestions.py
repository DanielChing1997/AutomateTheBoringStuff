#   1.  What is []?
    # A list
#   2.  How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
    #spam[2] = 'hello'
# For the following three questions, assume spam contains the list ['a', 'b', 'c', 'd'].

#   3.  What does spam[int(int('3' * 2) // 11)] evaluate to?
    # 'a'
#   4.  What does spam[-1] evaluate to?
    # 'd'
#   5.  What does spam[:2] evaluate to?
    # 'c, d'
# For the following three questions, assume bacon contains the list [3.14, 'cat', 11, 'cat', True].

#   6.  What does bacon.index('cat') evaluate to?
    # 1
#   7.  What does bacon.append(99) make the list value in bacon look like?
    # [3.14, 'cat', 11, 'cat', True, 99]
#   8.  What does bacon.remove('cat') make the list value in bacon look like?
    # [3.14, 11, 'cat', True]
#   9.  What are the operators for list concatenation and list replication?
    # +, = 
# 10.  What is the difference between the append() and insert() list methods?
    #append() adds it to the end, insert() adds it where you specify
# 11.  What are two ways to remove values from a list?
    #del, remove
# 12.  Name a few ways that list values are similar to string values.
    #list values can contain string values, [] is an empty list, '' is an empty string. both begin with something ex. [] list , '' string
# 13.  What is the difference between lists and tuples?
    #tuples are immutable, lists are mutable
# 14.  How do you write the tuple value that has just the integer value 42 in it?
    #tuple('42',)
# 15.  How can you get the tuple form of a list value? How can you get the list form of a tuple value?
    #list(tuple), tuple(list)
# 16.  Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
    #they contain references to the list
# 17.  What is the difference between copy.copy() and copy.deepcopy()?
    #copy.copy will copy the variable, deepcopy copies all the references