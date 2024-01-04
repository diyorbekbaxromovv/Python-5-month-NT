import threading
import time

start = time.perf_counter()

def index():
    print("Running function...")
    time.sleep(1)
    print("Complete function...")

threads = []

for _ in range(10):
    t = threading.Thread(target=index)
    t.start()
    threads.append(t)
    
for thread in threads:
    thread.join()
# thread1 = threading.Thread(target=index)
# thread2 = threading.Thread(target=index)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

finish = time.perf_counter()

print(f"Finished function {round(finish-start,2)} sec")
