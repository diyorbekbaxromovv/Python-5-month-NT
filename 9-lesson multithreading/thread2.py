import threading
import time
import concurrent.futures

start = time.perf_counter()

def index(secs):
    print("Running function...")
    time.sleep(secs)
    print("Complete function...")
    

    
    
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     t = executor.submit(index)

with concurrent.futures.ThreadPoolExecutor() as executor:
    res = [executor.submit(index, 1.5) for _ in range(10)]
    
    for f in concurrent.futures.as_completed(res):
        f.result()


# threads = []
# for _ in range(10):
#     t = threading.Thread(target=index,args=[1.5])
#     t.start()
#     threads.append(t)
    
# for thread in threads:
#     thread.join()



finish = time.perf_counter()

print(f"Finished function {round(finish-start,2)} sec")