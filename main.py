from transform.scan import Tscan
from transform.filters import DataFilter
from io.reader import TextReader, CSVReader
from io.writer import DataWriter
import os

def main():
    root = "./data"
    scanner = Tscan(root)
    
    print(f"scan the structure of \n{root}")
    try:
        depth_limit = int(input("Enter the depth limit for scanning: "))
    except ValueError:
        print("Invalid input. Using default depth limit of 1.")
        depth_limit = 1

    print("\n[current folder structure]")
    scanner.print_tree(root, max_depth=depth_limit)
    
    target_path = input("\n Enter the path to collect files from(or press Enter to keep current path):: ")
    target_path = target_path if target_path else root

    work_files = scanner.collect_files(target_path, max_depth=depth_limit)
    print(f"\n Found {len(work_files)} files: in total.")


    valid_files = list(filter(lambda f: (f.endswith('.csv') or f.endswith('.txt')) and 'backup' not in f, work_files))
    print(f"Target files to process: {len(valid_files)}")

    clean_filter = DataFilter("Cleaner", lambda x: x.strip().upper())

    output_path = "processed_output.tct"
    writer = DataWriter(output_path)
    next(writer)
    
    for file_path in valid_files:
        print(f"Processing: {os.path.basename(file_path)}...")
        reader = CSVReader(file_path) if file_path.endswith('.csv') else TextReader(file_path)

        for row in reader:
            processed_data = clean_filter.apply(row)
            writer.send(processed_data)

    writer.close()
    print(f"\nProcessing complete. Output written to {output_path}")
    

if __name__ == "__main__":
    main()

