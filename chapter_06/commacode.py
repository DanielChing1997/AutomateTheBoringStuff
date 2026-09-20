def commaCode(items):
    result = ""
    if len(items) == 0:
        print("empty")
    for i in range(len(items)):
        if i == (len(items) - 1) and len(items) > 1:
            result += ("and " + (items[i]))
        elif i == (len(items) - 1):
            result += items[i]
        else:
            result += ((items[i]) + ", ")
    return result

print(commaCode(["one", "two", "three"]))