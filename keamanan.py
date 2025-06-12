# hashing password 
# verifikasi pin sebelum transaksi
# security.py
import hashlib
import getpass
from datetime import datetime
from filelog import FileLogger
import utils as ut
import os

class Security:
    def __init__(self, user_id=None):
        file_nasabah = 'data/nasabah.txt'
        self.daftar_akun = ut.load_akun(file_nasabah)
        if user_id is not None:
            try:
                # print(f"# DEBUG: user_id received = {user_id} (type: {type(user_id)})")  # DEBUG
                self.akun = self.daftar_akun.get(user_id)
                # print(f"# DEBUG: akun in security = {self.akun}")  # DEBUG
                print(self.akun['nama'])
                if self.akun is None:
                    ut.cprint('TRANSAKSI TIDAK DAPAT DIPROSES.\nDATA AKUN TIDAK VALID ATAU TIDAK TERDAFTAR')
                    raise ValueError("Akun tidak ditemukan.")
                
                self.pin = self.akun['pin']
                self.user_id = user_id
                self.logger = FileLogger()
                print(f'Pin: {self.pin}')
                print(f'login_fail: {self.akun['login_fail']}')
                print(f'Tipe login_fail: {type(self.akun['login_fail'])}')
                self.isBanned = int(self.akun['login_fail']) >= 3
                # print(f"# DEBUG: Stored PIN = '{self.pin}' (type: {type(self.pin)})")  # DEBUG

            except ValueError as e:
                print(f"TRANSAKSI TIDAK DAPAT DIPROSES: {e}")
                self.akun = None
                self.pin = None
                self.isBanned = False
        else:
            self.akun = None
            self.pin = None
            self.isBanned = False

    def verifikasi(self, pin_input):
        # print(f"# DEBUG: Input PIN = '{pin_input}' (type: {type(pin_input)})")  # DEBUG
        pin_input = pin_input or getpass.getpass("Masukkan PIN Anda: ")
        # print(pin_input)
        if pin_input == self.pin:
            if self.isBanned:
                ut.cprint("Akun Anda telah diblokir karena terlalu banyak percobaan login gagal.")
                ut.cprint("Silakan kunjungi bank terdekat atau hubungi layanan pelanggan untuk membuka blokir.")
                return False
            print("PIN benar. Akses transaksi diberikan.\n")
            self.logger.log_per_akun(self.user_id, "Login berhasil")
            return True
        else:
            # print(f"# DEBUG: Login gagal. PIN salah untuk no_rek = {self.akun['no_rek']}")  # DEBUG
            print(self.akun['no_rek'])
            self.akun['login_fail'] = int(self.akun['login_fail']) + 1
            self.logger.log_per_akun(self.user_id, "Login berhasil")
            print("PIN salah. Transaksi dibatalkan.\n")
            return False
        print('ADUH KELUAR BRO')

    def isBanned(self):
        if int(self.akun['login_fail']) >= 3:
            isBanned = True
        else:
            isBanned = False

    def ganti_pin(self):
        ut.cprint("\n===================================")
        ut.cprint("---------  GANTI PIN ATM  ---------")
        ut.cprint("===================================")

        if not self.verifikasi():
            print("Verifikasi gagal. Ganti PIN dibatalkan.")
            return

        while True:
            new_pin = getpass.getpass("Masukkan PIN Baru (4 digit): ")
            if len(new_pin) != 4 or not new_pin.isdigit():
                print("PIN baru harus terdiri dari 4 digit angka.")
                continue

            confirm_pin = getpass.getpass("Konfirmasi PIN Baru: ")
            if new_pin != confirm_pin:
                print("\nPIN baru yang Anda masukkan tidak cocok. Silakan coba lagi.")
                continue

            self.akun['pin'] = new_pin
            self.logger.log_per_akun(self.user_id, "PIN berhasil diganti")
            print("\nPIN berhasil diganti!")
            break
