import tkinter as tk
from tkinter import ttk
import time 

def sleep_function():
    time.sleep(5)
    
def new_process():
    p = mp.Process(target=sleep_function)
    p.start()
    check_process(p)
    
def check_process(p):
    if not p.is_alive():
        lab['text'] = 'Run qilishdan Keyin'
        
    root.after(2000, check_process(p))
    



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('700x700')
    btn = ttk.Button(root, text = "Run", command=sleep_function)
    btn.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    lab = ttk.Label(root, text="Run qilishdan oldin")
    lab.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
root.mainloop()