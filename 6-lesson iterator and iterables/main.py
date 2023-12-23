# nums = [1,2,3]
# # print("__iter__")
# i_nums = iter(nums)
# print(next(i_nums))
# print(dir(nums)) #iterables

###Detailed process of working for loop function
nums = [1,2,3]
i_nums = (nums).__iter__()

print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
###

### This is program will be worked without any problems
nums = [1,2,3]
iterator_nums = iter(nums)

while True:
    try:
        item = next(iterator_nums)
        print(item)
        
    except StopIteration:
        break
###

###Range was made by hand
class MyRange:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        count = self.start
        self.start+=1
        
        return self.start - 1

nums = MyRange(1,10)

for i in nums:
    print(i)

