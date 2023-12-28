# with open("sample.txt", "w") as file:
#     file.write("Hello World!")
    
class Open_file:
    def __init__(self, filename, mode) -> None:
        self.filename = filename
        self.mode = mode
        
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exec_type, exec_val, traceback):
        self.file.close()
        

with Open_file("sample7.txt", "w") as file:
    file.write("Salom Dunyo")
    
print(file.closed)