import csv
import os

class CSVGenerator:

    def write(self, data, file_path):
        if not data:
            print("No data to write")
            return
        
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


        print(f"File written: ", {file_path})