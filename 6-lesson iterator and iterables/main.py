# nums = [1,2,3]
# # print("__iter__")
# i_nums = iter(nums)
# print(next(i_nums))
# print(dir(nums)) #iterables

###Detailed process of working for loop function
# nums = [1,2,3]
# i_nums = (nums).__iter__()

# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
###

### This is program will be worked without any problems
# nums = [1,2,3]
# iterator_nums = iter(nums)

# while True:
#     try:
#         item = next(iterator_nums)
#         print(item)
        
#     except StopIteration:
#         break
###

###Range was made by hand
# class MyRange:
#     def __init__(self, start, end) -> None:
#         self.start = start
#         self.end = end
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.start >= self.end:
#             raise StopIteration
#         count = self.start
#         self.start+=1
        
#         return self.start - 1

# nums = MyRange(1,10)

# for i in nums:
#     print(i)

# S.O.L.I.D principles -  

# sOlid
# import time
# class Logger:
#     def __init__(self) -> None:
#         self.prefix = time.strftime('%Y-%B-%d %H:%M:%S', time.localtime())
        
    
#     def log(self, message):
#         # print(self.prefix)
#         print(f"{self.prefix} --> {message}")
    
# class CustomLogger(Logger):
#     def __init__(self) -> None:
#         super().__init__()
#         self.prefix = time.strftime('%Y-%M-%d', time.localtime())

# logger = CustomLogger()
# logger.log("Soat Minut Sekund kerak")


# soLid

# class Creature:
#     def __init__(self, value) -> None:
#         self.value = value
        
#     def eat(self):
#         print('I can eat')
        
        
# dog = Creature({"name": "Reks", "age":5})
# cat = Creature({"name": "Kisa", "age":2})
# hen = Creature({"name": "noname", "age":4})
# horse = Creature(("Olov",8))

# attributes = (dog, cat, hen, horse)

# for i in attributes:
#     print(i.value["name"])

###
# class Creature:
#     def __init__(self, name, age) -> None:
#         self.value = {"name":name, "age":age}
        
#     def eat(self):
#         print('I can eat')
        
        
# dog = Creature("Reks", 5)
# cat = Creature("Kisa", 2)
# hen = Creature("noname", 4)
# horse = Creature("Olov",8)

# attributes = (dog, cat, hen, horse)

# for i in attributes:
#     print(i.value["name"])

###

# solId

# class Creature:
#     def __init__(self, name):
#         self.name = name
#     def eat(self):
#         print("I can eat")

# class SwimmerInterface:  
#     def swim(self):
#         print("I can swim")

# class WalkeInterface: 
#     def walk(self):
#         print("I can walk")

# class TalkerInterface:
#     def talk(self):
#         print("I can talk")
        



# class Human(Creature, SwimmerInterface, WalkeInterface, TalkerInterface):
#     pass

# class Fish(Creature, SwimmerInterface ):
#     pass

# class Snake(Creature):
#     pass

# fish = Fish("skumbria")
# javohir = Human("Javohir")
# snake = Snake("Python")

# snake.eat


# javohir.swim
# javohir.talk
# javohir.walk

# fish.eat
# fish.swim

# soliD

import time


# class TerminalPrinter():
#     def write(self, msg):
#         print(f"{msg}")
        

# class FilePrinter():
#     def write(self,msg):
#         with open('log.txt', 'a+', encoding = "UTF-8") as file:
#             file.write(f"{msg}")
# class Logger:
#     def __init__(self) -> None:
#         self.prefix = time.strftime('%Y-%B-%d %H:%M:%S', time.localtime())
        
#     def log_terminal(self, message):
#         TerminalPrinter().write(f"{self.prefix} --> {message}")
        
#     def log_file(self, message):
#         FilePrinter().write(f"{self.prefix} --> {message}")
    
    
    


# logger = Logger()
# logger.log_terminal

#####

# class TerminalPrinter():
#     def write(self, msg):
#         print(f"{msg}")
        

# class FilePrinter():
#     def write(self,msg):
#         with open('log.txt', 'a+', encoding = "UTF-8") as file:
#             file.write(f"{msg}")
# class Logger:
#     def __init__(self) -> None:
#         self.prefix = time.strftime('%Y-%B-%d %H:%M:%S', time.localtime())
        
#     def log(self, message, object_class):
#         object_class().write(f"{self.prefix} --> {message}")
    
    
    


# logger = Logger()
# logger.log("Hello World", FilePrinter)
# logger.log("Hello World", TerminalPrinter)