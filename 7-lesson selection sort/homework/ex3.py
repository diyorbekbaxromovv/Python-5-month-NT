def unique_num(numl):
    digit_count = {}
    for i in numl:
        if isinstance(i, int) and 0 <= i <= 9:
            digit_count[i] = digit_count.get(i, 0) + 1
    for digit, count in digit_count.items():
        if count == 1:
            return digit
    return None
print(unique_num([1, 2, 3, 4, 5, 2, 3, 4, 1]))
