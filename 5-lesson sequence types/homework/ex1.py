def numlist(num):
    newl = []
    rev_l = []
    for i in num:
        if len(str(i))>1:
            newl.append(i)
            # onlik = i//10
            # birlik = i%10
            # res = birlik + onlik
            # print(res)
    for i in newl:
        res = str(i)[::-1]
        newnum = int(res)
        rev_l.append(newnum)
    

    def bubble_sort(numlist):
        index = len(numlist)-1
    
        sorted = False
    
        while not sorted:
            sorted = True 
            for i in range(0, index):
                if numlist[i]>numlist[i+1]:
                    numlist[i],numlist[i+1] = numlist[i+1], numlist[i]
        return numlist


    print(bubble_sort(rev_l))
    
    
              
            
numlist([1,2,3,4,50,11,45,39])