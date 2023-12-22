import re
        
def text(word):
    res = max(word, key =lambda x: len(re.findall(r'[aeiouAEIOU]', x)))
    result = str(res)
    print(f"Eng ko'p unli so'z {result}")

text(["Hello", "World", "Independent"])