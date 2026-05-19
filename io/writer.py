class DataWriter:
    def __init__(self, file_path, formatter=None):
        self.file_path = file_path
        self.formatter = formatter if formatter else lambda x: x

    def write(self, data):
        with open(self.file_path, 'a') as f:
            formatted_data = self.formatter(data)
            f.write(str(formatted_data) + "\n")

    def file_writter(file_path):
        print(f"[Writer] '{file_path}' logging initialized.")
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                while True:
                    line = yield
                    if line is not None:
                        f.write(str(line) + "\n")

        except GeneratorExit:
            print(f"[Writer] '{file_path}' logging stopped.")

            