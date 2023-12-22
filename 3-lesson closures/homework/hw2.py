def funksiya(num):
    fnum = num
    digit = num %10
    num2 = digit
    num = num//10
    
    while num >0:
        digit = num%10
        num = num//10
        num2 = num2*10
        num2 = num2+digit
        
    if fnum==num2:
        return "True"
    else:
        return "False"

print(funksiya(122))