#named tuples
# from collections import namedtuple

# rgb_colors = {"red":235, "green":64, "blue":52}

# print(rgb_colors["red"]) 
# Color = namedtuple('Color',['red','green','blue'])
# rgb_rang = Color(235, 64, 52)

# # print(type(Color))
# print(rgb_rang)

# user = namedtuple('User',['name', 'age', 'location'])

# def get_user():
#     return [
#         user('Boburjon',25,'Fergana'),
#         user('Murodjon',26,'Namangan'),
#         user('Javohir', 19, 'Mars')
#     ]
    
# for i in get_user():
    # print(f"{i.name} is {i.age} years old from {i.location}")
    
################ datetime

import datetime 
#  weekday bu dushanba 0dan boshlanadi, isoweekday 1 dan
# data = datetime.date.today()
# + days=7 yozilsa 7 kun keyingi sanani chiqarib beradi, - teskarisi
# print(data.weekday())
# tdelta = datetime.timedelta(days=7)
# print(data + tdelta)

# birthdate = datetime.date(2024,1,2)
# print(birthdate)
# print(birthdate - data)


##########################
import pytz
# data = datetime.datetime(2023,12,19,17,8,48,10000)


# data = datetime.datetime.now(tz=pytz.timezone('Asia/Tashkent'))
# print(data.strftime('%B %d, %Y - %H hour %M minutes %S seconds, %A, %W'))
eng_date = 'December 19, 2023'

date = datetime.datetime.strptime(eng_date, '%B %d, %Y')
print(date)

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now(tz=pytz.UTC)
# # dt_utc = datetime.datetime.utcnow()
# print(dt_today)
# print(dt_now)
# print(dt_utc)
# print(dt_now)

# for i in pytz.all_timezones:
#     print(i)
    
# dt_utc = dt_now.astimezone(pytz.timezone('Etc/GMT-5'))
# 
# print(dt_utc)


