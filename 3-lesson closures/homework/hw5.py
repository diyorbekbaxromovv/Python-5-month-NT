def func(text, element):
    my_l = []
    for i in text:
        my_l.append(i)
        
    indeks = [index for (index, item) in enumerate(my_l) if item == element]
    return indeks

        
print(func("Diyorbek","k"))        
        