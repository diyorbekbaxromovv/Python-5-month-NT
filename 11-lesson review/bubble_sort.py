def bubble_sort(my_l):
    n = len(my_l)
    
    for i in range(n):
        for j in range(0,n - i - 1):
            if my_l[j]> my_l[j+1]:
                my_l[j], my_l[j+1] = my_l[j+1] , my_l[j]
                
my_list = [5,4,3,2,1]
print(bubble_sort(my_list))

        