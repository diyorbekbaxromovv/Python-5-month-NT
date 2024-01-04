import time

start = time.perf_counter()

def index():
    print("Running a function.....")
    time.sleep(3)
    print("Complete a function.....")
    
    
index()

finish = time.perf_counter()

print(f"Finished in {round(finish-start),2} seconds")