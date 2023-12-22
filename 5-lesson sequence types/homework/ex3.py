def bubble_sort(numlist):
        index = len(numlist)-1
    
        sorted = False
    
        while not sorted:
            sorted = True 
            for i in range(0, index):
                if numlist[i]<numlist[i+1]:
                    sorted = False
                    numlist[i],numlist[i+1] = numlist[i+1], numlist[i]
        return numlist
    
    
print(bubble_sort([1,2,3,4,5,6]))