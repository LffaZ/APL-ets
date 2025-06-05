# hashing password 
# verifikasi pin sebelum transaksi
# security.py
import hashlib
import getpass

class Security:
    def _init_(self, pin_plain):
        """
        Saat objek dibuat, langsung hash dan simpan PIN-nya.
        """
        self.hashed_pin = self.hash_pin(pin_plain)

    def hash_pin(self, pin):
        """
        Hashing PIN pakai SHA-256.
        """
        return hashlib.sha256(pin.encode()).hexdigest()

    def verifikasi(self):
        """
        Minta input PIN, lalu cocokkan dengan hashed_pin yang disimpan.
        """
        print("\n--- Verifikasi PIN ---")
        pin_input = getpass.getpass("Masukkan PIN Anda: ")
        if self.hash_pin(pin_input) == self.hashed_pin:
            print("PIN benar. Akses transaksi diberikan.\n")
            return True
        else:
            print("PIN salah. Transaksi dibatalkan.\n")
            return False