import threading
import time
import concurrent.futures

start = time.perf_counter()

def index(secs):
    print(f"Running in {secs} function")
    time.sleep(secs)
    print(f"Completed in {secs} function...")
    
with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [5,4,3,2,1]
    res = [executor.submit(index, secds) for secds in seconds]
    
    for f in concurrent.futures.as_completed(res):
        f.result()

finish = time.perf_counter()

print(f"Finished function {round(finish-start,2)} sec")