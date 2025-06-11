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

    def verifikasi(self):
        print("\n--- Verifikasi PIN ---")
        pin_input = getpass.getpass("Masukkan PIN Anda: ")
        if pin_input == self.pin:
            print("PIN benar. Akses transaksi diberikan.\n")
            self.log_activity("PIN benar. Akses transaksi diberikan.")
            return True
        else:
            print("PIN salah. Transaksi dibatalkan.\n")
            self.log_activity("PIN salah. Transaksi dibatalkan.")
            return False
    
    # def isBanned(self):