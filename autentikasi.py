# Login, Pemanggilan Data Akun, Logout
from filelog import FileLogger
import datetime
import utils as ut
from bahasa import LanguageSelector

bahasa = LanguageSelector(['Bahasa'])

class Authenticator:
    def __init__(self, daftar_akun):
        self.daftar_akun = daftar_akun
        self.logger = FileLogger()
        self.session = None

    def inputnorek(self):
        no_rek = ut.cinput("")
        return no_rek
    
    def inputpin(self):
        ut.cprint('MASUKKAN NOMOR PIN ANDA:')
        pin = ut.cinput("")
        return pin

    def login(self, no_rek, pin):
        # for percobaan in range(3):
            # no_rek = ut.cinput("")
            # pin = ut.cinput("Masukkan PIN: ")
        akun = self.daftar_akun.get(no_rek)

        if akun and akun.verifikasi_pin(pin):
            self.session = akun
            print(f"\nSelamat datang, {akun.nama}!\n")
            self.logger.log_per_akun(no_rek, "Login berhasil")
            return akun

        print("Login gagal.\n")
        akun
        self.logger.log_per_akun(no_rek, "Login gagal: PIN salah")
        print("Akun diblokir sementara.\n")
        return None

    def logout(self):
        if self.session:
            norek = self.session.no_rek
            self.logger.log_per_akun(norek, "Logout")
            print(f"Anda telah logout dari akun {self.session.nama}\n")
            self.session = None