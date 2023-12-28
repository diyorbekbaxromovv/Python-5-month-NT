def square_nums(nums):
    
    
    
    for i in nums:
        yield i*i
        
        
    

my_list = square_nums([2,4,5,7,9])

print(my_list)