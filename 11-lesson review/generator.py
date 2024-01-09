##sinxron ishlashi
import time 
import os

def foo():
    for i in os.walk('H\\'):
        yield i[0]

def clock():
    time1 = round(time.time())
    
    while True:
        if  (round(time.time()) - time1) % 5==0:
            yield "5 seconds"
        else: 
            yield 0
    
def main():
    data = foo()
    query = clock()
    while True:
        a = next(data)
        b = next(query)
        print(a)
        
        if b: print(b)
        
        time.sleep(1)
        
        
main()
    