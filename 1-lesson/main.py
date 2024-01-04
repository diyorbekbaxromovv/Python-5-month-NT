#   C dasturlash tilida строго-типизированный bo'ladi o'zgaruvchi yozilishidan type ni yozish kerak va bitta nomli o'zgaruvchi yaratilsa eski o'zga
# ruvchini hotirasi o'chmaydi chunki type o'zgarmaydi
#  Python tilida dynamic bo'ladi va bitta nomli o'zgaruvchi yaratilsa eski o'zgaruchi hotirasi o'chib ketadi chunki python dynamic shuning uchun yangi 
# boshqa typeda yaratilishi mumkin
# #### shu narsa garbage collection deyiladi



import re
 
 
text = """Regular expressions can be concatenated to form new regular expressions; 
if A and B are both regular expressions, then AB is also a regular expression. In general, 
if a string p matches A and another string q matches B, the string pq will match AB. 
This holds unless A or B contain low precedence operations; boundary conditions between A and B; or have numbered group references.
Thus, complex expressions can easily be constructed from simpler primitive expressions like the ones described here. For details of the 
theory and implementation of regular expressions,
consult the Friedl book [Frie09], or almost any textbook about compiler construction"""


# r"[Tt]he", text - bu The the so'zlarni chaqirib beradi katta va kichik the 
# javob = re.findall(r"[Tt]he", text)
# 
# javob = re.findall("[0123456789]", text)
# javob = re.findall("[0-5]", text)

javob = re.findall("[A-Z]", text)

print(len(javob))    


