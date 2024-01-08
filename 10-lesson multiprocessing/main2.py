import time 
import multiprocessing
import concurrent.futures

start = time.perf_counter()


def foo(num):
    print(f"Start running {num}...")
    
    time.sleep(num)
    
    return f"Done {num}..."
    

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        seconds = [5,4,3,2,1]
        result = executor.map(foo, seconds)
        
        
    for i in result:
        print(i)