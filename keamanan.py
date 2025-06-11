# hashing password 
# verifikasi pin sebelum transaksi
# security.py
import hashlib
import getpass
from datetime import datetime
import os

class Security:
    def __init__(self, pin_plain, user_id=None):
        self.pin = pin_plain
        self.user_id = user_id
        self.akun = self.daftar_akun.get(user_id)
        self.isBanned = self.akun['login_fail'] >= 3

    def verifikasi(self):
        print("\n--- Verifikasi PIN ---")
        pin_input = getpass.getpass("Masukkan PIN Anda: ")
        if pin_input == self.pin:
            if self.isBanned:
                print("Akun Anda telah diblokir karena terlalu banyak percobaan login gagal.")
                print("Silakan kunjungi bank terdekat atau hubungi layanan pelanggan untuk membuka blokir.")
                return False
            print("PIN benar. Akses transaksi diberikan.\n")
            self.log_activity("PIN benar. Akses transaksi diberikan.")
            return True
        else:
            self.akun['login_fail'] += 1
            print("PIN salah. Transaksi dibatalkan.\n")
            self.log_activity("PIN salah. Transaksi dibatalkan.")
            return False

    def isBanned(self, akun):
        if akun['login_fail'] >= 3:
            isBanned = True
        else:
            isBanned = False