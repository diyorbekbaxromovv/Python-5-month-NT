##sinxron ishlashi
import time 
import os

def clock():
    time1 = round(time.time())
    
    
    while True:
        if  (round(time.time()) - time1) % 5==0:
            print("5 seconds")
            time.sleep(1)
def foo():
    for i in os.walk('D\\'):
        print(i[0])
        time.sleep(1)    
def main():
    foo()
    clock()
main()

# 