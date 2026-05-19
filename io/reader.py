class BaseReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file=None
        print(f"[Alert!] {self.file_path} 경로에서 reader 준비.")
        
    def __iter__(self):
        try:
            self.file=open(self.file_path, 'r', encoding='utf-8')
        except FileNotFoundError:
            print(f"[Error!] File not found: {self.file_path}")
            self.file=None
        return self
    
    def __next__(self):
        if self.file is None:
            raise StopIteration
            
        line = self.file.readline()
        if not line:
            self.close()
            raise StopIteration
        return line.strip()
    
    def close(self):
        if self.file:
            self.file.close()
            print("[Alert!] File closed. safely.")

class TextReader(BaseReader):
    def __init__(self, file_path):
        super().__init__(file_path)
    
    def __next__(self):
        line = self.file.readline()
        if not line:
            self.close()
            raise StopIteration
        return line.strip()
    
class CSVReader(BaseReader):
    def __init__(self, file_path, delimiter=','):
        super().__init__(file_path)
        self.delimiter = delimiter

    def __next__(self):
        line = self.file.readline()
        if not line:
            self.close()
            raise StopIteration
        return line.strip().split(self.delimiter)
    