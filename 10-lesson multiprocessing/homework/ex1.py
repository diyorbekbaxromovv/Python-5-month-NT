def function(numlist):

    if not numlist:
        return 1
    
    sorted_list = sorted(numlist)
    
    for i, num in enumerate(sorted_list, start=1):
        if i != num:
            return i
    
    
    return sorted_list[-1] + 1

my_l = [1,2,4,5]
next_num = function(my_l)
print(next_num)
