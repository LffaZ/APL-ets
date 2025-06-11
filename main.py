from autentikasi import Authenticator
from filelog import FileLogger
from bahasa import LanguageSelector
import utils as ut
import msvcrt
import sys

filelog = FileLogger()
file_nasabah = 'data/nasabah.txt'
daftar_akun = ut.load_akun(file_nasabah)
auth = Authenticator(daftar_akun)
bahasa = LanguageSelector(['Bahasa Indonesia', 'English', 'Spanish'])

try:
    while True:
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
            no_rek= auth.inputnorek()
            bahasa.show_menu()
            pin = auth.inputpin()
            akun = auth.login(no_rek, pin)
            if not akun:
                break
        else:
            print("== Menu Utama ==")
            print("1. Logout")
            print("2. Keluar")
            pilihan = input("Pilih: ")

            if pilihan == '1':
                auth.logout()
            elif pilihan == '2':
                auth.logout()
                break

except KeyboardInterrupt:
    print("\nProgram dihentikan oleh user (Ctrl+C). Keluar...")