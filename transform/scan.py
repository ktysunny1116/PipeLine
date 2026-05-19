import os

class Tscan:
    def __init__(self, root_path):
        self.root_path = root_path
        print(f"[Alert!] Tscan initialized with root path: {self.root_path}")
        
    def print_tree(self, path, max_depth, current_depth=0, indent=""):
        if current_depth > max_depth:
            return
        
        try:
            items = os.listdir(path)
        except FileNotFoundError:
            print(indent + "[Error!] Path not found: " + path)
            return
        except PermissionError:
            print(indent + "[Error!] Permission denied: " + path)
            return
        
        for i, item in enumerate(items):
            full_path = os.path.join(path, item)
            is_last = (i == len(items) - 1)
            prefix = " └── " if is_last else "├── "
            
            print(indent + prefix + item)
            
            if os.path.isdir(full_path):
                new_indent = indent + ("    " if is_last else "│   ")
                self.print_tree(
                    full_path,
                    max_depth,
                    current_depth + 1,
                    new_indent
                )
                
    def collect_files(self, path, max_depth, current_depth=0):
        files = []
        if current_depth > max_depth:
            return files
        try:
            for item in os.listdir(path):
                full_path = os.path.join(path, item)
                if os.path.isdir(full_path):
                    files.extend(self.collect_files(full_path, max_depth, current_depth+1))
                else:
                    files.append(full_path)

        except FileNotFoundError:
            print(f"[Error!] Path not found: {path}")
            pass
        return files
    
