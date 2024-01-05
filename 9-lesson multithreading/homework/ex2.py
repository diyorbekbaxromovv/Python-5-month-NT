def function(word):
    letters = [c for c in word if c.isalpha()]
    reversed_letters = letters[::-1]

    result = ''
    i = 0

    for char in word:
        if char.isalpha():
            result += reversed_letters[i]
            i += 1
        else:
            result += char

    return result

input_text = "He%llo, Wor!ld!"
result = function(input_text)
print(result)
