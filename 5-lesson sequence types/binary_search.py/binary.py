# def binary_seach(my_list, value):
#     start_index = 0
#     count = 0
#     end_index = len(my_list)-1
    
#     while start_index<=end_index:
#         mid_point = start_index + (end_index-start_index)//2
#         mid_point_value = my_list[mid_point]
        
#         count = count + 1
#         if mid_point_value == value:
#             return (mid_point, mid_point_value, count)
        
#         elif value<mid_point_value:
#             end_index = mid_point-1
        
#         else:
#             start_index = mid_point + 1
            
#     return None

# print(binary_seach([5,7,9,79,45,56], 45))

def binary_search(my_l, target):
    low = 0
    high = len(my_l) - 1
    
    while low<=high:
        mid = (low + high) // 2
        if my_l[mid] == target:
            return mid
        elif my_l[mid]>target:
            high = mid - 1
        else:
            low = mid + 1
    
    return None

print(binary_search([1,2,3,4,5], 4))
        





















