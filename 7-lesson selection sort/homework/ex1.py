def add_function(numlist):
    seen = {}
    result = []

    for i, item in enumerate(reversed(numlist)):
        if item in seen:
            result.insert(0, '_')
        else:
            result.insert(0, item)
            seen[item] = i
    
    return result

print(add_function([1,2,3,4,5,6,5]))
