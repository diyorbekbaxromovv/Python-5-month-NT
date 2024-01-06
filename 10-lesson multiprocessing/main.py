import time 
import multiprocessing

start = time.perf_counter()


def foo():
    print("Start running")
    
    time.sleep(1)
    
    print("Done Running...")
    

if __name__ == "__main__":
    res = []
    for _ in range(1000):
        p = multiprocessing.Process(target=foo)
        p.start()
        res.append(p)
        
        
    for p in res:
        p.join()
    
    # p1 = multiprocessing.Process(target=foo)
    # p2 = multiprocessing.Process(target=foo)

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    finish = time.perf_counter()
    print(f"Finished in {round(finish-start,2)} seconds")