import random

def function(s, t):
    s = t[:]
    tas_harf = random.choice(s)
    t += tas_harf
    
    return tas_harf

s = ""
t = "y"

random_letter = function(s, t)
print("Tasodifiy qo'shilgan harf:", random_letter)
