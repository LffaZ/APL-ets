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
        self.pinprev_input = 0
        self.new_pin = 0

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
                ut.cprint("AKUN ANDA TELAH DIBLOKIR KARENA TERLALU BANYAK PERCOBAAN LOGIN GAGAL.")
                ut.cprint("SILAKAN KUNJUNGI BANK TERDEKAT ATAU HUBUNGI LAYANAN PELANGGAN UNTUK MEMBUKA BLOKIR.")
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
        print()
        ut.cprint('MASUKKAN PIN LAMA ANDA')
        self.pinprev_input = ut.cinput('')

        while True:
            if not self.verifikasi(self.pinprev_input):
                ut.cprint("VERIFIKASI GAGAL. GANTI PIN DIBATALKAN")
                break

            ut.cprint('MASUKKAN PIN BARU (4 DIGIT):')
            self.new_pin = ut.cinput('')
            if len(self.new_pin) != 4 or not self.new_pin.isdigit():
                print("PIN BARU HARUS TERDIRI DARI 4 DIGIT ANGKA.")
                continue

            ut.cprint('KONFIRMASI PIN BARU:')
            confirm_pin = ut.cinput('')
            if self.new_pin != confirm_pin:
                print("\nPIN BARU YANG ANDA MASUKKAN TIDAK COCOK. SILAKAN COBA LAGI.")
                continue

            self.akun['pin'] = self.new_pin
            self.logger.log_per_akun(self.user_id, f"PIN diubah. PIN baru: {self.new_pin}")
            print("\nPIN BERHASIL DIGANTI!")
            break
