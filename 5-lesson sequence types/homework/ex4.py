text = open("/Users/user/Desktop/Fullstack/back-end\Python/5-month/5-lesson sequence types/homework/ex4text.txt", "r")
read = text.read()
text.close()

wl = read.split(" ")
nw = len(wl)

print(nw)    