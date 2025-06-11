import shutil
import csv
from akun import Akun

def cprint(text):
    columns = shutil.get_terminal_size().columns
    print(text.center(columns))

# def cinput(prompt):
#     columns = shutil.get_terminal_size().columns
#     print(prompt.center(columns))
#     return input()

def cinput(prompt):
    columns = shutil.get_terminal_size().columns
    prompt_len = len(prompt)
    start_pos = (columns - prompt_len) // 2
    print(' ' * start_pos + prompt, end='', flush=True)
    return input()

def load_akun(path):
    daftar_akun = {}
    with open(path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            no_rek = row['userID']
            pin = row['PIN']
            nama = row['Nama']
            akun = Akun(no_rek, nama, pin)
            daftar_akun[no_rek] = akun
    return daftar_akun