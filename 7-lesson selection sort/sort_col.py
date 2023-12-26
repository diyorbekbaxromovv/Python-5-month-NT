def selection_sort(my_list):
    index_length = range(0,len(my_list)-1)
    
    
    for i in index_length:
        min_value = i
        
        for j in range(i+1, len(my_list)):
            if my_list[j]<my_list[min_value]:
                min_value = j
                
    
        if min_value !=i:
            my_list[min_value], my_list[i] = my_list[i], my_list[min_value]
        
        
    
    return my_list

print(selection_sort([8,2,5,11,22,18]))