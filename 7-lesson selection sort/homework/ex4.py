def raqam(numl, n):
    borraqam = set()
    for num in numl:
        if isinstance(num, int) and 0 <= num <= n:
            borraqam.add(num)
    for digit in range(n + 1):
        if digit not in borraqam:
            numl.append(digit)
            return numl
    return numl

my_list = [1, 2, 3, 4, 5, 2, 3, 4, 1]
n_value = 9
print(raqam(my_list,n_value))
