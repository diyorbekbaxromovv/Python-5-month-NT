# a = 25


# def my_function():
#     name = "Murodjon"
#     global a
#     print(a,name)
#     a = 30
    
# my_function()    

###########################################
# a = 25
# name = "Boburjon"
# def my_function():
#     name = "Murodjon"
    
    
#     def inner_function():
#         prefix = "Google"
#         global name
#         print(prefix, name)
        
#     inner_function()
    
# my_function()    


#######################Closures

# def my_func():
#     age = 26
#     name = "Murodjon"
    
#     def inner(email):
#         print(email, name)
        
        
#     return inner

# execute = my_func()

# execute("m@gmail.com")
        
#########################

# def counter(start):
#     def increment(step=1):
#         nonlocal start
#         start = start+step
#         print(start)
        
#     return increment

# myfunc = counter(5)


# myfunc()
# myfunc()


# import re 

# text = "Einstein was ranked the programming programing 77 789 456 12 greatest physicist of all time gooogle google gooooooogle"

# output = re.findall(r"programm?ing", text)

# print(output)


text = "Banana"
# my_char = iter(text)

# print(next(my_char))
z