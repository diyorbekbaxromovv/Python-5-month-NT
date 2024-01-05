from collections import Counter


def function(word_list):
    
    
    
    all = ''.join(word_list)
    
    
    letter_count = Counter(all)
    
    repeating_letters = [letter for letter, count in letter_count.items() if count > 1]
    
    return repeating_letters


print(function(["bella", "label", "roller"]))
