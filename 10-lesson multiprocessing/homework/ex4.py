def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
 
    return left

sorted_array = [1, 3, 5, 6]
target_value = 5
print(search_insert(sorted_array, target_value))
