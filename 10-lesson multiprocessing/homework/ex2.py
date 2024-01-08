def function(n_l):
    unique_numbers = {}
    for i in range(len(n_l) - 1, -1, -1):
        number = n_l[i]
        if number not in unique_numbers:
            unique_numbers[number] = i
        else:
            n_l[i] = "_"

    n_l.sort(key=lambda x: (x, 0) if x != "_" else (float('inf'), 1))

    return n_l
my_list = [3, 1, 4, 1, 6, 2, 4]
print(function(my_list))
