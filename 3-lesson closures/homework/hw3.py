def funksiya(matn):
    char_freq = {}
    for char in matn:
        if char in char_freq:
            char_freq[char] = char_freq[char] + 1
        else:
            char_freq[char] = 1
    result = max(char_freq, key = char_freq.get)
    return result

print(funksiya('Diyorbekk'))