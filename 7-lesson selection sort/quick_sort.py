def quick_sort(my_list):
    length = len(my_list)
    
    
    if len(my_list)<=1:
        return my_list
    
    else:
        pivot = my_list.pop()
        # print(pivot)
        
    items_katta = []
    items_kichik = []
    
    for i in my_list:
        if i>pivot:
            items_katta.append(i)
        else:
            items_kichik.append(i)
    
    return quick_sort(items_kichik) + [pivot] + quick_sort(items_katta)
print(quick_sort([17,15,2,4,25,6,7]))
