import csv
import os

class FileLogger:
    def __init__(self, path='log_sistem.txt'):
        self.path = path

    def log(self, pesan):
        with open(self.path, 'a') as f:
            f.write(pesan + '\n')

    def tulis_csv(self, file_path, header, data_rows):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data_rows)
        self.log(f"Tulis CSV: {file_path} dengan {len(data_rows)} baris")

    def baca_csv(self, path_csv):
        with open(path_csv, 'r') as f:
            return f.readlines()