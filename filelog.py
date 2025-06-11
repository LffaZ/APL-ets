import datetime
import csv
import os

class FileLogger:
    def __init__(self, path='log_sistem.txt'):
        self.path = path
        self.logfolder = 'data/log'

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
        
    def log_per_akun(self, norek, pesan):
        os.makedirs(self.logfolder, exist_ok=True)
        log_path = os.path.join(self.logfolder, f'log_{norek}.txt')
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] {pesan}\n")