from autentikasi import Authenticator
from filelog import FileLogger
from bahasa import LanguageSelector
from transaksi import Transaksi
import utils as ut
import msvcrt
import sys

filelog = FileLogger()
file_nasabah = 'data/nasabah.txt'
daftar_akun = ut.load_akun(file_nasabah)
# print(f"# DEBUG: daftar_akun keys = {list(daftar_akun.keys())}")  # DEBUG
auth = Authenticator(daftar_akun)
bahasa = LanguageSelector(['Bahasa Indonesia', 'English', 'Spanish'])
transaksi = Transaksi(start_callback=lambda: start(auth, bahasa, transaksi))

def start(auth, bahasa, transaksi):
    try:
        while True:
            start(auth, bahasa, transaksi)
            if not auth.session:
                ut.cprint("SELAMAT DATANG DI BANK BUKANMAKSUDKUBEGITU")
                ut.cprint("------------------------------------------")
                ut.cprint("WELCOME TO BANK BUKANMAKSUDKUBEGITU")
                print()
                print()
                print()
                ut.cprint("MASUKKAN KARTU ATM ANDA")
                ut.cprint("------------------------")
                ut.cprint("PLEASE INSERT YOUR CARD")
                print()
                print()
                no_rek = auth.inputnorek()
                print(no_rek)
                # print(f"# DEBUG: Input no_rek = '{no_rek}' (type: {type(no_rek)})")  # DEBUG
                bahasa.show_menu()
                pin = auth.inputpin()
                # print(f"# DEBUG: Input PIN = '{pin}' (type: {type(pin)})")  # DEBUG
                # print(pin)
                # akun = auth.login(no_rek, pin)
                akun = auth.login('1234567890', '3333')
                if not akun:
                    break
                transaksi.menu_utama()
            else:    
                break

    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh user (Ctrl+C). Keluar...")

start(auth, bahasa, transaksi)