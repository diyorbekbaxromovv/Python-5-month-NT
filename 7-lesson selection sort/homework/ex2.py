def farqi(str1, str2):
    differences = []
    for i in set(str1 + str2):
        if str1.count(i) != str2.count(i):
            differences.append(i)
    return differences
string1 = "abbb"
string2 = "abbbd"

print(farqi(string1, string2))
