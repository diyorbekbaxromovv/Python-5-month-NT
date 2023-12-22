import re
text_file = open('/Users/user/Desktop/full-stack/back-end/Python/5-month/4-lesson named tuples/homework/req.txt', 'r')
my_l = []
for i in text_file:
    my_l.append(i)
print(my_l)

try:
    for i in my_l:
        print(int(i))
    
except:
    numl = []
    numl.append(int(i))
    print(numl)