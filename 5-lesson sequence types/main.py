# import random
# # sequence > list is mutable data type
# # String and tuple are immutable data types

# sequence_type = [1,2,3,4,5]
# print(sequence_type.index(5))
# ######Binary search - kitob misoli

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
        
# def bubble_sort(my_list):
#     len_index = len(my_list)-1   
#     sorted = False
#     count = 0
#     while not sorted:
#         count = count + 1
#         sorted = True
        
#         for i in range(0, len_index):
#             if my_list[i]>my_list[i+1]:
#                 sorted = False
#                 my_list[i], my_list[i+1]=my_list[i+1], my_list[i]
                
#     return f"{my_list},sikllar soni {count}"

# print(bubble_sort([10,2,4,12,8,11]))     


        
        


