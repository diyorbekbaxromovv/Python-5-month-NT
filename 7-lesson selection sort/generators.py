# def square_nums(nums):    
#     for i in nums:
#         yield i*i
# my_list = square_nums([2,4,5,7,9])
# for i in my_list:
#     print(i)
    
# my_list = [x*x for x in [2,4,5,6,7]]
# print(my_list)

# import random
# import time

# names = ['Murodjon', 'Boburjon', 'Ikromjon', 'Abdulbosid', 'Javohir']
# majors = ['Math', 'IT', 'History', 'Geography', 'English','Russian']

# def person_list(people_num):
#     result = []
    
#     for i in range(people_num):
#         person = {
#             'id':i,
#             'name':random.choice(names),
#             'major':random.choice(majors)
#         }
#         result.append(person)
        
#     return result

# def person_generator(people_num):
#     for i in range(people_num):
#         person = {
#             'id':i,
#             'name':random.choice(names),
#             'major':random.choice(majors)
#         }
        
        
#     yield person


# time1 = time.time()
# people_list = person_list(1000000)
# time2 = time.time()

# time1 = time.time()
# people_list = person_generator(1000000)
# time2 = time.time()


# print("Funksiya ishlash tezligi {} sekund".format(time2-time1))

