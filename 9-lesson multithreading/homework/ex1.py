def function(word):
    unli = "aeiouAEIOU"
    text_list = list(word)
    i, j = 0, len(text_list) - 1

    while i < j:
        while i < j and text_list[i] not in unli:
            i += 1
        while i < j and text_list[j] not in unli:
            j -= 1

        text_list[i], text_list[j] = text_list[j], text_list[i]
        i += 1
        j -= 1

    return ''.join(text_list)

matn = "Hello World"
result = function(matn)
print(result)
