import shutil, csv, os
from akun import Akun

def cprint(text):
    columns = shutil.get_terminal_size().columns
    print(text.center(columns))

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
            saldo = row['Saldo']
            nama = row['Nama']
            login_fail = row['LoginFail'] if row['LoginFail'] else '0'
            akun = Akun(no_rek, nama, pin, saldo, login_fail)
            daftar_akun[no_rek] = akun
    return daftar_akun

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def update_akun(akun_baru, file_path='nasabah.txt'):
    # akun_baru should be Akun class based
    backup_path = file_path.replace('.txt', '_prev.txt')
    shutil.copyfile(file_path, backup_path)  

    with open(backup_path, 'r', encoding='utf-8', newline='') as old_file, \
        open(file_path, 'w', encoding='utf-8', newline='') as new_file:

        reader = csv.DictReader(old_file)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        writer.writeheader()

        updated = False
        for row in reader:
            if row['userID'] == akun_baru[no_rek]:
                writer.writerow({
                    'userID': akun_baru[no_rek],
                    'PIN': akun_baru.pin,
                    'Nama': akun_baru.nama,
                    'Saldo': akun_baru.saldo,
                    'LoginFail': akun_baru.login_fail
                })
                updated = True
            else:
                writer.writerow(row)

        if not updated:
            writer.writerow({
                'userID': akun_baru[no_rek],
                'PIN': akun_baru.pin,
                'Nama': akun_baru.nama,
                'Saldo': akun_baru.saldo,
                'LoginFail': akun_baru.login_fail
            })