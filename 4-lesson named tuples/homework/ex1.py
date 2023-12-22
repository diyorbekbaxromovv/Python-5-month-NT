def number(nlist):
    n = 1
    while n< len(nlist):    
        for i in range(len(nlist)-n):
            if nlist[i] > nlist[i+1]:
                nlist[i], nlist[i+1] = nlist[i+1],nlist[i]
                
        n+=1
        
print(number([1,3,4,5,5])) 
