def plus(a,b):
    
    result = a[0]+b[0]
    result2 = a[1]+b[1]
    result3 = a[2]+b[2]
    
    output = str(result) + str(result2) + str(result3)
    return int(output)

print(plus([1,1,1],[2,2,2]))